from pygame import*

init()
screen = display.set_mode((800,600))
display.set_caption("Mega Jump")
running = True
mainFont = font.Font("Twelve Ton Goldfish.ttf",60)
def center(pic,coords,blitFlag):
    '''Returns the coords of where to blit the image such that it is
    centered at the given coords and blits the image in the center
    if blitFlag is passed in as True.'''
    coords = coords[0]-pic.get_width()//2,coords[1]-pic.get_height()//2
    if blitFlag:
        screen.blit(pic,coords)
    return coords
def drawCredits():
    creditTxt = mainFont.render("Developed by Andrew Li 2013",True,(255,135,0))
    center(creditTxt,(400,230),True)
    
backgroundPic = image.load("pics/titleScreen/background.png").convert()
def background():
    screen.blit(backgroundPic,(0,0))
    
playPic = image.load("pics/titleScreen/playbutton.png").convert_alpha()
def drawButtons():
    center(playPic,(400,350),True)

def buttons(screen,mx,my):
    global running
    playRect = Rect(400-playPic.get_width()//2,350-playPic.get_height()//2,playPic.get_width(),playPic.get_height())    
    if playRect.collidepoint(mx,my) and mb[0] == 1:
        running = False
                         
def drawScene():
    screen.fill((0,0,0))
    background()
    drawButtons()
    drawCredits()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    buttons(screen,mx,my)
    drawScene()
    display.flip()

quit()

import megajump

    
