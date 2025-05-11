import pygame as pg
pg.init()

#functions

def playSound(sound, var):
    pg.mixer.init()
    effect = pg.mixer.Sound(sound)
    if var!= None:
        effect.set_volume(var)
    effect.play()

def board(screen, step, color):
    W = screen.get_width()
    row = 1
    val = 0 
    for i in range(60 , screen.get_height(), step):
        if row % 2 == 1:
            val = 0
        else:
            val = step
        for io in range(0, W, 2*step):
            pg.draw.rect(screen, color, (io+val,i, step, step))
        row+=1
    pg.draw.line(screen, (0,0,0), (0,60), (WIDTH, 60), 5)

#class definitions

class Snake(pg.sprite.Sprite):
    def __init__(self, screen, color, x,y,height,width, up ,down, left, right):
        super().__init__()
        self.screen = screen
        self.color = color
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.rectObj = pg.Rect(x,y,height,width)
        self.rect = self.rectObj
        self.x = self.rectObj.left
        self.y = self.rectObj.top
    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rectObj)
    def getRect(self):
        return self.rect
class Apple(pg.sprite.Sprite):
    def __init__(self, screen, x, y, step):
        super().__init__()
        image = pg.image.load('images/apple.webp')
        imag1 = pg.transform.scale(image, (step,step))
        self.imag1 = imag1
        self.rectObj = imag1.get_rect()
        self.rectObj.left = x
        self.x = x
        self.y = y
        self.rectObj.top = y
        self.screen = screen
        self.rect = self.rectObj
    def draw(self):
        self.screen.blit(self.imag1, (self.x, self.y))
    def getRect(self):
        return self.rect
class Button:
    bClick = False
    def __init__(self, screen, rect, image, mouse_coords, clicked):
        self.image = image
        self.mouse_coords = mouse_coords
        self.rect = rect
        self.clicked = clicked
        screen.blit(image, (rect[0], rect[1]))
    def check(self):
          if self.clicked and (self.rect[0] <= self.mouse_coords[0]<= self.rect[0] + self.rect[2]) and (self.rect[1] <= self.mouse_coords[1]<= self.rect[1] + self.rect[3]):
            playSound('sounds/buttonSound.wav', None)
            return True
          else:
              return False  
          
#constant vars

CONSTM = 1.25
SP1 = pg.image.load('images/singlePlayer.png')
ogw, ogh = SP1.get_size()
nw = CONSTM*ogw
nh = ogh*CONSTM
SP = pg.transform.scale(SP1, (nw,nh))
nw = CONSTM*ogw
nh = ogh*CONSTM
TITLE = pg.image.load('images/title.png')
WHITE = (255,255,255)
WIDTH = 900
HEIGHT = 900+60
LIGHT_GREEN = (76, 153, 0)
DARK_GREEN = (0,60,5)
LIGHT_BLUE = (0,102,204)
VAL = (WIDTH-TITLE.get_size()[0])/2
VAL1 = VAL + (TITLE.get_size()[0]-SP.get_size()[0])/2