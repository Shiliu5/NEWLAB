import sys
import pygame
import random

# 游戏参数
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

# 方块形状
SHAPES = [
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    [
        [1, 1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0]
    ],
    [
        [1, 1, 1],
        [0, 0, 1]
    ]
]

def draw_block(screen, x, y, color, size=GRID_SIZE):
    pygame.draw.rect(screen, color, (x * size, y * size, size, size))
    pygame.draw.rect(screen, BLACK, (x * size, y * size, size, size), 1)

def draw_shape(screen, shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                draw_block(screen, x + j, y + i, COLORS[cell - 1])

def rotate(shape):
    return list(zip(*reversed(shape)))

def check_collision(board, shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if y + i >= len(board) or x + j < 0 or x + j >= len(board[y + i]) or board[y + i][x + j]:
                    return True
    return False

def clear_lines(board):
    full_lines = [i for i, row in enumerate(board) if all(cell for cell in row)]
    if full_lines:
        for i in full_lines:
            del board[i]
            board.insert(0, [0] * GRID_WIDTH)
    return len(full_lines)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")

    board = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    shape = random.choice(SHAPES)
    x, y = GRID_WIDTH // 2 - len(shape[0]) // 2, 0

    clock = pygame.time.Clock()
    speed = 500
    last_time = 0

    while True:
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_shape = rotate(shape)
                    if not check_collision(board, new_shape, x, y):
                        shape = new_shape

        if current_time - last_time > speed:
            if not check_collision(board, shape, x, y + 1):
                y += 1
            else:
                for i, row in enumerate(shape):
                    for j, cell in enumerate(row):
                        if cell:
                            board[y + i][x + j] = cell

                lines_cleared = clear_lines(board)
                if lines_cleared:
                    print(f"Cleared {lines_cleared} line(s)")

                shape = random.choice(SHAPES)
                x, y = GRID_WIDTH // 2 - len(shape[0]) // 2, 0

                if check_collision(board, shape, x, y):
                    break

            last_time = current_time

        if keys[pygame.K_LEFT] and not check_collision(board, shape, x - 1, y):
            x -= 1
        if keys[pygame.K_RIGHT] and not check_collision(board, shape, x + 1, y):
            x += 1

        screen.fill(WHITE)

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell:
                    draw_block(screen, j, i, COLORS[cell - 1])

        draw_shape(screen, shape, x, y)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
