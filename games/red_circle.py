import pygame as pg

pg.init()
screen = pg.display.set_mode((1280,720))
clock = pg.time.Clock()
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        screen.fill("purple")
        pg.draw.circle(screen, "red", player_pos, 40)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player_pos.y -= 300 * dt
        if keys[pg.K_s]:
            player_pos.y += 300 * dt
        if keys[pg.K_a]:
            player_pos.x -= 300 * dt
        if keys[pg.K_d]:
            player_pos.x += 300 * dt

        pg.display.flip()
        dt = clock.tick(60) / 1000


pg.quit()