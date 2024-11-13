import pygame as pg


pg.init()
dimensions = (750,750)
screen = pg.display.set_mode(dimensions)
clock = pg.time.Clock()
running = True
turn = 0
winner = -1

board = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]]

def drawBoard(dimensions):
    d = dimensions[0]
    size = dimensions[0]/3
    b = 25 #buffer value
    screen.fill("white")
    
    #draw board
    pg.draw.line(screen, "black", (size,b), (size,d-b), 5)
    pg.draw.line(screen, "black", (2*size,b), (2*size,d-b), 5)
    pg.draw.line(screen, "black", (b,size), (d-b,size), 5)
    pg.draw.line(screen, "black", (b,2*size), (d-b,2*size), 5)
    
    #draw plays
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                center = (size*i+125,size*j+125)
                pg.draw.circle(screen, "red", center, 100, 10)
            elif board[i][j] == 1:
                pg.draw.line(screen, "blue", (i*size+b,j*size+b), ((i+1)*size-b,(j+1)*size-b), 10)
                pg.draw.line(screen, "blue", (i*size+b,(j+1)*size-b), ((i+1)*size-b,j*size+b), 10)
    
    checkWin()
        
                
def reset():
    global winner, board, turn
    winner = -1
    turn = 0
    board = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]]
    
def drawWin(player):
    screen.fill("white")
    font = pg.font.Font(None, 80)
    font2 = pg.font.Font(None, 50)
    if winner:
        text = font.render("Player 1 Won!", True, "blue")
    else:
        text = font.render("Player 2 Won!", True, "red")
    
    text2 = font2.render("R to reset", True, "black")
    screen.blit(text, (200,375))
    screen.blit(text2, (275,450))
        
def play():
    global turn
    size = dimensions[0]/3
    pos = pg.mouse.get_pos()
    
    x = int(pos[0]//size)
    y = int(pos[1]//size)
    
    if board[x][y] != -1:
        return
    if turn:
        board[x][y] = 0
        turn = 0
    else:
        board[x][y] = 1
        turn = 1
    

def checkWin():
    global winner
    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=-1):
        winner = 0 if board[0][0]==0 else 1
    if(board[2][0]==board[1][1] and board[2][0]==board[0][2] and board[2][0]!=-1):
        winner = 0 if board[2][0]==0 else 1
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][0]!=-1):
            winner = 0 if board[i][0]==0 else 1
        for j in range(3):
            if(board[0][j]==board[1][j] and board[0][j]==board[2][j] and board[0][j]!=-1):
                winner = 0 if board[0][j]==0 else 1   
    if(winner!=-1):
        drawWin(winner)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        drawBoard(dimensions)
        
        if event.type == pg.MOUSEBUTTONDOWN:
            play()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                reset()
        
    pg.display.flip()
    clock.tick(60)

pg.quit()