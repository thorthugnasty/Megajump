from pygame import *
from random import *

display.set_mode((1,1)) #Again we set here to load images
mainBgImg = image.load("pics/background/skybg.png").convert()
sunPic = image.load("pics/background/sun.png").convert_alpha()
moonPic = image.load("pics/background/moon.png").convert_alpha()

def drawBg(screen,height):
    '''Draws the main background, including the sky, clouds, sun and moon'''
    drawMainBg(screen,height)
    drawClouds(screen,clouds,height)
    drawSun(screen,height)
    drawMoon(screen,height)
    
def drawSun(screen,height):
    '''Draws the sun in the sky. The sun constantly moves down as you go up
    in the world'''
    
    sunY = 100+height%(10*(10000-600))//75 #Starts at a y-coord of 100, then moves down as you go up
    center(screen,sunPic,(200,sunY),True)
    
def drawMoon(screen,height):
    '''The moon appears when you get high enough in the sky'''
    
    moonY = -800 + height%(10*(10000-600))//75
    center(screen,moonPic,(200,moonY),True)
    
    
def drawMainBg(screen,height):
    
    '''The background is designed to scroll slowly to cover more space'''
    screen.blit(mainBgImg,(0,(height%((10000-600)*10)/10-10000+600)))

def drawClouds(screen,clouds,height):
    for each in clouds:
        each.drawCloud(screen,height)
def center(screen,pic,coords,blitFlag):
    '''Returns the coords of where to blit the image such that it is
    centered at the given coords and blits the image in the center
    if blitFlag is passed in as True.'''
    coords = coords[0]-pic.get_width()//2,coords[1]-pic.get_height()//2
    if blitFlag:
        screen.blit(pic,coords)
    return coords
        
def screenCoords(x,y,height):
    '''Converts global coordinates to screen, for blitting '''
    return (x,height + 600 - y)

    
class Cloud: #A cloud that scrolls at a random speed, making a layered background
    
    cloud1Img = image.load("pics/background/cloud1.png").convert_alpha()
    cloud2Img = image.load("pics/background/cloud2.png").convert_alpha()
    cloud3Img = image.load("pics/background/cloud3.png").convert_alpha()
    cloudImgs = [cloud1Img,cloud2Img,cloud3Img]
    
    def __init__(self):
        self.x = randint(0,800)
        self.y = randint(0,100000)
        self.speed = random()
        self.pic = choice(self.cloudImgs)
        
    def drawCloud(self,screen,height):
        '''Draws the cloud in a world with a random height to change the scroll speed'''
        center(screen,self.pic,screenCoords(self.x,self.y,height*self.speed),True) #Blits it somewhere on the map
        
clouds = [Cloud() for i in range(100)] #Draws 100 clouds somewhere in the world
