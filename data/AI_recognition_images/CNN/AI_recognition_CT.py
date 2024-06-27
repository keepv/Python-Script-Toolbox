import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 假设你已经有了一个包含CT图像的数据集，分为训练集和验证集
# 数据集的结构可能如下：
# dataset/
# ├── train/
# │   ├── class1/
# │   │   ├── image1.jpg
# │   │   ├── image2.jpg
# │   │   └── ...
# │   └── class2/
# │       ├── image1.jpg
# │       ├── image2.jpg
# │       └── ...
# └── validation/
#     ├── class1/
#     │   ├── image1.jpg
#     │   ├── image2.jpg
#     │   └── ...
#     └── class2/
#         ├── image1.jpg
#         ├── image2.jpg
#         └── ...

# 数据预处理
train_datagen = ImageDataGenerator(rescale=1./255)         #将训练图像像素值从0~255缩放到0~1
validation_datagen = ImageDataGenerator(rescale=1./255)     #将测试图像像素值从0~255缩放到0~1

train_generator = train_datagen.flow_from_directory(
    'dataset/train',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary')

validation_generator = validation_datagen.flow_from_directory(
    'dataset/validation',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary')

# 构建模型
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))    #二分类问题

# 编译模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 训练模型
history = model.fit(
    train_generator,
    steps_per_epoch=100,    #根据你的数据集大小调整(steps_per_epoch = 训练集样本总数 / 批次大小)
    epochs=15,
    validation_data=validation_generator,   #根据你的数据集大小调整(validation_steps = 验证集样本总数 / 批次大小)
    validation_steps=50)  

# 评估模型
test_loss, test_acc = model.evaluate(validation_generator)
print('Test accuracy:', test_acc)

# 设置模型检查点回调
checkpoint_path = "model_checkpoint.h5"  # 模型保存的路径和文件名
checkpoint = ModelCheckpoint(checkpoint_path, 
                             monitor='val_loss',  # 监控的指标，这里以验证集的损失为例
                             verbose=1,  # 日志信息的详细程度
                             save_best_only=True,  # 只保存最佳模型
                             mode='min',  # 最佳模型的判断标准，'min'表示最小化指标，'max'表示最大化指标
                             save_weights_only=False,  # 是否只保存权重
                             period=1)  # 每隔多少个epoch保存一次模型

# 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 训练模型并传入ModelCheckpoint回调
history = model.fit(train_generator,
                    steps_per_epoch=100,
                    epochs=15,
                    validation_data=validation_generator,
                    validation_steps=50,
                    callbacks=[checkpoint])

# 加载最佳模型
model.load_weights(checkpoint_path)