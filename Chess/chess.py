import pygame
import os
xGrid =8  # 19
yGrid =8 # 25
bw=100
height = yGrid * bw
width = xGrid * bw
fps=60
bouncer=0
clock = pygame.time.Clock()
pygame.init()
w = pygame.display.set_mode((width,height))
Grid=[
    [31,51,41,21,11,43,53,33],
    [61,63,65,67,69,71,73,75],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [60,62,64,66,68,70,72,74],
    [30,50,40,20,10,42,52,32],
     [0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]
Active=[
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1]]
def reset():
    global Active
    Active = [[-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1]]
Selecter=[-1,-1]
def draw_rook(x,y):
    if Grid[x][y] // 10 == 3:
        if Grid[x][y] % 2 == 0:
            c = 301
        else:
            c = 311
        Mouse_Loc = pygame.mouse.get_pos()
        if Active[x][y] == 1 and x == Mouse_Loc[1] // bw and y == Mouse_Loc[0] // bw:
            pygame.draw.rect(w,(150,186,118),(y * bw,x * bw,bw + 1,bw + 1))
        if Active[x][y] == 0:
            x = x*bw-bouncer
            y = y*bw
        else:
            x *= bw
            y *= bw

        image = pygame.image.load(os.path.join("Assets","Pieces",str(c) + ".png"))
        w.blit(pygame.transform.smoothscale(image,(bw,bw)),(y,x))


def draw_pawn(x,y):
    if Grid[x][y] // 10 > 5:
        if Grid[x][y] % 2 == 0:
            c = 601
        else:
            c = 611
        Mouse_Loc = pygame.mouse.get_pos()
        if Active[x][y] == 1 and x == Mouse_Loc[1] // bw and y == Mouse_Loc[0] // bw:
            pygame.draw.rect(w,(150,186,118),(y * bw,x * bw,bw + 1,bw + 1))
        if Active[x][y] == 0:
            x = x*bw-bouncer
            y = y*bw
        else:
            x *= bw
            y *= bw

        image = pygame.image.load(os.path.join("Assets","Pieces",str(c) + ".png"))
        w.blit(pygame.transform.smoothscale(image,(bw,bw)),(y,x))


def draw_knight(x,y):
    if Grid[x][y] // 10 == 5:
        if Grid[x][y] % 2 == 0:
            c = 501
        else:
            c = 511
        Mouse_Loc = pygame.mouse.get_pos()
        if Active[x][y] == 1 and x == Mouse_Loc[1] // bw and y == Mouse_Loc[0] // bw:
            pygame.draw.rect(w,(150,186,118),(y * bw,x * bw,bw + 1,bw + 1))
        if Active[x][y] == 0:
            x = x*bw-bouncer
            y = y*bw
        else:
            x *= bw
            y *= bw
        image = pygame.image.load(os.path.join("Assets","Pieces",str(c) + ".png"))
        w.blit(pygame.transform.smoothscale(image,(bw,bw)),(y,x))


def draw_bishop(x,y):
    if Grid[x][y] // 10 == 4:
        if Grid[x][y] % 2 == 0:
            c = 401
        else:
            c = 411
        Mouse_Loc = pygame.mouse.get_pos()
        if Active[x][y] == 1 and x == Mouse_Loc[1] // bw and y == Mouse_Loc[0] // bw:
            pygame.draw.rect(w,(150,186,118),(y * bw,x * bw,bw + 1,bw + 1))
        if Active[x][y] == 0:
            x = x*bw-bouncer
            y = y*bw
        else:
            x *= bw
            y *= bw
        image = pygame.image.load(os.path.join("Assets","Pieces",str(c) + ".png"))
        w.blit(pygame.transform.smoothscale(image,(bw,bw)),(y,x))


def draw_queen(x,y):
    if Grid[x][y] // 10 == 2:
        if Grid[x][y] % 2 == 0:
            c = 201
        else:
            c = 211
        Mouse_Loc = pygame.mouse.get_pos()
        if Active[x][y] == 1 and x == Mouse_Loc[1] // bw and y == Mouse_Loc[0] // bw:
            pygame.draw.rect(w,(150,186,118),(y * bw,x * bw,bw + 1,bw + 1))
        if Active[x][y] == 0:
            x = x*bw-bouncer
            y = y*bw
        else:
            x *= bw
            y *= bw
        image = pygame.image.load(os.path.join("Assets","Pieces",str(c) + ".png"))
        w.blit(pygame.transform.smoothscale(image,(bw,bw)),(y,x))


