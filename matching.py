import pygame

pygame.init()

WIDTH=600
HEIGHT=600
TITLE="ROCKET IN SPACE"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

go=False
bg1=pygame.image.load("candy.jpg")
bg2=pygame.image.load("ludo.png")
bg3=pygame.image.load("subway.png")
bg4=pygame.image.load("temple.png")


screen.fill("White")

while go==False:
    font=pygame.font.SysFont("comic sans",50)
    option1=font.render("candy crush",True,"Red")
    screen.blit(option1,(300,450))
    pygame.display.update()   
    option2=font.render("ludo",True,"Red")
    screen.blit(option2,(300,300))
    pygame.display.update()    
    option3=font.render("subway surfers",True,"Red")
    screen.blit(option3,(300,150))
    pygame.display.update()   
    option4=font.render("temple run",True,"Red")
    screen.blit(option4,(300,0))
    pygame.display.update()

    screen.blit(bg1,(0,0))
    screen.blit(bg2,(0,150))
    screen.blit(bg3,(0,300))
    screen.blit(bg4,(0,450))


    
    for event in pygame.event.get(): 
      if event.type==pygame.MOUSEBUTTONDOWN:
          pos1=pygame.mouse.get_pos()
          pygame.draw.circle(screen,"Black",pos1,25,0)
      if event.type==pygame.MOUSEBUTTONUP:
          pos2=pygame.mouse.get_pos()
          pygame.draw.circle(screen,"Black",pos2,25,0)
          pygame.draw.line(screen,"Black",pos1,pos2,10)
      if event.type==pygame.QUIT:
        go=True
    pygame.display.update()
    