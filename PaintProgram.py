#paintprogram.py
#This program is a graphics editor similar to Microsoft Paint and
#has similar functionality. It allows the user to edit graphics with a variety of tools
#along with the ability to open and save files 
#Created by Anas Saqib
from pygame import*
from random import*
from math import*
screen=display.set_mode((1000,730))
tool="pencil"
stamp=""
Background=image.load("background.jpg")                          #blits all the images for the tools
Colourspectrum=image.load("colourspectrum.jpg")
Pencil=image.load("quill(pencil).jpg")
Eraser=image.load("cloak.jpg")
Paintbrush=image.load("broomstick.jpg")
Spraycan=image.load("potion.jpg")
Fill=image.load("paintbucket.jpg")
Sample=image.load("eyedropper.jpg")

Clear=image.load("wand.jpg")
Rectangle=image.load("Rectangle.jpg")
Circle=image.load("circle.jpg")
Ellipse=image.load("ellipse.jpg")
Line=image.load("line.jpg")
Polygon=image.load("Polygon.jpg")
Sizeup=image.load("sizeup.jpg")
Sizedown=image.load("sizedown.jpg")
Undo=image.load("timeturner.jpg")
Redo=image.load("ressurectionstone.jpg")
Leftarrow=image.load("leftarrow.jpeg")
Rightarrow=image.load("rightarrow.jpeg")
Save=image.load("save.jpeg")
Load=image.load("load.jpeg")

Sorcerersstone1=image.load("sorcerersstone1.jpg")
Sorcerersstone2=image.load("sorcerersstone2.jpg")
Chamberofsecrets1=image.load("chamberofsecrets1.jpg")
Chamberofsecrets2=image.load("chamberofsecrets2.jpg")
Prisonerofazkaban1=image.load("prisonerofazkaban1.jpg")
Prisonerofazkaban2=image.load("prisonerofazkaban2.jpg")
Gobletoffire1=image.load("gobletoffire1.jpg")
Gobletoffire2=image.load("gobletoffire2.jpg")
Orderoftheph1=image.load("orderoftheph1.jpg")
Orderoftheph2=image.load("orderoftheph2.jpg")
Halfbloodprince1=image.load("halfbloodprince1.jpg")
Halfbloodprince2=image.load("halfbloodprince2.jpg")
Deathlyhallows1=image.load("deathlyhallows1.jpg")
Deathlyhallows2=image.load("deathlyhallows2.jpg")
Gryffindor1=image.load("gryffindor1.png")
Gryffindor2=image.load("gryffindor2.png")
Slytherin1=image.load("slytherin1.png")
Slytherin2=image.load("slytherin2.png")
Hufflepuff1=image.load("hufflepuff1.png")
Hufflepuff2=image.load("hufflepuff2.png")
Ravenclaw1=image.load("ravenclaw1.png")
Ravenclaw2=image.load("ravenclaw2.png")
Hogwartsemblem1=image.load("hogwartsemblem1.png")
Hogwartsemblem2=image.load("hogwartsemblem2.png")
Dumbledore1=image.load("dumbledore1.png")
Dumbledore2=image.load("dumbledore2.png")
Voldemort1=image.load("voldemort1.png")
Voldemort2=image.load("voldemort2.png")
Hogwarts1=image.load("hogwarts1.jpg")
Hogwarts2=image.load("hogwarts2.jpg")
Ron1=image.load("ron1.png")
Ron2=image.load("ron2.png")
Hermione1=image.load("hermione1.png")
Hermione2=image.load("hermione2.png")
Sirius1=image.load("sirius1.png")
Sirius2=image.load("sirius2.png")
Hagrid1=image.load("hagrid1.png")
Hagrid2=image.load("hagrid2.png")
Snape1=image.load("snape1.png")
Snape2=image.load("snape2.png")
Mcgonagall1=image.load("mcgonagall1.png")
Mcgonagall2=image.load("mcgonagall2.png")
Ministryofmagic1=image.load("ministryofmagic1.png")
Ministryofmagic2=image.load("ministryofmagic2.png")
Buckbeak1=image.load("buckbeak1.png")
Buckbeak2=image.load("buckbeak2.png")
Harrypotter1=image.load("harrypotter1.png")
Harrypotter2=image.load("harrypotter2.png")
Harry1=image.load("harry1.png")
Harry2=image.load("harry2.png")
Triwizardcup1=image.load("triwizardcup1.png")
Triwizardcup2=image.load("triwizardcup2.png")
Duel1=image.load("duel1.jpg")
Duel2=image.load("duel2.jpg")
Harrypotters1=image.load("harrypotters1.png")
Harrypotters2=image.load("harrypotters2.png")
stampsarea=(175,629,658,105)						#defines the selection area for each tool
canvas=Rect(175,75,658,550)
pencil=Rect(17,75,40,40)
paintbrush=Rect(69,75,40,40)
eraser=Rect(121,75,40,40)
spraycan=Rect(17,135,40,40)
fill=Rect(69,135,40,40)
sample=Rect(121,135,40,40)
clear=Rect(17,195,40,40)
rectangle=Rect(69,195,40,40)
circle=Rect(121,195,40,40)
ellipse=Rect(17,255,40,40)
line=Rect(69,255,40,40)
polygon=Rect(121,255,40,40)
sizeu=Rect(35,310,25,25)
sized=Rect(105,310,25,25)
undo=Rect(35,350,25,25)
redo=Rect(105,350,25,25)
filled=Rect(105,392,25,25)
unfilled=Rect(35,392,25,25)
save=Rect(35,20,40,40)
load=Rect(105,20,40,40)
colours=Rect(840,175,155,180)
colourscr=Rect(940,125,35,35)
sizedis=Rect(860,125,35,35)
descriptionarea=Rect(838,12,162,77)


