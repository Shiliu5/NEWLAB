import numpy as np
import random

# 定义游戏棋盘大小
BOARD_SIZE = 4

# 定义动作
ACTIONS = ['up', 'down', 'left', 'right']

# 初始化Q表
Q = np.zeros((BOARD_SIZE, BOARD_SIZE, BOARD_SIZE, BOARD_SIZE, len(ACTIONS)))

# 定义学习率和折扣因子
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9

# 定义训练参数
EPISODES = 10000
MAX_MOVES = 100

# 定义2048游戏逻辑
class Game2048:
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_cells = np.argwhere(self.board == 0)
        if len(empty_cells) > 0:
            row, col = random.choice(empty_cells)
            self.board[row, col] = random.choice([2, 4])

    def move(self, action):
        if action == 'up':
            self.board = np.rot90(self.board, 1)
        elif action == 'down':
            self.board = np.rot90(self.board, 3)
        elif action == 'left':
            self.board = np.rot90(self.board, 2)
        moves = []
        for i in range(BOARD_SIZE):
            merged = False
            row = self.board[i]
            new_row = np.zeros_like(row)
            j = 0
            while j < BOARD_SIZE:
                if row[j] == 0:
                    j += 1
                    continue
                if j < BOARD_SIZE - 1 and row[j] == row[j + 1] and not merged:
                    new_row[j] = 2 * row[j]
                    self.score += new_row[j]
                    merged = True
                    j += 2
                else:
                    new_row[j] = row[j]
                    j += 1
            moves.append(new_row)
        self.board = np.array(moves)
        if action == 'up':
            self.board = np.rot90(self.board, 3)
        elif action == 'down':
            self.board = np.rot90(self.board, 1)
        elif action == 'left':
            self.board = np.rot90(self.board, 2)
        self.add_random_tile()

    def get_state(self):
        return tuple(map(tuple, self.board))

    def is_game_over(self):
        if np.any(self.board == 0):
            return False
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if (i < BOARD_SIZE - 1 and self.board[i, j] == self.board[i + 1, j]) or \
                   (j < BOARD_SIZE - 1 and self.board[i, j] == self.board[i, j + 1]):
                    return False
        return True

# Q-learning算法
def q_learning():
    for episode in range(EPISODES):
        game = Game2048()
        for move in range(MAX_MOVES):
            state = game.get_state()
            if random.random() < 0.1:
                action = random.choice(ACTIONS)
            else:
                action = ACTIONS[np.argmax(Q[state])]
            game.move(action)
            new_state = game.get_state()
            reward = game.score
            if game.is_game_over():
                Q[state][ACTIONS.index(action)] += LEARNING_RATE * (reward - Q[state][ACTIONS.index(action)])
                break
            Q[state][ACTIONS.index(action)] += LEARNING_RATE * (reward + DISCOUNT_FACTOR * np.max(Q[new_state]) - Q[state][ACTIONS.index(action)])

# 测试训练结果
def test_model():
    game = Game2048()
    while not game.is_game_over():
        state = game.get_state()
        action = ACTIONS[np.argmax(Q[state])]
        game.move(action)
    print('Final Score:', game.score)

# 运行训练和测试
q_learning()
test_model()
