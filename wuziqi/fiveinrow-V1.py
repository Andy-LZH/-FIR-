# _author__ = "Zhuoheng Li"
# __copyright__ = "Copyright (C) 2019 Zhuoheng Li"
# __license__ = "GPL-3.0"
# __version__ = "1.0"

import pygame
import os
# 初始化 PyGame

pygame.init()

# 初始化音乐模板

pygame.mixer.init()

# 设置屏幕大小以及宽度

WIDTH = 912
LENGTH = 912
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Five In Row")
pos = (WIDTH / 2, WIDTH / 2)

# 定时刷新屏幕

FPS = 60
clock = pygame.time.Clock()

# 加载背景图片

base_folder = os.path.dirname(__file__)
img_folder = os.path.join(base_folder, 'images')
background_img = pygame.image.load(os.path.join(img_folder, 'back.jpg')).convert()
grid_side = WIDTH / 16
font_name = pygame.font.get_default_font()


# 画出 15*15 棋盘


def draw_text(surf, text, size):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (243, 173, 173))
    text_rect = text_surface.get_rect()
    text_rect.midtop = pos
    surf.blit(text_surface, text_rect)


def draw_background(surface):
    # 导入照片
    surface.blit(background_img, (0, 0))

    # 设置四个顶点位置

    upper_left = (grid_side, grid_side)
    upper_right = (WIDTH - grid_side, grid_side)
    down_left = (grid_side, WIDTH - grid_side)
    down_right = (WIDTH - grid_side, WIDTH - grid_side)

    # 四个顶点互相连线
    corner_points = [
        # 顶边
        (upper_left, upper_right),
        # 左边
        (upper_left, down_left),
        # 右边
        (upper_right, down_right),
        # 底边
        (down_left, down_right)
    ]
    for line in corner_points:
        pygame.draw.line(surface, (0, 0, 0), line[0], line[1], 2)

    # 画网格

    for i in range(1, 15):
        new = i * grid_side
        pygame.draw.line(surface, (0, 0, 0), (grid_side, new), (WIDTH - grid_side, new), 2)

    for i in range(1, 15):
        new = i * grid_side
        pygame.draw.line(surface, (0, 0, 0), (new, grid_side), (new, WIDTH - grid_side), 2)

    # 画点

    # 五子棋五个关键点
    # TODO grid_side 不知为何储存为 'float' 类型
    pygame.draw.circle(surface, (0, 0, 0), (int(4 * grid_side) + 1, int(4 * grid_side)), 6)
    pygame.draw.circle(surface, (0, 0, 0), (int(4 * grid_side) + 1, int(12 * grid_side)), 6)
    pygame.draw.circle(surface, (0, 0, 0), (int(12 * grid_side) + 1, int(4 * grid_side)), 6)
    pygame.draw.circle(surface, (0, 0, 0), (int(12 * grid_side) + 1, int(12 * grid_side)), 6)
    pygame.draw.circle(surface, (0, 0, 0), (int(12 * grid_side) + 1, int(12 * grid_side)), 6)
    pygame.draw.circle(surface, (0, 0, 0), (int(8 * grid_side) + 1, int(8 * grid_side)), 6)


# TODO 黑白子样式及落点功能

all_chess = []


def if_win(position, color):
    chess_vertical = []
    chess_horizontal = []
    chess_i_slope_obligate = []
    chess_d_slope_obligate = []
    saying = ""
    winning = False

    # determine if  Vertical side has win
    for i in all_chess:

        # Vertical
        if i[0][0] == position[0] * grid_side and i[1] == color:
            chess_vertical.append(i)
            chess_vertical.sort()
            # print(chess_vertical, "chess_horizontal")

        # horizontal
        if i[0][1] == position[1] * grid_side and i[1] == color:

            chess_horizontal.append(i)
            chess_horizontal.sort()
