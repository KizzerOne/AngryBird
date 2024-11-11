import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Angry Birds")

# 设置颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置初始位置
bird_x, bird_y = 100, 300
bird_speed_y = 0

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed_y = -10

    # 更新鸟的位置
    bird_speed_y += 1  # 模拟重力
    bird_y += bird_speed_y

    # 绘制背景
    screen.fill(WHITE)

    # 绘制鸟（用矩形代替）
    pygame.draw.rect(screen, RED, (bird_x, bird_y, 50, 50))

    # 绘制障碍物（用矩形代替）
    pygame.draw.rect(screen, GREEN, (400, 300, 50, 200))

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()