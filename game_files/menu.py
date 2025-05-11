import pygame as pg
import singlePlayer
import util
def menu():
    pg.init()
    screen = pg.display.set_mode((util.WIDTH, util.HEIGHT))
    clock = pg.time.Clock()
    running = True
    pg.display.set_caption('The Pythonic Snake - Menu')
    util.playSound('sounds/theme.wav', .2)
    while running:
        clicked = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                        clicked = True
        screen.fill(util.LIGHT_GREEN)
        #program starts here
        mouse_coords = pg.mouse.get_pos()
        screen.blit(util.TITLE, (util.VAL,100))
        single = util.Button(screen, (util.VAL1,425,util.SP.get_size()[0],util.SP.get_size()[1]), util.SP, mouse_coords, clicked)
        if single.check():
            singlePlayer.singlePlayer()
        pg.display.flip()
        clock.tick(60)
    pg.quit()