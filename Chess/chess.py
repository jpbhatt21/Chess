import pygame
xGrid =8  # 19
yGrid =8 # 25
bw=100
height = yGrid * bw
width = xGrid * bw
fps=60
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
[0,0,0,0,0,0,0,0]
]
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
    [-1,-1,-1,-1,-1,-1,-1,-1]

]
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
def draw_rook(color,x,y):
    if Grid[x][y] // 10 == 3:
        if Grid[x][y] % 2 == 0:
            color = (255,255,255)
        bx = bw // 10
        y = y * bw + 2 * bx + bx // 2
        x = x * bw + bx
        pygame.draw.rect(w,color,(y,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 2,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 2,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 4,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 4,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y,x + bx,bx * 5,bx))
        pygame.draw.rect(w,(0,0,0),(y,x + bx,bx * 5,bx),bx // 5)
        pygame.draw.rect(w,color,(y + bx,x + bx * 2,bx * 3,bx * 4))
        pygame.draw.rect(w,(0,0,0),(y + bx,x + bx * 2,bx * 3,bx * 4),bx // 5)
        pygame.draw.rect(w,color,(y - bx // 2,x + bx * 6,bx * 6,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y - bx // 2,x + bx * 6,bx * 6,bx * 2),bx // 5)
def draw_pawn(color,x,y):
    if Grid[x][y] // 10 >5:
        if Grid[x][y] % 2 == 0:
            color = (255,255,255)
        bx = bw // 10
        y = y * bw
        x = x * bw + bx
        pygame.draw.circle(w,color,(y+bw//2,x+bx),bx)
        pygame.draw.circle(w,(0,0,0),(y+bw//2,x+bw),bx,bx // 5)
        pygame.draw.rect(w,color,(y+bx ,x + bx * 6,bx * 6,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx ,x + bx * 6,bx * 6,bx * 2),bx // 5)
def draw_knight(color,x,y):
    if Grid[x][y] // 10 ==5:
        if Grid[x][y] % 2 == 0:
            color = (255,255,255)
        bx = bw // 10
        y = y * bw + 2 * bx + bx // 2
        x = x * bw + bx
        pygame.draw.rect(w,color,(y,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 2,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 2,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 4,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 4,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y,x + bx,bx * 5,bx))
        pygame.draw.rect(w,(0,0,0),(y,x + bx,bx * 5,bx),bx // 5)
        pygame.draw.rect(w,color,(y + bx,x + bx * 2,bx * 3,bx * 4))
        pygame.draw.rect(w,(0,0,0),(y + bx,x + bx * 2,bx * 3,bx * 4),bx // 5)
        pygame.draw.rect(w,color,(y - bx // 2,x + bx * 6,bx * 6,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y - bx // 2,x + bx * 6,bx * 6,bx * 2),bx // 5)
def draw_bishop(color,x,y):
    if Grid[x][y] // 10 ==4:
        if Grid[x][y] % 2 == 0:
            color = (255,255,255)
        bx = bw // 10
        y = y * bw + 2 * bx + bx // 2
        x = x * bw + bx
        pygame.draw.rect(w,color,(y,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 2,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 2,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 4,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 4,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y,x + bx,bx * 5,bx))
        pygame.draw.rect(w,(0,0,0),(y,x + bx,bx * 5,bx),bx // 5)
        pygame.draw.rect(w,color,(y + bx,x + bx * 2,bx * 3,bx * 4))
        pygame.draw.rect(w,(0,0,0),(y + bx,x + bx * 2,bx * 3,bx * 4),bx // 5)
        pygame.draw.rect(w,color,(y - bx // 2,x + bx * 6,bx * 6,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y - bx // 2,x + bx * 6,bx * 6,bx * 2),bx // 5)
def draw_queen(color,x,y):
    if Grid[x][y] // 10==2:
        if Grid[x][y] % 2 == 0:
            color = (255,255,255)
        bx = bw // 10
        y = y * bw + 2 * bx + bx // 2
        x = x * bw + bx
        pygame.draw.rect(w,color,(y,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 2,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 2,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 4,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 4,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y,x + bx,bx * 5,bx))
        pygame.draw.rect(w,(0,0,0),(y,x + bx,bx * 5,bx),bx // 5)
        pygame.draw.rect(w,color,(y + bx,x + bx * 2,bx * 3,bx * 4))
        pygame.draw.rect(w,(0,0,0),(y + bx,x + bx * 2,bx * 3,bx * 4),bx // 5)
        pygame.draw.rect(w,color,(y - bx // 2,x + bx * 6,bx * 6,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y - bx // 2,x + bx * 6,bx * 6,bx * 2),bx // 5)
def draw_king(color,x,y):
    if Grid[x][y] // 10==1:
        if Grid[x][y] % 2 == 0:
            color = (255,255,255)
        bx = bw // 10
        y = y * bw + 2 * bx + bx // 2
        x = x * bw + bx
        pygame.draw.rect(w,color,(y,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 2,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 2,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y + bx * 4,x,bx,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y + bx * 4,x,bx,bx * 2),bx // 5)
        pygame.draw.rect(w,color,(y,x + bx,bx * 5,bx))
        pygame.draw.rect(w,(0,0,0),(y,x + bx,bx * 5,bx),bx // 5)
        pygame.draw.rect(w,color,(y + bx,x + bx * 2,bx * 3,bx * 4))
        pygame.draw.rect(w,(0,0,0),(y + bx,x + bx * 2,bx * 3,bx * 4),bx // 5)
        pygame.draw.rect(w,color,(y - bx // 2,x + bx * 6,bx * 6,bx * 2))
        pygame.draw.rect(w,(0,0,0),(y - bx // 2,x + bx * 6,bx * 6,bx * 2),bx // 5)
def printer(n):
    counter = 0
    while counter < (xGrid * yGrid):
        x = counter // xGrid
        y = counter % xGrid
        y2 = (x) % 2 +n
        if (counter % 2 == 0 and y2 % 2 != 0) or (counter % 2 != 0 and y2 % 2 == 0):
            pygame.draw.rect(w,(238, 238, 210),(y * bw,x * bw,bw,bw))
        else:
            pygame.draw.rect(w,(118, 150, 86),(y * bw,x * bw,bw,bw))
        if Active[x][y]==0:
            pygame.draw.rect(w,(118,150,186),(y * bw,x * bw,bw,bw))

        color=(50,50,50)
        draw_rook(color,x,y)
        draw_pawn(color,x,y)
        draw_knight(color,x,y)
        draw_bishop(color,x,y)
        draw_queen(color,x,y)
        draw_king(color,x,y)
        if Active[x][y]==1:
            pygame.draw.circle(w,(118,150,186),(y * bw+bw//2,x * bw+bw//2),bw//5)

        counter += 1

def pawn_space(x,y):
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

def main():
    run=True
    yM=0
    xM=0
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
                Selecter[0]=-1
                Selecter[1]=-1
                clock.tick(10)
                turn=(turn+1)%2
            elif Grid[yM][xM]!=0:
                reset()
                if(Grid[yM][xM]%2==turn):
                    Selecter[0] = yM
                    Selecter[1] = xM
                    Active[Selecter[0]][Selecter[1]] = 0
                    if (Grid[yM][xM] // 10 > 5):
                        pawn_space(xM,yM)










        keypress=pygame.key.get_pressed()
        for event in pygame.event.get():
            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = False

        pygame.display.update()

main()