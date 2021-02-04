import pygame, sys, random

def point(xpoint, ypoint, colour):
    center = (int(xpoint), int(ypoint))
    pygame.draw.circle(screen, colour, center, 2)

pygame.init()
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption(('Sierpiński triangle'))
rgb = (0,0,0)

ax = screen_width / 2
ay = 0

bx = 0
by = screen_height - 4

cx = screen_width - 4
cy = screen_height - 4

point(ax,ay,(0,206,209))
point(bx,by,(255,0,255))
point(cx,cy,(255,255,51))

x = random.randint(0,screen_width - 4)
y = random.randint(0,screen_height - 4)

for i in range(30000):
    point(x, y, rgb)
    chosen = int(random.randint(0,2))
    if chosen == 0:
        x = (x + ax) // 2
        y = (y + ay) // 2
        rgb = (0,206,209)  
    if chosen == 1:
        x = (x + bx) // 2
        y = (y + by) // 2
        rgb = (255,0,255)
    if chosen == 2:
        x = (x + cx) // 2
        y = (y + cy) // 2
        rgb = (255,255,51)
    pygame.display.flip()


while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(80)