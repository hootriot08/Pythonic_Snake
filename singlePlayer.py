import pygame as pg
import sys
import random as r
import util
def gameOver(arg, step):
    pg.init()
    screen = pg.display.set_mode((util.WIDTH, util.HEIGHT))
    pg.display.set_caption(arg)
    running =True
    while running:
        clicked = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
        screen.fill(util.LIGHT_GREEN)
        util.board(screen, step, util.DARK_GREEN)
        pg.draw.rect(screen, (240, 211, 132), ((util.WIDTH-600)/2, (util.HEIGHT/3)+20-60,600,360))
        image = pg.image.load('images/gameOver.png')
        screen.blit(image, ((util.WIDTH-630)/2,(util.HEIGHT/3)+20-60))
        imag1 = pg.image.load('images/exit.png')
        imag2 = pg.image.load('images/again.png')
        exit = util.Button(screen, (imag1.get_width()/2 + (util.WIDTH-600)/2 + 20,450+140-60-60-30,imag1.get_width(), imag1.get_height()), imag1, pg.mouse.get_pos(), clicked)
        again = util.Button(screen, (imag1.get_width()/2 + (util.WIDTH-600)/2 + 20,550+140-60-60-30,imag2.get_width(), imag2.get_height()), imag2, pg.mouse.get_pos(), clicked)     
        if exit.check():
            sys.exit()
        if again.check():
            singlePlayer()
        pg.display.flip()
    pg.quit()
def singlePlayer():
    step = 36
    pHL = []
    segs = []
    all_snake_sprites = pg.sprite.Group()
    score = 0
    pg.init()
    screen = pg.display.set_mode((util.WIDTH, util.HEIGHT))
    clock = pg.time.Clock()
    running = True
    fps = 13.5
    pg.display.set_caption('The Pythonic Snake - Single Player')
    y = 12*step+ 60
    x = 12*step
    x1 = r.randint(0,24)*step
    y1 = r.randint(0,24)*step + 60
    up = True
    down = False
    left = False
    right = False
    font = pg.font.Font(None, 32*3)
    iterator = 0
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and not snake1.down:
                    up = True
                    down = False
                    left = False
                    right = False
                    if iterator % 2 ==0:
                        util.playSound('sounds/blip1.wav', .35)
                    else:
                        util.playSound('sounds/blip2.wav', .35)
                    iterator +=1
                elif event.key == pg.K_DOWN and not snake1.up:
                    up = False
                    down = True
                    left = False
                    right = False
                    if iterator % 2 ==0:
                        util.playSound('sounds/blip1.wav', .35)
                    else:
                        util.playSound('sounds/blip2.wav', .35)
                    iterator +=1
                elif event.key == pg.K_LEFT and not snake1.right:
                    up = False
                    down = False
                    left = True
                    right = False
                    if iterator % 2 ==0:
                        util.playSound('sounds/blip1.wav', .35)
                    else:
                        util.playSound('sounds/blip2.wav', .35)
                    iterator +=1
                elif event.key == pg.K_RIGHT and not snake1.left:
                    up = False
                    down = False
                    left = False
                    right = True
                    if iterator % 2 ==0:
                        util.playSound('sounds/blip1.wav', .35)
                    else:
                        util.playSound('sounds/blip2.wav', .35)
                    iterator +=1
        screen.fill(util.LIGHT_GREEN)
        text = font.render(f"Score: {score}", True, (0,0,0))
        screen.blit(text,(0,0,text.get_width(), text.get_height()))
        util.board(screen, step, util.DARK_GREEN)
        curr_x1 = x
        curr_y1 = y
        if up:
            y-=step
        elif down:
            y+=step
        elif left:
            x-=step
        elif right:
            x+=step
        snake1 = util.Snake(screen, util.LIGHT_BLUE, x, y, step,step, up, down, left, right)
        snake1.draw()
        i = 0
        for snake in segs:
            if i == 0:
                ogX = snake.rectObj.left
                ogY = snake.rectObj.top
                snake.rectObj.left = curr_x1
                snake.rectObj.top = curr_y1
                i+=1
            else: 
                ogX = snake.rectObj.left
                ogY = snake.rectObj.top
                snake.rectObj.left = pHL[-1][0]
                snake.rectObj.top = pHL[-1][1]
            pHL.append((ogX, ogY))
            snake.draw()
        apple = util.Apple(screen, x1, y1, step)
        preAppleSnakeColl = pg.sprite.spritecollide(apple, all_snake_sprites, False)
        #this inner while is prob why the freezin is happening
        #reinvent the recalibration of apple's x,y if they alr collide with snake
        '''
        while(preAppleSnakeColl):
            apple.x = r.randint(0,25)*step
            apple.y = r.randint(0,25)*step + 60
            preAppleSnakeColl = pg.sprite.spritecollide(apple, all_snake_sprites, False)
            '''
        apple.draw()
        collided_seg = pg.sprite.spritecollide(snake1, all_snake_sprites, False)
        if collided_seg:
            util.playSound('sounds/smash.wav', None)
            gameOver('The Pythonic Snake - Single Player', step)
        if snake1.rectObj.colliderect(apple.rectObj):
            newSnake = util.Snake(screen, util.LIGHT_BLUE, curr_x1, curr_y1, step, step, up, down, left, right)
            segs.append(newSnake)
            all_snake_sprites.add(newSnake)
            score +=1
            util.playSound('sounds/crunch.wav', None)
            x1 = r.randint(0,24)*step
            y1 = r.randint(0,24)*step + 60
        if (snake1.x >= util.WIDTH and snake1.right) or (snake1.x < -1 and snake1.left) or (snake1.y >= util.HEIGHT and snake1.down) or (snake1.y < 59 and snake1.up):
            util.playSound('sounds/smash.wav', None)
            gameOver('The Pythonic Snake - Single Player', step)
        try:
            pg.display.flip()
        except:
            sys.exit()
        clock.tick(fps)
    pg.quit()