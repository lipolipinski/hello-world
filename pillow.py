import pygame
import sys
import random


pygame.init()
screen = pygame.display.set_mode((520, 340))
pygame.display.set_caption('!!!!  this is the greatest  !!!!!')
clock = pygame.time.Clock()
done = False
matrix = []

class Box:
    def __init__(self):
        pass

        # self.color = color
        # self.y = y

    def recta (self):
        pygame.draw.rect(screen,(random.randint(10,255),0,random.randint(10,255)) , pygame.Rect(random.randint(0,520),random.randint(0,340),10,10))


# def box():
#         color = ["red",'blue','purple','green','coral']
#         pygame.Surface.fill(screen, (128,0,random.randint(100,255)))
#         for box in range(10):
#             pygame.draw.rect(screen, (color[random.randint(0,4)]), pygame.Rect(random.randint(0,520),random.randint(0,340),10,10))

# def back():
#     bk_color =

    # return  bk_color


boxes = [Box() for n in range (10000)]

    # box2 = Box( (0,random.randint(100,255),0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit(); sys.exit();
    clock.tick(10)
    # code goes here
    # box()

    # box1 = Box( (random.randint(100,255),0,0))
    # box2 = Box( (0,random.randint(100,255),0))

    # pygame.Surface.fill(screen,(0,0,0))

    for box in boxes:
        box.recta()
    for y in range(34-1):
        for x in range(52-1):
            matrix.append(screen.get_at((x,y)))
            # print(matrix)







    # box1.recta()
    # box2.recta()





    pygame.display.flip()


        # pygame.draw.rect(screen, (0,128,255), pygame.Rect(x, y, 90, 90))
    # print(screen.get_at((70,60)))
    #     if event.type==pygame.KEYDOWN : done = True









