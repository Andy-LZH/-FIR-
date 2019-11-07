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
pygame.display.set_caption("Hey I'm created by Andy")

# 定时刷新屏幕

FPS = 60
clock = pygame.time.Clock()

# 加载背景图片

base_folder = os.path.dirname(__file__)
img_folder = os.path.join(base_folder, 'images')
background_img = pygame.image.load(os.path.join(img_folder, 'back.jpg')).convert()


# 画出 15*15 棋盘

def draw_background(surface):
    # 导入照片
    surface.blit(background_img, (0, 0))
    grid_side = WIDTH / 16

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


def draw_chess(monitor, position, color):
    all_chess.append((position, color))
    pygame.draw.circle(monitor, color, position, 5)


def draw_movements(monitor):
    for m in all_chess:
        # m[0] 存的是位置，m[1]存的是颜色
        pygame.draw.circle(monitor, m[1], m[0], 16)

# 主循环


event_click = 0
while True:
    clock.tick(FPS)

    # 处理事件

    for event in pygame.event.get():

        # 监听退出事件

        if event.type == pygame.QUIT:
            running = False

        # TODO 监听鼠标点击事件

        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_click += 1
            pos = event.pos
            grid = (int(round(event.pos[0])),
                    int(round(event.pos[1])))

            # 定义白子
            if event_click % 2 == 0:
                print(pos)
                draw_chess(screen, grid, (255, 255, 255))

            # 定义黑子
            else:
                draw_chess(screen, grid, (0, 0, 0))

    # 画出棋盘
    draw_background(screen)
    draw_movements(screen)
    # 刷新屏幕
    pygame.display.flip()


