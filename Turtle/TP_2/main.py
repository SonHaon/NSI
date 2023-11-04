import turtle as tu
from math import pi,sqrt
from random import randint

tu.speed(0)
tu.colormode(255)
tu.setup(1000,640)
tu.bgcolor((0,0,0))

def croix():
    tu.goto(0,0)
    tu.down()
    for i in range(4):
        tu.fd(1000)
        tu.bk(1000)
        tu.rt(90)
    tu.up()



def color():
    color=(randint(0,255),randint(0,255),randint(0,255))
    tu.pensize(0.5)
    return color

def carre(x:int,y:int,c:int)->None:
    """dessine un carré de coté c avec comme point de départ les coordonnées (x,y)"""
    tu.up()
    tu.goto(x-c/2,y+c/2)
    tu.setheading(0)
    tu.down()
    for i in range(4):
        tu.fd(c)
        tu.rt(90)
    tu.up()
    tu.goto(x,y)

def carre_full(x,y,cote,color):
    tu.fillcolor(color)
    tu.goto(x,y)
    tu.begin_fill()
    carre(x,y,cote)
    tu.end_fill()
    tu.up()

def carre_imbrique(x,y,cote,nb):
    ecart=cote/10
    for i in range(nb):
        carre_full(x,y,cote,color())
        cote-=ecart

def triangle(x:int,y:int,c:int)->None:
    """dessine un triangle équilatérale de coté c"""
    tu.up()
    tu.goto(x-c/2,y+(sqrt(c**2-(c/2)**2))/2)
    tu.setheading(0)
    tu.down()
    for i in range(3):
        tu.fd(c)
        tu.rt(120)
        print(tu.xcor(),tu.ycor())
    tu.up()
    tu.goto(x,y)

def triangle_full(x,y,cote,color):
    tu.fillcolor(color)
    tu.goto(x,y)
    tu.begin_fill()
    triangle(x,y,cote)
    tu.end_fill()
    tu.up()

def triangle_imbrique(x,y,cote,nb):
    ecart=cote/10
    for i in range(nb):
        triangle_full(x,y+i*2,cote,color())
        cote-=ecart

def cercle(x,y,r):
    tu.goto(x,y-r)
    tu.down()
    tu.circle(r)
    tu.up()

def cercle_full(x,y,r,color):
    tu.up()
    tu.setheading(0)
    tu.goto(x,y)
    tu.fillcolor(color)
    tu.begin_fill()
    cercle(x,y,r)
    tu.end_fill()

def cercle_imbrique(x,y,cote,nb):
    cote/=2
    ecart=cote/10
    for i in range(nb):
        cercle_full(x,y,cote,color())
        cote-=ecart

def hexagone(x:int,y:int,c:int)->None:
    """dessine un carré de coté c avec comme point de départ les coordonnées (x,y)"""
    tu.goto(x-c/2,y+(sqrt(c**2-(c/2)**2)))
    tu.setheading(0)
    tu.down()
    for i in range(7):
        tu.fd(c)
        tu.rt(60)
    tu.up()
    tu.setheading(0)
    tu.goto(x,y)

def hexagone_full(x,y,cote,color):
    tu.up()
    tu.goto(x,y)
    tu.fillcolor(color)
    tu.begin_fill()
    hexagone(x,y,cote)
    tu.end_fill()
    tu.up()

def hexagone_imbrique(x,y,cote,nb):
    cote/=2
    ecart=cote/10
    for i in range(nb):
        hexagone_full(x,y,cote,color())
        cote-=ecart

def ecran_carre(large,haut,cote):
    for y in range(round(large/2)-50,-round(haut/2)+50-1,-100):
        for x in range(-round(large/2)+50,round(haut/2)-50+1,100):
            carre_imbrique(x,y,cote,6)

forme={
    0:carre_imbrique,
    1:triangle_imbrique,
    2:cercle_imbrique,
    3:hexagone_imbrique
}

def ecran_random(large,haut,cote):
    for y in range(round(haut/2)-round(cote/2),-round(haut/2)+round(cote/2)-1,-cote):
        for x in range(-round(large/2)+round(cote/2),round(large/2)-round(cote/2)+1,cote):
            forme[randint(0,3)](x,y,cote-5,6)


croix()

#triangle_imbrique(0,0,100,10)

ecran_random(1270,650,100)

croix()
tu.up()
tu.goto(10000,10000)
tu.done()