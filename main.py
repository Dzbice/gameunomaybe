from imports import *
from Player import *
py.init()
WIDTH = 500
HEIGHT = 500
screen = py.display.set_mode((WIDTH,HEIGHT), py.RESIZABLE)

py.display.set_caption("game i guess")

clock = py.time.Clock()
#colors
BLACK = (20,20,20)
WHITE = (255,255,255)
RED = (255,0,0)

class Main():
    def __init__(self):
        pass
    
    def Main(self):
        run = True
        mainplayer = player()
        while run:
            screen.fill(BLACK)
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
            screen.blit(mainplayer.image, mainplayer.rect)
            mainplayer.movement()
            mainplayer.direct()
            py.display.flip()
            clock.tick()
            


if __name__ == "__main__":
    main = Main()
    main.Main()