screen.blit(Background,(0,0))
screen.blit(Colourspectrum,(840,175))
draw.rect(screen,(255,255,255),canvas)
screen.blit(Pencil,(17,75))
screen.blit(Paintbrush,(69,75))
screen.blit(Eraser,(121,75))
screen.blit(Spraycan,(17,135))
screen.blit(Fill,(69,135))
screen.blit(Sample,(121,135))
screen.blit(Clear,(17,195))
screen.blit(Rectangle,(69,195))
screen.blit(Circle,(121,195))
screen.blit(Ellipse,(17,255))
screen.blit(Line,(69,255))
screen.blit(Polygon,(121,255))
screen.blit(Undo,(35,350))
screen.blit(Redo,(105,350))
screen.blit(Sizeup,(35,310))
screen.blit(Sizedown,(105,310))
screen.blit(Leftarrow,(69,654))
screen.blit(Rightarrow,(895,654))
screen.blit(Save,(35,20))
screen.blit(Load,(105,20))


draw.rect(screen,(255,255,255),descriptionarea)
draw.rect(screen,(255,255,255),sizedis)
x1,y1=0,0
x2,y2=0,0
x4,y4=0,0
x3,y3=0,0
c=0
colour=(0,0,0)
size=10
list1=[]
click=False
erctype="unfilled"
toolused=False
toolarea= screen.subsurface(0,0,174,425).copy()
draw.rect(screen,(255,0,0),pencil,1)
curscreen=[]
curscbpos=-2
curscreen.append((screen.subsurface(canvas).copy()))

stamps="first"
rightarrow=Rect(895,654,40,40)
leftarrow=Rect(69,654,40,40)
sorcerersstone1=Rect(200,629,30,30)
chamberofsecrets1=Rect(296,629,30,30)
prisonerofazkaban1=Rect(392,629,30,30)
gobletoffire1=Rect(488,629,30,30)
orderoftheph1=Rect(584,629,30,30)
halfbloodprince1=Rect(680,629,30,30)
deathlyhallows1=Rect(776,629,30,30)
gryffindor1=Rect(200,690,30,30)
slytherin1=Rect(296,690,30,30)
hufflepuff1=Rect(392,690,30,30)
ravenclaw1=Rect(488,690,30,30)
hogwartsemblem1=Rect(584,690,30,30)
dumbledore1=Rect(680,690,30,30)
voldemort1=Rect(776,690,30,30)


