# 定义棋盘大小
BOARD_SIZE = 15

# 初始化棋盘
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# 定义棋子类型
BLACK = '●'
WHITE = '○'

# 当前玩家，默认为黑棋先下
current_player = BLACK

# 打印棋盘
def print_board():
    print('  ' + ' '.join(str(i) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        print(str(i) + ' ' + ' '.join(board[i]))

# 判断是否获胜
def check_win(row, col):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        for i in range(1, 5):
            new_row = row + dx * i
            new_col = col + dy * i
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE and board[new_row][new_col] == current_player:
                count += 1
            else:
                break
        if count == 5:
            return True
    return False

# 游戏主循环
while True:
    print_board()
    print('当前玩家：', current_player)
    move = input('请输入您的落子位置，格式为"行 列"（例如：3 4）：')
    row, col = map(int, move.split())
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == ' ':
        board[row][col] = current_player
        if check_win(row, col):
            print_board()
            print('玩家', current_player, '获胜！')
            break
        current_player = WHITE if current_player == BLACK else BLACK
    else:
        print('无效的落子位置，请重新输入！')
