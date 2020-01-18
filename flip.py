from pygame import *
import random

#ballpic = image.load('ball.png')
#ballpic.set_colorkey((0,0,0))

#numballs = 4
delay = 1

done = False

#balls = []

BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
stat="Let's Play"

cl=0
top=450

def flip(lst):
   lstposi=-1
   for i in xrange(len(lst)-1):
      if lst[i:i+2]=="++":
         lstposi=i
         if not flip(lst[:i]+"--"+lst[i+2:])[0]:
            return True, i
         else: pass
   return False, lstposi

def chck(lst):
   for i in xrange(len(lst)-1):
      if lst[i:i+2]=="++":
         return True
   return False

def curr_ipt(color):
   curr=""  

   for x in color:
      if x==BLUE:
         curr+="+"
      else:
         curr+="-"
   return curr

init()
screen = display.set_mode((1280, 960))
display.set_caption('Flip game')
event.set_grab(1)

button1 = Rect(400, 400, 200, 100)
draw.rect(screen,RED,button1,0)
button2 = Rect(700, 400, 200, 100)
draw.rect(screen,RED,button2,0)

def text_objects(text, font):
    textSurface = font.render(text, True, GREEN)
    return textSurface, textSurface.get_rect()

smallText = font.SysFont("comicsansms",32)
TextSurf1, TextRect1 = text_objects("Easy", smallText)
TextRect1.center = ( 500, 450 )
screen.blit(TextSurf1, TextRect1)
TextSurf2, TextRect2 = text_objects("Hard", smallText)
TextRect2.center = ( 800, 450 )
screen.blit(TextSurf2, TextRect2)


display.update()
but_cl= False
while but_cl== False:
    for e in event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                but_cl = True
    
        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = e.pos  # gets mouse position
            #draw.circle(screen, RED, [60, 250], 40)
            #display.update()
            # checks if mouse position is over the button

            if button1.collidepoint(mouse_pos):
               numballs=13
               but_cl = True
            if button2.collidepoint(mouse_pos):
               numballs=22
               but_cl = True
screen.fill(0)   
color=[BLUE]*numballs
r=16
space=1200/numballs

left = (1280-r*2-(numballs-1)*space)/2

#for count in range(numballs):
#    balls.append(dict)
#    balls[count] = {'x': 0, 'y': 0, 'xmove': random.randint(1, 2), 'ymove': random.randint(1, 2)}


while done == False:
    screen.fill(0)
    #for count in range(numballs):
    #    screen.blit(ballpic, (100+count*45, 210))
    for count in range(numballs):
        draw.circle(screen, color[count], [left+count*space, top], r)


    time.delay(delay)
    
    button1 = Rect(100, 100, 200, 100)
    draw.rect(screen,RED,button1,0)
    TextSurf1, TextRect1 = text_objects("QUIT", smallText)
    TextRect1.center = ( 200, 150 )
    screen.blit(TextSurf1, TextRect1)
    
    button2 = Rect(400, 100, 200, 100)
    draw.rect(screen,RED,button2,0)
    TextSurf2, TextRect2 = text_objects("REPLAY", smallText)
    TextRect2.center = ( 500, 150 )
    screen.blit(TextSurf2, TextRect2)

    button3 = Rect(700, 100, 200, 100)
    draw.rect(screen,RED,button3,0)
    TextSurf3, TextRect3 = text_objects("NEW GAME", smallText)
    TextRect3.center = ( 800, 150 )
    screen.blit(TextSurf3, TextRect3)


    TextSurf11, TextRect11 = text_objects(stat, smallText)
    TextRect11.center = ( 600, 750 )
    screen.blit(TextSurf11, TextRect11)

    
    display.update()

    for e in event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                done = True

        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = e.pos
            if button1.collidepoint(mouse_pos):
               done = True
            if button2.collidepoint(mouse_pos):
               cl=0
               stat="Let's Play"
               color=[BLUE]*numballs
            if button3.collidepoint(mouse_pos):
               cl=0
               stat="Let's Play"
               if numballs<20:
                  numballs=random.randrange(13, 16)
               else:
                  numballs=random.randrange(22, 25)
                  
               color=[BLUE]*numballs
               r=16
               space=1200/numballs

            for n in xrange(numballs):
               if (mouse.get_pos()[1]-top)**2+(mouse.get_pos()[0]-left-n*space)**2 <=r*r:
                  comp=False
                  if cl==1:
                     if abs(n-temp)==1 and color[n]!=GREEN:
                        color[n]=GREEN
                        cl=0
                        comp=True
                     elif abs(n-temp)>0 and color[n]==GREEN:   
                        pass   
                     elif abs(n-temp)==0:
                        color[temp]=BLUE
                        cl=0       
                     else:
                        color[temp]=BLUE
                        color[n]=GREEN
                        temp=n
                  elif cl==0 and color[n]!=GREEN:
                     color[n]=GREEN
                     cl=1
                     temp=n
                  else: pass   
                  if comp:
                     time.delay(delay)
                     #print curr_ipt(color)
                     p=flip(curr_ipt(color))
                     if p[1]!=-1:
                        color[p[1]]=GREEN
                        color[p[1]+1]=GREEN
                        if not chck(curr_ipt(color)):
                           stat="You Lose"
                     else: 
                        stat="You Win"
  
                  break
            
    #if screen.get_at((mouse.get_pos())) == (255, 255, 255) and event.get.type == pygame.MOUSEBUTTONDOWN:
    #    done = True

