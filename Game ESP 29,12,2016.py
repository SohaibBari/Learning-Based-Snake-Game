import pygame
import time
import random

global d_width
global d_height
d_width=800
d_height=600

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
lightblue=(106,206,250)
lightcoral=(240,128,128)



pygame.init()
display=pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Snake with a weird diet")
clock=pygame.time.Clock()
    
def circle(c_x,c_y,c_r,color=green):
    pygame.draw.circle(display, color, [c_x,c_y], c_r)

def text_objects(text, font, color):
    textSurface= font.render(text,True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,size, sleep,hei=d_height/2, wid=d_width/2,color=black):
    text2= pygame.font.Font("C:\Windows\Fonts\Arial.ttf",size)
    TextSurf,TextRect=text_objects(text,text2,color)
    TextRect.center=(wid,hei)
    display.blit(TextSurf, TextRect)
    if sleep!=0:
        pygame.display.update()
        time.sleep(sleep)

def question(val=1):
    if val==0:
        global Q1
        global Q2
        global a1_x
        global a2_x
        global a3_x
        global a1_y
        global a2_y
        global a3_y
        global a2_d
        global a3_d
        Q1=str(random.randint(1,10))
        Q2=str(random.randint(1,10))
        
        a2_d=random.randint(-10,10)
        a3_d=random.randint(-10,10)
        while a2_d==0:
            a2_d=random.randint(-10,10)
        while a3_d==0 or a3_d==a2_d:
            a3_d=random.randint(-10,10)
        a1_x=40*random.randint(1,19)
        a1_y=40*random.randint(3,14)
        a2_y=40*random.randint(3,14)
        a3_y=40*random.randint(3,14)
        while (a1_y==400 and 100<a1_x>160):
            a1_x=40*random.randint(1,19)
        a2_x=40*random.randint(1,19)
        while abs(a2_x-a1_x)<40 and (a2_y==400 and 100<a2_x>160):
            a2_x=40*random.randint(1,19)
        a3_x=40*random.randint(1,19)
        while (abs(a3_x-a2_x)<40 or abs(a3_x-a1_x)<40) and(a3_y==400 and 100<a3_x>160):
            a3_x=40*random.randint(1,19)
        

        
    answer=int(Q1)+int(Q2)
    message_display(Q1+"+"+Q2,40,0,50,d_width/2,blue)
    message_display(str(answer),20,0, a1_y,a1_x)
    pygame.draw.rect(display,black,[a1_x-20,a1_y-20,40,40],1)
    message_display(str(answer+a2_d),20,0,a2_y,a2_x)
    pygame.draw.rect(display,black,[a2_x-20,a2_y-20,40,40],1)
    message_display(str(answer+a3_d),20,0,a3_y,a3_x)
    pygame.draw.rect(display,black,[a3_x-20,a3_y-20,40,40],1)
    scr=str(score)
    message_display("Score: "+scr,30,0,70,700,red)
    list_ans=[[a1_x,a1_y],[a2_x,a2_y],[a3_x,a3_y]]
    
    return list_ans

def crash(score,wall=0):
    if score<0:
        message_display("You've lost!",80,2,d_height/2,d_width/2,red)
    else:
        score=str(score)
        message_display("Your score is: "+score,80,2,d_height/2,d_width/2,red)
    gameloop()

def designs():
    pygame.draw.rect(display,lightblue,[0,0,800,100])
    #pygame.draw.rect(display,lightcoral,[0,100,800,500])
    pygame.draw.line(display,black,[0,100],[800,100],2)
    pygame.draw.line(display,black,[0,0],[0,600],2)
    pygame.draw.line(display,black,[798,0],[798,600],2)
    pygame.draw.line(display,black,[0,598],[800,598],2)
    pygame.draw.line(display,black,[0,0],[800,0],2)
    

