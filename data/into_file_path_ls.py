import os
import curses
from colorama import init, Fore, Back, Style

# 初始化 colorama
init()

# 获取所有文件路径的函数
def get_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def main(stdscr):
    # 清屏
    stdscr.clear()

    # 获取文件路径
    try:
        file_paths = get_file_paths('.')
    except Exception as e:
        stdscr.addstr(0, 0, f"Error: {e}")
        stdscr.refresh()
        stdscr.getch()
        return

    if not file_paths:
        stdscr.addstr(0, 0, "No files found in the current directory.")
        stdscr.refresh()
        stdscr.getch()
        return

    # 初始化被选中文件的索引
    selected_index = 0
    
    # 初始化 curses 颜色对
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # 选中的文件路径颜色对
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # 未选中的文件路径颜色对
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # 文件名颜色对
    
    while True:
        stdscr.clear()
        
        # 用颜色显示文件路径
        for i, path in enumerate(file_paths):
            directory, filename = os.path.split(path)
            if i == selected_index:
                stdscr.addstr(i, 0, directory + os.sep, curses.color_pair(1))
                stdscr.addstr(i, len(directory) + 1, filename, curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addstr(i, 0, directory + os.sep, curses.color_pair(2))
                stdscr.addstr(i, len(directory) + 1, filename, curses.color_pair(3))

        # 获取用户输入
        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_index = (selected_index - 1) % len(file_paths)
        elif key == curses.KEY_DOWN:
            selected_index = (selected_index + 1) % len(file_paths)
        elif key == ord('-'):
            break

        stdscr.refresh()

if __name__ == "__main__":
    # 初始化 curses
    curses.wrapper(main)