import os
import base64

def process_files(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        # 构造完整的文件路径
        file_path = os.path.join(directory, filename)
        txt_file_path = file_path + '.txt'
        
        # 检查文件名是否没有后缀
        if '.' not in filename:
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 如果对应的.txt文件不存在，则创建它
                if not os.path.exists(txt_file_path):
                    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(content)
                    print(f"创建新文件: {txt_file_path}")
                else:
                    # 如果.txt文件已存在，则替换其内容
                    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(content)
            except Exception as e:
                print(f"处理文件 {filename} 时发生错误: {e}")

def decode_base64(encoded_data):
    try:
        decoded_bytes = base64.b64decode(encoded_data)
        decoded_string = decoded_bytes.decode('utf-8')
        print("解码后的字符串:", decoded_string)
    except Exception as e:
        print("解码失败:", e)

# 设置当前工作目录
current_directory = os.getcwd()

# 处理当前目录下的所有文件
process_files(current_directory)

# 尝试解码
encoded_data = "您的编码数据"
decode_base64(encoded_data)

print("所有文件处理完成")