def menu():
    done=False
    global key_setting
    key_setting=0
    global grid_setting
    grid_setting=0
    global border_setting
    border_setting=0
    while not done:
        display.fill(white)

        #Keys Settings
        pygame.draw.rect(display,green,[140,120,220,65])
        pygame.draw.rect(display,green,[400,120,80,65])
        pygame.draw.rect(display,green,[500,120,80,65])
        message_display("Keys Settings",30,0,150,250,white)
        message_display("1",30,0,150,440,white)
        message_display("2",30,0,150,540,white)

        #Grid Settings
        pygame.draw.rect(display,green,[140,220,220,65])
        pygame.draw.rect(display,green,[400,220,80,65])
        pygame.draw.rect(display,green,[500,220,80,65])
        message_display("Grid Settings",30,0,250,250,white)
        message_display("1",30,0,250,440,white)
        message_display("2",30,0,250,540,white)

        #Border Settings
        pygame.draw.rect(display,green,[140,320,220,65])
        pygame.draw.rect(display,green,[400,320,80,65])
        pygame.draw.rect(display,green,[500,320,80,65])
        message_display("Border Settings",30,0,350,250,white)
        message_display("1",30,0,350,440,white)
        message_display("2",30,0,350,540,white)

        #Start
        pygame.draw.rect(display,blue,[300,450,200,100])
        message_display("Start",40,0,500,400,white)

        #DISPLAY BLUE BORDER ON SETTINGS
        if key_setting==1:
            pygame.draw.rect(display,blue,[400,120,80,65],2)
        elif key_setting==2:
            pygame.draw.rect(display,blue,[500,120,80,65],2)

        if grid_setting==1:
            pygame.draw.rect(display,blue,[400,220,80,65],2)
        elif grid_setting==2:
            pygame.draw.rect(display,blue,[500,220,80,65],2)

        if border_setting==1:
            pygame.draw.rect(display,blue,[400,320,80,65],2)
        elif border_setting==2:
            pygame.draw.rect(display,blue,[500,320,80,65],2)

        if grid_setting==0 or key_setting==0 or border_setting==0:
            message_display ("Choose settings",40,0,50,400,blue)
        else:
            message_display ("Press Start to Play",40,0,50,400,blue)

        #Cursor position
        message_display("Info",20,0,500,75)
        mouse_hover=pygame.mouse.get_pos()

        #Keys Settings
        if 400<=mouse_hover[0]<=480 and 120<=mouse_hover[1]<=185:
                    message_display("Uses all 4 keys",15,0,550,100)
        elif 500<=mouse_hover[0]<=680 and 120<=mouse_hover[1]<=185:
                    message_display("Uses only left and right keys",15,0,550,140)

        #Grid Settings
        elif 400<=mouse_hover[0]<=480 and 220<=mouse_hover[1]<=285:
                    message_display("No Grid-like path",15,0,550,100)
        elif 500<=mouse_hover[0]<=680 and 220<=mouse_hover[1]<=285:
                    message_display("Grid-like path",15,0,550,100)

        #Border Settings
        elif 400<=mouse_hover[0]<=480 and 320<=mouse_hover[1]<=385:
                    message_display("Borders are on",15,0,550,100)
        elif 500<=mouse_hover[0]<=680 and 320<=mouse_hover[1]<=385:
                    message_display("Borders are off",15,0,550,100)
        pygame.display.update()

        #Click Settings
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_click=pygame.mouse.get_pos()
                #Keys
                if 400<=mouse_click[0]<=480 and 120<=mouse_click[1]<=185:
                    key_setting=1
                elif 500<=mouse_click[0]<=680 and 120<=mouse_click[1]<=185:
                    key_setting=2

                #Grid Settings
                elif 400<=mouse_click[0]<=480 and 220<=mouse_click[1]<=285:
                    grid_setting=1
                elif 500<=mouse_click[0]<=680 and 220<=mouse_click[1]<=285:
                    grid_setting=2

                #Border Settings
                elif 400<=mouse_click[0]<=480 and 320<=mouse_click[1]<=385:
                    border_setting=1
                elif 500<=mouse_click[0]<=680 and 320<=mouse_click[1]<=385:
                    border_setting=2
                
                #Start
                elif 300<=mouse_click[0]<=500 and 450<=mouse_click[1]<=550:
                    if key_setting!=0:
                        done=True

            
                        
        
        

    
