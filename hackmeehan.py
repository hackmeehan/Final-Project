from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, TextAsset
from math import sqrt

print('To start, click the mouse.')
print('Then use the space bar to make a stroke, using the mouse to aim.')

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
    floor6 = RectangleAsset(620, 75, greenline, darkgreen)
    Sprite(floor6, (300, 380))
    floor7 = RectangleAsset(200, 300, greenline, darkgreen)
    Sprite(floor7, (722, 80))
    floorpatch3 = PolygonAsset([(0, 0), (90, 0), (90, 70), (0, 70)], treegreenline, treegreen)
    Sprite(floorpatch3, (860, 58)) 
    floor9 = RectangleAsset(220, 90, greenline, darkgreen)
    Sprite(floor9, (90, 110))
    
    startlineblue = RectangleAsset(100, 2, blueline, blue)
    Sprite(startlineblue, (80, 380))
    
    wall1 = RectangleAsset(10, 300, thinline, brown)
    wall1sprite = Sprite(wall1, (80, 100))
    wall4 = RectangleAsset(120, 10, thinline, brown)
    wall4sprite = Sprite(wall4, (170, 200))
    wall2 = RectangleAsset(10, 200, thinline, brown)
    wall2sprite = Sprite(wall2, (170, 200))
    wall5 = RectangleAsset(310, 12, thinline, brown)
    wall5sprite = Sprite(wall5, (80, 100))
    wall6 = RectangleAsset(10, 300, thinline, brown)
    wall6sprite = Sprite(wall6, (390, 100))
    wall7 = RectangleAsset(10, 300, thinline, brown)
    wall7sprite = Sprite(wall7, (290, 150))
    wall11 = RectangleAsset(325, 10, thinline, brown)
    wall11sprite =  Sprite(wall11, (400, 370))
    wall12 = RectangleAsset(10, 300, thinline, brown)
    wall12sprite = Sprite(wall12, (715, 80))
    wall13 = RectangleAsset(625, 10, thinline, brown)
    wall13sprite = Sprite(wall13, (290, 450))
    wall14 = RectangleAsset(10, 330, thinline, brown)
    wall14sprite = Sprite(wall14, (915, 130))
    wall15 = RectangleAsset(70, 10, thinline, brown)
    wall15sprite = Sprite(wall15, (855, 120))
    wall16 = RectangleAsset(10, 60, thinline, brown)
    wall16sprite = Sprite(wall16, (855, 70))
    wall17 = RectangleAsset(140, 10, thinline, brown)
    wall17sprite = Sprite(wall17, (715, 70))
    
    water = EllipseAsset(40, 80, waterline, watercolor)
    watersprite = Sprite(water, (810, 270))
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
        self.vy = 0
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
            xcoorballhole = self.x
            ycoorballhole = self.y
            vectorxhole = xcoorballhole-805
            vectoryhole = ycoorballhole-110
            unitvectorxhole = vectorxhole/(sqrt((vectoryhole**2)+(vectorxhole**2)))
            unitvectoryhole = vectoryhole/(sqrt((vectoryhole**2)+(vectorxhole**2)))
            self.x = self.x + (-.5*unitvectorxhole)
            self.y = self.y + (-.5*unitvectoryhole)
            self.vx = 0
            self.vy = 0
            scoreboard = TextAsset("Score: "+str(len(scorecounter)), style="bold 15pt Arial", width=250)
            Sprite(scoreboard, (760, 82))
        collidinglistwater = self.collidingWith(watersprite)
        if collidinglistwater:
            self.vy *= 0.9
            self.vx *= 0.9
            self.y += self.vy
            self.x += self.vx
            if sqrt((self.vy**2)+(self.vx**2)) < 1.5:
                self.vy = 0
                self.vx = 0
                
        collidinglistwall1 = self.collidingWith(wall1sprite)
        if collidinglistwall1:
            self.vx = self.vx*-1
        collidinglistwall2 = self.collidingWith(wall2sprite)
        if collidinglistwall2:
            self.vx = self.vx*-1
        collidinglistwall4 = self.collidingWith(wall4sprite)
        if collidinglistwall4:
            self.vy = self.vy*-1
        collidinglistwall5 = self.collidingWith(wall5sprite)
        if collidinglistwall5:
            self.vy = self.vy*-1
        collidinglistwall6 = self.collidingWith(wall6sprite)
        if collidinglistwall6:
            self.vx = self.vx*-1
        collidinglistwall7 = self.collidingWith(wall7sprite)
        if collidinglistwall7:
            self.vx = self.vx*-1  
        collidinglistwall11 = self.collidingWith(wall11sprite)
        if collidinglistwall11:
            self.vy = self.vy*-1
        collidinglistwall12 = self.collidingWith(wall12sprite)
        if collidinglistwall12:
            self.vx = self.vx*-1
        collidinglistwall13 = self.collidingWith(wall13sprite)
        if collidinglistwall13:
            self.vy = self.vy*-1
        collidinglistwall14 = self.collidingWith(wall14sprite)
        if collidinglistwall14:
            self.vx = self.vx*-1
        collidinglistwall15 = self.collidingWith(wall15sprite)
        if collidinglistwall15:
            self.vy = self.vy*-1
        collidinglistwall16 = self.collidingWith(wall16sprite)
        if collidinglistwall16:
            self.vx = self.vx*-1
        collidinglistwall17 = self.collidingWith(wall17sprite)
        if collidinglistwall17:
            self.vy = self.vy*-1

    def spaceKey(self, event):
        global i
        global j
        xcoorball = self.x
        ycoorball = self.y
        vectorx = i-xcoorball
        vectory = j-ycoorball
        unitvectorx = vectorx/(sqrt((vectory**2)+(vectorx**2)))
        unitvectory = vectory/(sqrt((vectory**2)+(vectorx**2)))
        scorecounter.append('stroke')
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
    golfball = ball(white, 5, 125, 387)

myapp = minigolf()
myapp.listenMouseEvent('click', mouseClick)
myapp.listenMouseEvent('mousemove', mouseMove)
myapp.run()