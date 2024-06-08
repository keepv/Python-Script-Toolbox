import os

def 列出无后缀文件(目录):
    # 列出目录中所有无后缀文件
    文件列表 = [文件 for 文件 in os.listdir(目录) if os.path.isfile(os.path.join(目录, 文件)) and not os.path.splitext(文件)[1]]
    return 文件列表

def 保存文件名(目录):
    while True:
        文件列表 = 列出无后缀文件(目录)
        if not 文件列表:
            print("未找到无后缀文件。")
            return None

        print("无后缀文件列表:")
        for 索引, 文件 in enumerate(文件列表):
            print(f"{索引}: {文件}")

        选择 = input("通过输入文件编号选择文件（直接回车退出）: ")
        if 选择 == '':
            return None
        
        try:
            选择 = int(选择)
            if 选择 < 0 or 选择 >= len(文件列表):
                print("选择无效，请重试。")
                continue

            文件名 = 文件列表[选择]
            return 文件名

        except ValueError:
            print("输入无效，请输入一个数字。")

def 主程序():
    目录 = '.'  # 当前目录
    文件名 = 保存文件名(目录)

    if 文件名:
        print(f"已选择的文件: {文件名}")
    else:
        print("没有任何MIME文件")

if __name__ == "__main__":
    主程序()
    # 在此处添加您希望在循环结束后执行的其他代码
    print("")