def gameloop():
    c_x= int(120)
    c_y= int(400)

    x_change=2
    y_change=0
    global score
    score=0
    quest=0

    game_exit=False
    move="right"
    coords=[]

    while not game_exit:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
                
            if key_setting==1:
                    if event.type == pygame.KEYUP:
                        if event.key==pygame.K_UP:
                            if move!="up" and move!="down":
                                move="up"
                        elif event.key==pygame.K_DOWN:
                            if move!="up" and move!="down":
                                move="down"
                        elif event.key ==pygame.K_LEFT:
                            if move!="left" and move!="right":
                                move="left"
                        elif event.key==pygame.K_RIGHT:
                            if move!="left" and move!="right":
                                move="right"
            elif key_setting==2:
                    if event.type == pygame.KEYUP:
                        if event.key ==pygame.K_LEFT:
                            if move=="right":
                                move="up"
                            elif move=="up":
                                move="left"
                            elif move=="left":
                                move="down"
                            elif move=="down":
                                move="right"
                            else:
                                print ("Error at left")
                        elif event.key== pygame.K_RIGHT:
                            if move=="right":
                                move="down"
                            elif move=="up":
                                move="right"
                            elif move=="left":
                                move="up"
                            elif move=="down":
                                move="left"
                            else:
                                print ("Error at right")
        if grid_setting==1:
                    if move=="up":
                        y_change=-2
                        x_change=0
                    elif move=="down":
                        x_change=0
                        y_change=2
                    elif move=="left":
                        x_change=-2
                        y_change=0
                    elif move=="right":
                        x_change=2
                        y_change=0
        elif grid_setting==2:
                    if move=="up" and c_x%40==0:
                        y_change=-2
                        x_change=0
                    elif move=="down" and c_x%40==0:
                        x_change=0
                        y_change=2
                    elif move=="left" and c_y%40==0:
                        x_change=-2
                        y_change=0
                    elif move=="right" and c_y%40==0:
                        x_change=2
                        y_change=0

        display.fill(white)
        
        speeed=(score//10)+1
        while speeed>=0:
            if x_change>0:
                c_x+=1
            if x_change<0:
                c_x-=1
            if y_change>0:
                c_y+=1
            if y_change<0:
                c_y-=1
            coords.append([c_x,c_y])
            speeed-=1

            
        #CIRCLE AMOUNT
        no_circles=score
        count=0
        while count<=no_circles:
            c_r=20
            spot=len(coords)-1-20*(count)
            circle(coords[spot][0],coords[spot][1],c_r)
            count+=1
            if count>1:
                if (coords[spot][0]-10<c_x<coords[spot][0]+10) and coords[spot][1]-10<c_y<coords[spot][1]+10 or(coords[spot][0]<c_x+10<coords[spot][0]+10 and coords[spot][1]<c_y+10<coords[spot][1]+10):
                    crash(score)
                spot+=1

        #Calling all the colorful things and then questions
        designs()
        if quest==1:
            answers=question()
        if quest==0:
            answers=question(0)
            quest=1

        #CRASH AT WALL
        if border_setting==1:
            if c_x<=c_r or c_x>=d_width-c_r or c_y<100+c_r or c_y>=d_height-c_r:
                crash(score,1)
        if border_setting==2:
            if c_x<c_r and move=="left":
                c_x=820
            elif c_x>d_width and move=="right":
                c_x=0
            elif c_y<100 and move=="up":
                c_y=600
            elif c_y>=d_height and move=="down":
                c_y=100

        #SCORE
        if (a1_x-20<=c_x-19<=a1_x+20 or a1_x-20<=c_x+19<=a1_x+20) and (a1_y-20<=c_y-19<=a1_y+20 or a1_y-20<=c_y+19<=a1_y+20):
            score+=1
            quest=0
        if ((a2_x-20<=c_x-19<=a2_x+20 or a2_x-20<=c_x+19<=a2_x+20) and (a2_y-20<=c_y-19<=a2_y+20 or a2_y-20<=c_y+19<=a2_y+20)) or ((a3_x-20<=c_x-19<=a3_x+20 or a3_x-20<=c_x+19<=a3_x+20) and (a3_y-20<=c_y-19<=a3_y+20 or a3_y-20<=c_y+19<=a3_y+20)):
            score-=1
            quest=0
            if score<0:
                crash(score)

        
        
        pygame.display.update()
        clock.tick(60)
menu()
gameloop()
pygame.quit()
quit()
    
    
    