screen.blit((Sorcerersstone1),(200,629))
screen.blit((Chamberofsecrets1),(296,629))
screen.blit((Prisonerofazkaban1),(392,629))
screen.blit((Gobletoffire1),(488,629))
screen.blit((Orderoftheph1),(584,629))
screen.blit((Halfbloodprince1),(680,629))
screen.blit((Deathlyhallows1),(776,629))
screen.blit((Gryffindor1),(200,690))
screen.blit((Slytherin1),(296,690))
screen.blit((Hufflepuff1),(392,690))
screen.blit((Ravenclaw1),(488,690))
screen.blit((Hogwartsemblem1),(584,690))
screen.blit((Dumbledore1),(680,690))
screen.blit((Voldemort1),(776,690))

font.init()
timesFont=font.SysFont("Times New Roman",12)                  #description of tools
pentext1=timesFont.render("Quill", 1, (255,0,0))
pentext2=timesFont.render("Acts as a pencil", 1, (255,0,0))
pentext3=timesFont.render("allowing you to draw lines", 1, (255,0,0))
pentext4=timesFont.render("of any colour", 1, (255,0,0))
painttext1=timesFont.render("Broomstick", 1, (255,0,0))
painttext2=timesFont.render("Acts as a paintbrush", 1, (255,0,0))
painttext3=timesFont.render("allowing you to draw thick lines", 1, (255,0,0))
painttext4=timesFont.render("of any colour", 1, (255,0,0))
ertext1=timesFont.render("Cloak of Invisibility", 1, (255,0,0))
ertext2=timesFont.render("Acts as a eraser ", 1, (255,0,0))
ertext3=timesFont.render("allowing you to eraser your work" , 1, (255,0,0))
spraytext1=timesFont.render("Magic Potion ", 1, (255,0,0))
spraytext2=timesFont.render("Allows you to work with ", 1, (255,0,0))
spraytext3=timesFont.render("a spraycan ", 1, (255,0,0))
filltext1=timesFont.render("Paint Bucket ", 1, (255,0,0))
filltext2=timesFont.render("Allows you to fill ", 1, (255,0,0))
filltext3=timesFont.render("an enclosed space ", 1, (255,0,0))
samtext1=timesFont.render("Eyedropper ", 1, (255,0,0))
samtext2=timesFont.render("Gets the colour from ", 1, (255,0,0))
samtext3=timesFont.render("any point on the canvas ", 1, (255,0,0))
clrtext1=timesFont.render("The Elder Wand ", 1, (255,0,0))
clrtext2=timesFont.render("Clears the canvas " , 1, (255,0,0))
rectext1=timesFont.render("Draws unfilled or filled ", 1, (255,0,0))
rectext2=timesFont.render("rectangles ", 1, (255,0,0))
crcltext1=timesFont.render("Draws unfilled or filled ", 1, (255,0,0))
crcltext2=timesFont.render("circles ", 1, (255,0,0))
elltext1=timesFont.render("Draws unfilled or filled ", 1, (255,0,0))
elltext2=timesFont.render("ellipses ", 1, (255,0,0))
linetext1=timesFont.render("Draws straight lines ", 1, (255,0,0))
poltext1=timesFont.render("Draws any-sided polygons ", 1, (255,0,0))
poltext2=timesFont.render("Pressing enter will complete ", 1, (255,0,0))
poltext3=timesFont.render("the polygon ", 1, (255,0,0))
sutext1=timesFont.render("Increases the size of the ", 1, (255,0,0))
sutext2=timesFont.render("paintbrush, eraser or spraycan ", 1, (255,0,0))
sdtext1=timesFont.render("Decreases the size of the ", 1, (255,0,0))
sdtext2=timesFont.render("paintbrush, eraser or spraycan ", 1, (255,0,0))
undotext1=timesFont.render("The Time Turner ", 1, (255,0,0))
undotext2=timesFont.render("Goes back in time and ", 1, (255,0,0))
undotext3=timesFont.render("undoes your last action ", 1, (255,0,0))
redotext1=timesFont.render("The Ressurection Stone ", 1, (255,0,0))
redotext2=timesFont.render("Brings back your last action ", 1, (255,0,0))
stamptext1=timesFont.render("Stamp ", 1, (255,0,0))
sizedtext=timesFont.render(str(size) , 1, (255,0,0))
screen.blit((sizedtext),(871,135))
screen.blit((pentext1),(903,20))
screen.blit((pentext2),(874,45))
screen.blit((pentext3),(854,60))
screen.blit((pentext4),(885,75))
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN and mouse.get_pressed()[0]==1:
            screencopy=screen.copy()
            click=True
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()[0]
    keys = key.get_pressed()
    draw.rect(screen,colour,colourscr)
    if save.collidepoint((mx,my)) and click==True:
        filename=raw_input("What do you want the file name to be?")
        image.save(screen.subsurface(canvas).copy(), filename+".bmp")
    if load.collidepoint((mx,my)) and click==True:
        filename=raw_input("What is the filename of the image that you want to load?")
        loadfile=image.load(filename+".bmp")
        screen.blit((loadfile),(175,75))
    if rightarrow.collidepoint((mx,my)) and click==True:
        stamps="second"
    if leftarrow.collidepoint((mx,my)) and click==True:
         stamps="first"
    if stamps=="first":
        screen.blit((Sorcerersstone1),(200,629))
        screen.blit((Chamberofsecrets1),(296,629))
        screen.blit((Prisonerofazkaban1),(392,629))
        screen.blit((Gobletoffire1),(488,629))
        screen.blit((Orderoftheph1),(584,629))
        screen.blit((Halfbloodprince1),(680,629))
        screen.blit((Deathlyhallows1),(776,629))
        screen.blit((Gryffindor1),(200,690))
        screen.blit((Slytherin1),(296,690))
        screen.blit((Hufflepuff1),(392,690))
        screen.blit((Ravenclaw1),(488,690))
        screen.blit((Hogwartsemblem1),(584,690))
        screen.blit((Dumbledore1),(680,690))
        screen.blit((Voldemort1),(776,690))
    if stamps=="second":
        screen.blit((Hogwarts1),(200,629))
        screen.blit((Ron1),(296,629))
        screen.blit((Hermione1),(392,629))
        screen.blit((Sirius1),(488,629))
        screen.blit((Hagrid1),(584,629))
        screen.blit((Snape1),(680,629))
        screen.blit((Mcgonagall1),(776,629))
        screen.blit((Ministryofmagic1),(200,690))
        screen.blit((Buckbeak1),(296,690))
        screen.blit((Harrypotter1),(392,690))
        screen.blit((Harry1),(488,690))
        screen.blit((Triwizardcup1),(584,690))
        screen.blit((Duel1),(680,690))
        screen.blit((Harrypotters1),(776,690))

	#selection of tools
    if sorcerersstone1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="sorcerersstone"
        if stamps=="second":
            stamp="hogwarts"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if chamberofsecrets1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="chamberofsecrets"
        if stamps=="second":
            stamp="ron"
        
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if prisonerofazkaban1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="prisonerofazkaban"
        if stamps=="second":
            stamp="hermione"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if gobletoffire1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="gobletoffire"
        if stamps=="second":
            stamp="sirius"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if orderoftheph1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="orderoftheph"
        if stamps=="second":
            stamp="hagrid"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if halfbloodprince1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="halfbloodprince"
        if stamps=="second":
            stamp="snape"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if deathlyhallows1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="deathlyhallows"
        if stamps=="second":
            stamp="mcgonagall"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if gryffindor1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="gryffindor"
        if stamps=="second":
            stamp="ministryofmagic"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if slytherin1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="slytherin"
        if stamps=="second":
            stamp="buckbeak"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if hufflepuff1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="hufflepuff"
        if stamps=="second":
            stamp="harrypotter"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if ravenclaw1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="ravenclaw"
        if stamps=="second":
            stamp="harry"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if hogwartsemblem1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="hogwartsemblem"
        if stamps=="second":
            stamp="triwizardcup"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if dumbledore1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="dumbledore"
        if stamps=="second":
            stamp="duel"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    if voldemort1.collidepoint((mx,my)) and click==True:
        if stamps=="first":
            stamp="voldemort"
        if stamps=="second":
            stamp="harrypotters"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((stamptext1),(903,20))
        tool=""
    

    if colours.collidepoint((mx,my)) and click==True:
        colour=screen.get_at((mx,my))
        draw.rect(screen,colour,colourscr)
    if sizeu.collidepoint((mx,my)) and click==True:
        size+=2
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((sutext1),(858,20))
        screen.blit((sutext2),(841,35))
        time.wait(100)
    if sized.collidepoint((mx,my)) and click==True:
        size-=2
        time.wait(100)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((sdtext1),(858,20))
        screen.blit((sdtext2),(841,35))
    if size>45:
        size=45
    if size<5:
        size=5
    sizedtext=timesFont.render(str(size) , 1, (255,0,0))
    draw.rect(screen,(255,255,255),sizedis)
    screen.blit((sizedtext),(871,135))
    if pencil.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="pencil"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(pencil),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((pentext1),(903,20))
        screen.blit((pentext2),(873,45))
        screen.blit((pentext3),(854,60))
        screen.blit((pentext4),(885,75))
    if paintbrush.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="paintbrush"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(paintbrush),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((painttext1),(893,20))
        screen.blit((painttext2),(871,45))
        screen.blit((painttext3),(840,60))
        screen.blit((painttext4),(885,75))
    if eraser.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="eraser"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(eraser),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((ertext1),(870,20))
        screen.blit((ertext2),(877,45))
        screen.blit((ertext3),(838,60))
    if spraycan.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="spraycan"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(spraycan),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((spraytext1),(886,20))
        screen.blit((spraytext2),(865,45))
        screen.blit((spraytext3),(892,60))
    if fill.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="fill"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(fill),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((filltext1),(886,20))
        screen.blit((filltext2),(878,45))
        screen.blit((filltext3),(876,60))
    if sample.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="sample"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(sample),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((samtext1),(892,20))
        screen.blit((samtext2),(870,45))
        screen.blit((samtext3),(865,60))
    if clear.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="clear"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(clear),1)
        draw.rect(screen,(255,255,255),canvas)
        curscreen.append((screen.subsurface(canvas).copy()))
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((clrtext1),(882,20))
        screen.blit((clrtext2),(878,45))
    if rectangle.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="rectangle"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(rectangle),1)
        draw.rect(screen,(255,255,255),filled)
        draw.rect(screen,(255,255,255),unfilled)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((rectext1),(864,20))
        screen.blit((rectext2),(895,35))
    if ellipse.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="ellipse"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(ellipse),1)
        draw.rect(screen,(255,255,255),filled)
        draw.rect(screen,(255,255,255),unfilled)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((elltext1),(864,20))
        screen.blit((elltext2),(901,35))
    if line.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="line"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(line),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((linetext1),(868,20))
    if polygon.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="polygon"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(polygon),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((poltext1),(858,20))
        screen.blit((poltext2),(851,45))
        screen.blit((poltext3),(894,60))
    if circle.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="circle"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(circle),1)
        draw.rect(screen,(255,255,255),filled)
        draw.rect(screen,(255,255,255),unfilled)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((crcltext1),(864,20))
        screen.blit((crcltext2),(902,35))
    if undo.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="undo"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(undo),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((undotext1),(882,20))
        screen.blit((undotext2),(868,45))
        screen.blit((undotext3),(867,60))
    if redo.collidepoint((mx,my)) and click==True:
        stamp=""
        tool="redo"
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(redo),1)
        draw.rect(screen,(255,255,255),descriptionarea)
        screen.blit((redotext1),(862,20))
        screen.blit((redotext2),(850,45))
    if canvas.collidepoint((mx,my)) and tool=="fill" and mb==1:        
        mx,my=mouse.get_pos()
        v,b=mx,my
        col=screen.get_at((v,b))
        if col!=colour and canvas.collidepoint((v,b)):    
            list1.append((v,b))
            while len(list1)!=0:
                for i in list1:
                    qw=list(i)
                    x5=qw[0]
                    y5=qw[1]
                    if screen.get_at((x5-1,y5))==col:
                        screen.set_at((x5-1,y5),colour)
                        list1.append((x5-1,y5))
                    if screen.get_at((x5+1,y5))==col:
                        screen.set_at((x5+1,y5),colour)
                        list1.append((x5+1,y5))
                    if screen.get_at((x5,y5-1))==col:
                        screen.set_at((x5,y5-1),colour)
                        list1.append((x5,y5-1))
                    if screen.get_at((x5,y5+1))==col:
                        screen.set_at((x5,y5+1),colour)
                        list1.append((x5,y5+1))
                    list1=list1[1:]
                toolused=True
                stamp=""
                display.flip()
    if mb==0:
        list1=[]
        x5=0
        y5=0
        qw=0
    
    if tool=="rectangle" or tool=="ellipse" or tool=="circle":
        if filled.collidepoint((mx,my)) and click==True:
            erctype="filled"
    if tool=="rectangle" or tool=="ellipse" or tool=="circle":
        if unfilled.collidepoint((mx,my)) and click==True:
            erctype="unfilled"
    if canvas.collidepoint((mx,my)) and mb==1:        
        screen.set_clip(canvas)
        if stamp=="sorcerersstone":
            screen.blit((screencopy),(0,0))
            screen.blit((Sorcerersstone2),(mx,my))
            toolused=True
        if stamp=="chamberofsecrets":
            screen.blit((screencopy),(0,0))
            screen.blit((Chamberofsecrets2),(mx,my))
            toolused=True
        if stamp=="prisonerofazkaban":
            screen.blit((screencopy),(0,0))
            screen.blit((Prisonerofazkaban2),(mx,my))
            toolused=True
        if stamp=="gobletoffire":
            screen.blit((screencopy),(0,0))
            screen.blit((Gobletoffire2),(mx,my))
            toolused=True
        if stamp=="orderoftheph":
            screen.blit((screencopy),(0,0))
            screen.blit((Orderoftheph2),(mx,my))
            toolused=True
        if stamp=="halfbloodprince":
            screen.blit((screencopy),(0,0))
            screen.blit((Halfbloodprince2),(mx,my))
            toolused=True
        if stamp=="deathlyhallows":
            screen.blit((screencopy),(0,0))
            screen.blit((Deathlyhallows2),(mx,my))
            toolused=True
        if stamp=="gryffindor":
            screen.blit((screencopy),(0,0))
            screen.blit((Gryffindor2),(mx,my))
            toolused=True
        if stamp=="slytherin":
            screen.blit((screencopy),(0,0))
            screen.blit((Slytherin2),(mx,my))
            toolused=True
        if stamp=="hufflepuff":
            screen.blit((screencopy),(0,0))
            screen.blit((Hufflepuff2),(mx,my))
            toolused=True
        if stamp=="ravenclaw":
            screen.blit((screencopy),(0,0))
            screen.blit((Ravenclaw2),(mx,my))
            toolused=True
        if stamp=="hogwartsemblem":
            screen.blit((screencopy),(0,0))
            screen.blit((Hogwartsemblem2),(mx,my))
            toolused=True
        if stamp=="dumbledore":
            screen.blit((screencopy),(0,0))
            screen.blit((Dumbledore2),(mx,my))
            toolused=True
        if stamp=="voldemort":
            screen.blit((screencopy),(0,0))
            screen.blit((Voldemort2),(mx,my))
            toolused=True
        if stamp=="hogwarts":
            screen.blit((screencopy),(0,0))
            screen.blit((Hogwarts2),(mx,my))
            toolused=True
        if stamp=="ron":
            screen.blit((screencopy),(0,0))
            screen.blit((Ron2),(mx,my))
            toolused=True
        if stamp=="hermione":
            screen.blit((screencopy),(0,0))
            screen.blit((Hermione2),(mx,my))
            toolused=True
        if stamp=="sirius":
            screen.blit((screencopy),(0,0))
            screen.blit((Sirius2),(mx,my))
            toolused=True
        if stamp=="hagrid":
            screen.blit((screencopy),(0,0))
            screen.blit((Hagrid2),(mx,my))
            toolused=True
        if stamp=="snape":
            screen.blit((screencopy),(0,0))
            screen.blit((Snape2),(mx,my))
            toolused=True
        if stamp=="mcgonagall":
            screen.blit((screencopy),(0,0))
            screen.blit((Mcgonagall2),(mx,my))
            toolused=True
        if stamp=="ministryofmagic":
            screen.blit((screencopy),(0,0))
            screen.blit((Ministryofmagic2),(mx,my))
            toolused=True
        if stamp=="buckbeak":
            screen.blit((screencopy),(0,0))
            screen.blit((Buckbeak2),(mx,my))
            toolused=True
        if stamp=="harrypotter":
            screen.blit((screencopy),(0,0))
            screen.blit((Harrypotter2),(mx,my))
            toolused=True
        if stamp=="harry":
            screen.blit((screencopy),(0,0))
            screen.blit((Harry2),(mx,my))
            toolused=True
        if stamp=="triwizardcup":
            screen.blit((screencopy),(0,0))
            screen.blit((Triwizardcup2),(mx,my))
            toolused=True
        if stamp=="duel":
            screen.blit((screencopy),(0,0))
            screen.blit((Duel2),(mx,my))
            toolused=True
        if stamp=="harrypotters":
            screen.blit((screencopy),(0,0))
            screen.blit((Harrypotters2),(mx,my))
            toolused=True
        
		#functionality of tools
        if tool=="pencil": 
            draw.line(screen,colour,(x,y),(mx,my),2)
            toolused=True
            stamp=""
        if tool=="eraser":
            J=mx-x
            K=my-y
            L=(J**2+K**2)**0.5
            if L==0:
                L=1
            l=1
            j=(l/L)*J
            k=(l/L)*K
            for i in range(L):
                draw.circle(screen,(255,255,255),(x,y),size)
                x+=j
                y+=k
            toolused=True
            stamp=""
        if tool=="paintbrush":
            J=mx-x
            K=my-y
            L=(J**2+K**2)**0.5
            if L==0:
                L=1
            l=1
            j=(l/L)*J
            k=(l/L)*K
            for i in range(L):
                draw.circle(screen,colour,(x,y),size)
                x+=j
                y+=k
            toolused=True
            stamp=""
        if tool=="spraycan":
            for i in range((size/4)):
                centrex=randint(mx-(size/2),mx+(size/2))
                centrey=randint(my-(size/2),my+(size/2))
                dist=(((mx-centrex)**2)+((my-centrey)**2))**0.5
                if dist<((size/2)+1):
                    draw.circle(screen,colour,(centrex,centrey),0)
            toolused=True
            stamp=""
        if tool=="line":
            screen.blit(screencopy,(0,0))
            if a==0:
                x1,y1=mouse.get_pos()
            draw.line(screen,colour,(x1,y1),(mx,my),3)
            a+=1
            toolused=True
            stamp=""
        if tool=="rectangle":
            if erctype=="unfilled":
                screen.blit(screencopy,(0,0))
                if a==0:
                    x1,y1=mouse.get_pos()
                draw.rect(screen,colour,(min(mx,x1),min(my,y1),abs(x1-mx),abs(y1-my)),2)
                
                a=1
            
            if erctype=="filled":
                screen.blit(screencopy,(0,0))
                if a==0:
                    x1,y1=mouse.get_pos()
                draw.rect(screen,colour,(min(mx,x1),min(my,y1),abs(x1-mx),abs(y1-my)))
                
                a=1
            toolused=True
            stamp=""
        if tool=="ellipse":
            if erctype=="unfilled":
                screen.blit(screencopy,(0,0))
                if a==0:
                    x1,y1=mouse.get_pos()
                try:
                    draw.ellipse(screen,colour,(min(mx,x1),min(my,y1),abs(x1-mx),abs(y1-my)),1)
                except ValueError:
                    pass
                
                a=1
            elif erctype=="filled":
                screen.blit(screencopy,(0,0))
                if a==0:
                    x1,y1=mouse.get_pos()
                draw.ellipse(screen,colour,(min(mx,x1),min(my,y1),abs(x1-mx),abs(y1-my)))
                
                a=1
            
            toolused=True
            stamp=""
        if tool=="sample":
            colour=screen.get_at((mx,my))
            
        elif tool=="polygon":
            if c==0:
                x2,y2=mx,my
                x3,y3=mx,my
                x4,y4=mx,my
                c=1
            else:
                screen.blit(screencopy,(0,0))
                draw.line(screen,colour,(x3,y3),(mx,my),2)
                x4,y4=mx,my
            toolused=True
            stamp=""
        if tool=="circle":
            if erctype=="unfilled":
                screen.blit(screencopy,(0,0))
                if a==0:
                    x1,y1=mouse.get_pos()

                radius=(((mx-x1)**2)+((my-y1)**2))**0.5
                try:    
                    draw.circle(screen,colour,(x1,y1),radius,1)
                except ValueError:
                    pass
                a=1
            
            elif erctype=="filled":
                screen.blit(screencopy,(0,0))
                if a==0:
                    x1,y1=mouse.get_pos()

                radius=(((mx-x1)**2)+((my-y1)**2))**0.5
                draw.circle(screen,colour,(x1,y1),radius)
                a=1
            
            toolused=True
            stamp=""
        screen.set_clip()
        
    if tool=="polygon" and mb!=1:
        x3,y3=x4,y4
        if keys[K_RETURN]==1:
            draw.line(screen,colour,(x3,y3),(x2,y2),2)
            c=0   
    if tool!="polygon":
        c=0
        
    if tool!="ellipse" and tool!="rectangle" and tool!="circle":               

        erctype="unfilled"
    if mb==0:
        a=0    
    if mb==0 and toolused==True:
        curscreen.append((screen.subsurface(canvas).copy()))
        toolused=False  
    
    x=mx
    y=my
    if redo.collidepoint((mx,my)) and click==True and len(curscreen)>=1:
        screen.blit((toolarea),(0,0))
        draw.rect(screen,(255,0,0),(redo),1)
        if curscbpos==-2:
            curscbpos=-3
        screen.blit((curscreen[curscbpos+2]),(175,75))
        curscbpos+=1
    
    if undo.collidepoint((mx,my)) and click==True and len(curscreen)>=curscbpos-(2*curscbpos):
        
        screen.blit((curscreen[curscbpos]),(175,75))
        curscbpos-=1
    
    if tool!="undo" and tool!="redo":
        curscbpos=-2
   
        
    
    click=False
    display.flip()


quit()