def draw_king(x,y):
    if Grid[x][y] // 10 == 1:
        if Grid[x][y] % 2 == 0:
            c = 101
        else:
            c = 111
        Mouse_Loc = pygame.mouse.get_pos()
        if Active[x][y] == 1 and x == Mouse_Loc[1] // bw and y == Mouse_Loc[0] // bw:
            pygame.draw.rect(w,(150,186,118),(y * bw,x * bw,bw + 1,bw + 1))
        if Active[x][y] == 0:
            x = x*bw-bouncer
            y = y*bw
        else:
            x *= bw
            y *= bw
        image = pygame.image.load(os.path.join("Assets","Pieces",str(c) + ".png"))
        w.blit(pygame.transform.smoothscale(image,(bw,bw)),(y,x))

def printer(n):
    counter = 0
    while counter < (xGrid * yGrid):
        x = counter // xGrid
        y = counter % xGrid
        y2 = (x) % 2 +n
        if (counter % 2 == 0 and y2 % 2 != 0) or (counter % 2 != 0 and y2 % 2 == 0):
            bg=(238, 238, 210)
            pygame.draw.rect(w,bg,(y * bw,x * bw,bw,bw))
        else:
            bg=(118, 150, 86)
            pygame.draw.rect(w,bg,(y * bw,x * bw,bw,bw))
        if Active[x][y]==0:
            pygame.draw.rect(w,(118,150,186),(y * bw,x * bw,bw,bw))

        color=(87, 84, 82)
        draw_rook(x,y)
        draw_pawn(x,y)
        draw_knight(x,y)
        draw_bishop(x,y)
        draw_queen(x,y)
        draw_king(x,y)
        if Active[x][y]==1:
            pygame.draw.circle(w,(118,150,186),(y * bw+bw//2,x * bw+bw//2),bw//5)

        counter += 1

def pawn_moves(Active,x,y):
    if Grid[y][x]%2==0:
        val=-1
    else:
        val=1
    if(Grid[y+val][x]==0):
        Active[y+val][x]=1
        if (Grid[y +2* val][x] == 0)and((val==1 and y==1 )or(val==-1 and y==yGrid-2)):
            Active[y + 2*val][x] = 1
    if x>0 and (Grid[y+val][x-1]%2!=Grid[y][x]%2 and Grid[y+val][x-1]!=0 ):
        Active[y+val][x-1] = 1
    if x<xGrid-1 and  (Grid[y + val][x + 1] % 2 != Grid[y][x] % 2 and Grid[y + val][x + 1] != 0):
        Active[y + val][x + 1] = 1
def rook_moves(Active,x,y):
    e=(Grid[y][x]+1)%2
    x2=x+1
    while(x2<xGrid):
        if(Grid[y][x2]==0):
            Active[y][x2]=1
        elif(Grid[y][x2]%2==e):
            Active[y][x2]=1
        if(Grid[y][x2]!=0):
            break
        x2+=1

    x2=x-1
    while(x2>=0):
        if(Grid[y][x2]==0):
            Active[y][x2]=1
        elif(Grid[y][x2]%2==e):
            Active[y][x2]=1
        if(Grid[y][x2]!=0):
            break
        x2-=1

    y2=y+1
    while(y2<yGrid):
        if(Grid[y2][x]==0):
            Active[y2][x]=1
        elif(Grid[y2][x]%2==e):
            Active[y2][x]=1
        if(Grid[y2][x]!=0):
            break
        y2+=1
    y2=y-1
    while(y2>=0):
        if(Grid[y2][x]==0):
            Active[y2][x]=1
        elif(Grid[y2][x]%2==e):
            Active[y2][x]=1
        if(Grid[y2][x]!=0):
            break
        y2-=1
def bishop_moves(Active,x,y):
    e=(Grid[y][x]+1)%2
    x2=x+1
    y2=y+1
    while(x2<xGrid and y2<yGrid):
        if(Grid[y2][x2]==0):
            Active[y2][x2]=1
        elif(Grid[y2][x2]%2==e):
            Active[y2][x2]=1
        if(Grid[y2][x2]!=0):
            break
        x2+=1
        y2+=1

    x2=x-1
    y2=y-1
    while(x2>=0 and y2>=0):
        if(Grid[y2][x2]==0):
            Active[y2][x2]=1
        elif(Grid[y2][x2]%2==e):
            Active[y2][x2]=1
        if(Grid[y2][x2]!=0):
            break
        x2-=1
        y2-=1

    y2=y+1
    x2=x-1
    while(y2<yGrid and x2>=0):
        if(Grid[y2][x2]==0):
            Active[y2][x2]=1
        elif(Grid[y2][x2]%2==e):
            Active[y2][x2]=1
        if(Grid[y2][x2]!=0):
            break
        y2+=1
        x2-=1
    y2=y-1
    x2=x+1
    while(y2>=0 and x2<xGrid):
        if(Grid[y2][x2]==0):
            Active[y2][x2]=1
        elif(Grid[y2][x2]%2==e):
            Active[y2][x2]=1
        if(Grid[y2][x2]!=0):
            break
        y2-=1
        x2+=1
def knight_moves(Active,x,y):
    e = (Grid[y][x] + 1) % 2
    if(y>1 and x>0)and (Grid[y-2][x-1]==0 or Grid[y-2][x-1]%2==e):
        Active[y-2][x-1]=1
    if (y>1 and x<xGrid-1)and (Grid[y-2][x+1]==0 or Grid[y-2][x+1]%2==e):
        Active[y-2][x+1] = 1
    if (y>0 and x<xGrid-2)and (Grid[y-1][x+2]==0 or Grid[y-1][x+2]%2==e):
        Active[y-1][x+2] = 1
    if (y>0 and x>1)and (Grid[y-1][x-2]==0 or Grid[y-1][x-2]%2==e):
        Active[y-1][x-2] = 1
    if (y<yGrid-2 and x>0)and (Grid[y+2][x-1]==0 or Grid[y+2][x-1]%2==e):
        Active[y+2][x-1] = 1
    if (y<yGrid-2 and x<xGrid-1)and (Grid[y+2][x+1]==0 or Grid[y+2][x+1]%2==e):
        Active[y+2][x+1] = 1
    if (y<yGrid-1 and x<xGrid-2)and (Grid[y+1][x+2]==0 or Grid[y+1][x+2]%2==e):
        Active[y+1][x+2] = 1
    if (y<yGrid-1 and x>1)and (Grid[y+1][x-2]==0 or Grid[y+1][x-2]%2==e):
        Active[y+1][x-2] = 1
def queen_moves(Active,x,y):
    e = (Grid[y][x] + 1) % 2
    x2 = x + 1
    while (x2 < xGrid):
        if (Grid[y][x2] == 0):
            Active[y][x2] = 1
        elif (Grid[y][x2] % 2 == e):
            Active[y][x2] = 1
        if (Grid[y][x2] != 0):
            break
        x2 += 1

    x2 = x - 1
    while (x2 >= 0):
        if (Grid[y][x2] == 0):
            Active[y][x2] = 1
        elif (Grid[y][x2] % 2 == e):
            Active[y][x2] = 1
        if (Grid[y][x2] != 0):
            break
        x2 -= 1

    y2 = y + 1
    while (y2 < yGrid):
        if (Grid[y2][x] == 0):
            Active[y2][x] = 1
        elif (Grid[y2][x] % 2 == e):
            Active[y2][x] = 1
        if (Grid[y2][x] != 0):
            break
        y2 += 1
    y2 = y - 1
    while (y2 >= 0):
        if (Grid[y2][x] == 0):
            Active[y2][x] = 1
        elif (Grid[y2][x] % 2 == e):
            Active[y2][x] = 1
        if (Grid[y2][x] != 0):
            break
        y2 -= 1
    x2 = x + 1
    y2 = y + 1
    while (x2 < xGrid and y2 < yGrid):
        if (Grid[y2][x2] == 0):
            Active[y2][x2] = 1
        elif (Grid[y2][x2] % 2 == e):
            Active[y2][x2] = 1
        if (Grid[y2][x2] != 0):
            break
        x2 += 1
        y2 += 1

    x2 = x - 1
    y2 = y - 1
    while (x2 >= 0 and y2 >= 0):
        if (Grid[y2][x2] == 0):
            Active[y2][x2] = 1
        elif (Grid[y2][x2] % 2 == e):
            Active[y2][x2] = 1
        if (Grid[y2][x2] != 0):
            break
        x2 -= 1
        y2 -= 1

    y2 = y + 1
    x2 = x - 1
    while (y2 < yGrid and x2 >= 0):
        if (Grid[y2][x2] == 0):
            Active[y2][x2] = 1
        elif (Grid[y2][x2] % 2 == e):
            Active[y2][x2] = 1
        if (Grid[y2][x2] != 0):
            break
        y2 += 1
        x2 -= 1
    y2 = y - 1
    x2 = x + 1
    while (y2 >= 0 and x2 < xGrid):
        if (Grid[y2][x2] == 0):
            Active[y2][x2] = 1
        elif (Grid[y2][x2] % 2 == e):
            Active[y2][x2] = 1
        if (Grid[y2][x2] != 0):
            break
        y2 -= 1
        x2 += 1
def king_moves(Active,x,y):
    e=(Grid[y][x]+1)%2
    if x>0 and(Grid[y][x-1]==0 or Grid[y][x-1]%2==e):
        Active[y][x-1]=1
    if x<xGrid-1 and (Grid[y][x+1]==0 or Grid[y][x+1]%2==e):
        Active[y][x+1]=1
    if(x>0):
        x2=x-1
    else:
        x2=x
    while(x2<xGrid and x2<x+2 and y>0):
        if(Grid[y-1][x2]==0):
            Active[y-1][x2]=1
        elif(Grid[y-1][x2]%2==e):
            Active[y-1][x2]=1
        x2+=1
    if(x>0):
        x2=x-1
    else:
        x2=x
    while(x2<xGrid and x2<x+2 and y<yGrid-1):
        if(Grid[y+1][x2]==0):
            Active[y+1][x2]=1
        elif(Grid[y+1][x2]%2==e):
            Active[y+1][x2]=1
        x2+=1
def main():
    run=True
    yM=0
    sw=0
    xM=0
    global bouncer
    moved=0
    turn=0
    while(run):
        clock.tick(60)
        printer(0)
        click=pygame.mouse.get_pressed()
        Mouse_Loc = pygame.mouse.get_pos()
        if 0<Mouse_Loc[0]<width and 0< Mouse_Loc[1]<height:
            yM = Mouse_Loc[1] // bw
            xM = Mouse_Loc[0] // bw % xGrid
        if click[0] and moved!=1:
            if(Selecter[0]!=-1 and Active[yM][xM] ==1):
                Grid[yM][xM] = Grid[Selecter[0]][Selecter[1]]
                Grid[Selecter[0]][Selecter[1]] = 0
                reset()
                sw=0
                p2=1
                bouncer=1
                Selecter[0]=-1
                Selecter[1]=-1
                clock.tick(10)
                turn=(turn+1)%2
            elif Grid[yM][xM]!=0:
                reset()
                sw=0
                p2=1
                bouncer=1
                if(Grid[yM][xM]%2==turn):
                    Selecter[0] = yM
                    Selecter[1] = xM
                    Active[Selecter[0]][Selecter[1]] = 0
                    if (Grid[yM][xM] // 10 > 5):
                        pawn_moves(Active,xM,yM)
                    elif (Grid[yM][xM] // 10 ==3):
                        rook_moves(Active,xM,yM)
                    elif (Grid[yM][xM] // 10 ==4):
                        bishop_moves(Active,xM,yM)
                    elif (Grid[yM][xM] // 10 ==5):
                        knight_moves(Active,xM,yM)
                    elif (Grid[yM][xM] // 10 ==2):
                        queen_moves(Active,xM,yM)
                    elif (Grid[yM][xM] // 10 ==1):
                        king_moves(Active,xM,yM)
        keypress=pygame.key.get_pressed()
        for event in pygame.event.get():
            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = False
        if sw==0:
            bouncer+=1 +(bouncer//16+1)%2
        elif sw==1:
            bouncer-=(1 +(bouncer//16+1)%2)
        if bouncer>=30:
            sw=1
        elif bouncer<=1:
            sw=0

        pygame.display.update()

main()