# TODO Need Attention
        for num in range(0, 15):
            if (i[0][0] - grid_side * num == (position[0] * grid_side)
                    and i[0][1] + grid_side * num == (position[1] * grid_side) and i[1] == color) \
                    or (i[0][0] + grid_side * num == (position[0] * grid_side)
                        and i[0][1] - grid_side * num == (position[1] * grid_side)) and (i[1] == color):
                chess_i_slope_obligate.append(i)
                chess_i_slope_obligate.sort()

            if (i[0][0] - grid_side * num == (position[0] * grid_side)
                and i[0][1] - grid_side * num == (position[1] * grid_side)
                    and i[1] == color) or (i[0][0] + grid_side * num == (position[0] * grid_side)
                                           and i[0][1] + 57 * num == (position[1] * grid_side)) and (i[1] == color):
                chess_d_slope_obligate.append(i)
                chess_d_slope_obligate.sort()

    counter_vertical = 0

    for p in chess_vertical:

        for q in range(1, len(chess_vertical)):

            if p[0][1] + grid_side == chess_vertical[q][0][1]:
                counter_vertical += 1
        if counter_vertical == 4:
            winning = True
            saying = "Vertical"

            # TODO Why set count = 0 would always produce count = 0?

    counter_horizontal = 0

    for p in chess_horizontal:
        for q in range(1, len(chess_horizontal)):

            if p[0][0] + grid_side == chess_horizontal[q][0][0]:
                counter_horizontal += 1

        if counter_horizontal == 4:
            winning = True
            saying = "Horizontal"

    counter_d_slope = 0

    for p in chess_d_slope_obligate:

        for q in range(1, len(chess_d_slope_obligate)):

            if p[0][0] + grid_side == chess_d_slope_obligate[q][0][0] \
                    and p[0][1] + grid_side == chess_d_slope_obligate[q][0][1]:
                counter_d_slope += 1

        if counter_d_slope == 4:
            winning = True
            saying = "Decreasing Slope"

    counter_i_slope = 0

    for p in chess_i_slope_obligate:

        for q in range(1, len(chess_i_slope_obligate)):

            if p[0][0] + grid_side == chess_i_slope_obligate[q][0][0] \
                    and p[0][1] - grid_side == chess_i_slope_obligate[q][0][1]:
                counter_i_slope += 1

        if counter_i_slope == 4:
            winning = True
            saying = "Increasing Slope"

    if winning and color == (0, 0, 0):
        text = "BlACK won the game"
        print(text, saying)
        winner = "BLACK"
        return [winner, True]

    if winning and color == (255, 255, 255):
        text = "WHITE won the game"
        print(text, saying)
        # draw_text(screen, text, 32)
        winner = "WHITE"
        return [winner, True]


def draw_movements(monitor):

    for m in all_chess:
        # m[0] 存的是位置，m[1]存的是颜色
        pygame.draw.circle(monitor, m[1], m[0], 16)


def draw_chess(monitor, position, color):

    all_chess.append(((int(position[0] * grid_side), int(position[1] * grid_side)), color))

    pygame.draw.circle(monitor, color, position, 5)


def undo():
    delete_point = all_chess[len(all_chess) - 1]
    all_chess.remove(delete_point)


# 主循环

event_click = 0
running = True
winning_state = False
result = []
while running:
    clock.tick(60)

    if winning_state:
        draw_text(screen, result[0] + " Win Five in row", 32)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                all_chess.clear()
                event_click = 0
                winning_state = False
            if event.type == pygame.QUIT:
                running = False

    # 处理事件

    for event in pygame.event.get():

        # 监听退出事件

        if event.type == pygame.QUIT:
            running = False

        # TODO 监听鼠标点击事件

        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_click += 1
            pos = event.pos
            grid = (int(round(event.pos[0] / (grid_side + .0))),
                    int(round(event.pos[1] / (grid_side + .0))))

            # 定义白子
            if event_click % 2 == 0:
                draw_chess(screen, grid, (255, 255, 255))
                result = if_win(grid, (255, 255, 255))
                if result is not None and result[1] is True:
                    print("Hell Yeah")
                    winning_state = True

            # 定义黑子
            else:
                draw_chess(screen, grid, (0, 0, 0))
                result = if_win(grid, (0, 0, 0))

                if result is not None and result[1] is True:
                    print("Hell Yeah")
                    winning_state = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            undo()
            event_click -= 1

    # 画出棋盘
    draw_background(screen)
    draw_movements(screen)

    # 刷新屏幕
    pygame.display.flip()
