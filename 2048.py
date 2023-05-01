import random

# 初始化游戏面板
def init_board():
    board = [[0 for i in range(4)] for j in range(4)]
    return board

# 在空白位置随机生成一个数字
def generate_number(board):
    empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty.append((i, j))
    if empty:
        x, y = random.choice(empty)
        board[x][y] = 2 if random.random() < 0.9 else 4

# 判断游戏是否结束
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
              
# 检查是否有相邻的两个数字相等
for i in range(3):
    for j in range(3):
        if board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]:
            return False
for i in range(3):
    if board[3][i] == board[3][i+1] or board[i][3] == board[i+1][3]:
        return False
return True

# 显示游戏面板
def print_board(board): 
  for i in range(4): 
    for j in range(4): 
      print(board[i][j], end='\t') 
      print()
      
# 合并相邻的相同数字
def merge(board): for i in range(4): 
    for j in range(3): 
      if board[i][j] == board[i][j+1] and board[i][j] != 0:
            board[i][j] *= 2
            board[i][j+1] = 0
for i in range(4):
    for j in range(3):
        if board[i][j] == 0:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
# 处理玩家的移动操作
def move(board, direction): if direction == 'left': 
    merge(board) 
elif direction == 'right': 
      board = [row[::-1] for row in board] 
    merge(board) 
      board = [row[::-1] for row in board] elif direction == 'up': 
        board = [[board[j][i] for j in range(4)] for i in range(4)] 
     merge(board) 
        board = [[board[j][i] for j in range(4)] for i in range(4)] 
elif direction == 'down': 
  board = [[board[j][i] for j in range(3, -1, -1)] for i in range(4)] 
  merge(board) 
  board = [[board[j][i] for j in range(3, -1, -1)] for i in range(4)] 
return board

# 主函数
def main(): 
  board = init_board() 
  generate_number(board) 
  generate_number(board) 
  print_board(board) 
  while not is_game_over(board): 
    direction = input('Enter direction (left, right, up, down): ') 
    board = move(board, direction) 
    generate_number(board) 
    print_board(board) 
    print('Game over!')

if name == 'main': main()
