from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sqrt

print('To start, click the mouse.')
print('Then use the space bar to make a stroke.')

for i in range(1):
    treegreen = Color(0x458B00, 1.0)
    green = Color(0x00ff00, 1.0)
    blue = Color(0x0000CD, 1.0)
    black = Color(0x000000, 1.0)
    slategrey = Color(0x8B8878, 1.0)
    white = Color(0xffffff, 1.0)
    brown = Color(0xCD661D, 1.0)
    khaki = Color(0xF0E68C, 1.0)
    darkgreen = Color(0x006400, 1.0)
    watercolor = Color(0x1874CD, 1.0)
    thinline = LineStyle(2, black)
    brownline = LineStyle(2, brown)
    blueline = LineStyle(2, blue)
    greenline = LineStyle(2, darkgreen)
    waterline = LineStyle(2, watercolor)
    treegreenline = LineStyle(2, treegreen)
    
    background = RectangleAsset(1200, 1000, thinline, treegreen)
    Sprite(background, (0, 0))
    
    floor1 = RectangleAsset(100, 200, greenline, darkgreen)
    Sprite(floor1, (80, 200))
    floor2 = PolygonAsset([(60, 200), (180, 100), (370, 100), (137, 200)], greenline, darkgreen)
    Sprite(floor2, (90, 100)) 
    floor3 = RectangleAsset(95, 346, greenline, darkgreen)
    Sprite(floor3, (300, 100))
    floorpatch = RectangleAsset(10, 10, greenline, darkgreen)
    Sprite(floorpatch, (290, 140))
    floor4 = EllipseAsset(80, 40, greenline, darkgreen)
    Sprite(floor4, (50, 360))
    floor5 = PolygonAsset([(0, 0), (150, 0), (240, 53), (164, 85)], greenline, darkgreen)
    Sprite(floor5, (298, 445)) 
    floorpatch2 = PolygonAsset([(0, 0), (98, 70), (0, 70)], greenline, darkgreen)
    Sprite(floorpatch2, (388, 400)) 
    floor6 = RectangleAsset(250, 68, greenline, darkgreen)
    Sprite(floor6, (670, 380))
    floor7 = RectangleAsset(200, 300, greenline, darkgreen)
    Sprite(floor7, (722, 80))
    floorpatch3 = PolygonAsset([(0, 0), (90, 0), (90, 70)], treegreenline, treegreen)
    Sprite(floorpatch3, (840, 70)) 
    floor8 = PolygonAsset([(0, 80), (200, 0), (200, 70), (0, 145)], greenline, darkgreen)
    Sprite(floor8, (470, 380)) 
    
    startlineblue = RectangleAsset(100, 2, blueline, blue)
    Sprite(startlineblue, (80, 380))
    
    wall1 = RectangleAsset(10, 200, thinline, brown)
    Sprite(wall1, (80, 200))
    wall2 = RectangleAsset(10, 200, thinline, brown)
    Sprite(wall2, (170, 200))
    wall3 = PolygonAsset([(60, 200), (180, 100), (190, 100), (70, 200)], thinline, brown)
    Sprite(wall3, (78, 100))
    wall4 = PolygonAsset([(60, 200), (180, 150), (190, 150), (70, 200)], thinline, brown)
    Sprite(wall4, (168, 150))
    wall5 = RectangleAsset(200, 12, thinline, brown)
    Sprite(wall5, (192, 100))
    wall6 = RectangleAsset(10, 300, thinline, brown)
    Sprite(wall6, (390, 100))
    wall7 = RectangleAsset(10, 300, thinline, brown)
    Sprite(wall7, (290, 150))
    wall8 = PolygonAsset([(0, 0), (10, 0), (180, 80), (170, 80)], thinline, brown)
    Sprite(wall8, (288, 448))
    wall8 = PolygonAsset([(360, 0), (380, 0), (180, 80), (160, 80)], thinline, brown)
    Sprite(wall8, (460, 449))
    wall9 = PolygonAsset([(0, 0), (10, 0), (90, 60), (80, 60)], thinline, brown)
    Sprite(wall9, (388, 397))
    wall10 = PolygonAsset([(360, 0), (380, 0), (180, 80), (160, 80)], thinline, brown)
    Sprite(wall10, (468, 377))
    wall11 = RectangleAsset(50, 10, thinline, brown)
    Sprite(wall11, (665, 370))
    wall12 = RectangleAsset(10, 300, thinline, brown)
    Sprite(wall12, (715, 80))
    wall13 = RectangleAsset(250, 6, thinline, brown)
    Sprite(wall13, (665, 450))
    wall14 = RectangleAsset(10, 325, thinline, brown)
    Sprite(wall14, (915, 130))
    wall15 = PolygonAsset([(0, 0), (10, 0), (90, 60), (80, 60)], thinline, brown)
    Sprite(wall15, (835, 70))
    wall16 = RectangleAsset(140, 10, thinline, brown)
    Sprite(wall16, (715, 70))
    
    water = EllipseAsset(70, 120, waterline, watercolor)
    watersprite = Sprite(water, (750, 160))
    hole = CircleAsset(10, thinline, black)
    holesprite = Sprite(hole, (800, 105))

scorecounter = []

golfball = None

class minigolf(App):
    
    def step(self):
        if golfball:
            golfball.step()

class ball(Sprite):
    def __init__(self, color, diameter, x, y):
        global myapp
        self.c = color
        self.d = diameter
        self.vy = -3.7
        self.vx = 0
        theball = CircleAsset(self.d, thinline, self.c)
        myapp.listenKeyEvent('keydown', 'space', self.spaceKey)
        super().__init__(theball, (x, y))
    def step(self):
        self.vy *= 0.99
        self.vx *= 0.99
        self.y += self.vy
        self.x += self.vx
        if sqrt((self.vy**2)+(self.vx**2)) < 1:
            self.vy = 0
            self.vx = 0
        collidinglisthole = self.collidingWith(holesprite)
        if collidinglisthole:
            self.vx = 0
            self.vy = 0
            global scorecounter
            print('Score: '+(len(scorecounter)+1))
        collidinglistwater = self.collidingWith(watersprite)
        if collidinglistwater:
            self.vy *= 0.9
            self.vx *= 0.9
            self.y += self.vy
            self.x += self.vx
            if sqrt((self.vy**2)+(self.vx**2)) < 1:
                self.vy = 0
                self.vx = 0
    def spaceKey(self, event):
        global i
        global j
        #i = event.x
        #j = event.y
        xcoorball = self.x
        ycoorball = self.y
        vectorx = i-xcoorball
        vectory = j-ycoorball
        unitvectorx = vectorx/(sqrt((vectory**2)+(vectorx**2)))
        unitvectory = vectory/(sqrt((vectory**2)+(vectorx**2)))
        scorecounter.append('point')
        if self.vx == 0 and self.vy == 0: 
            self.vx = 5*(unitvectorx)
            self.vy = 5*(unitvectory)
    


        
    
def mouseMove(event):
    global i 
    global j
    i = event.x
    j = event.y
def mouseClick(event):
    global i
    global j
    global golfball
    i = event.x
    j = event.y
    golfball = ball(white, 5, 130, 400)


myapp = minigolf()
myapp.listenMouseEvent('click', mouseClick)
myapp.listenMouseEvent('mousemove', mouseMove)
myapp.run()
