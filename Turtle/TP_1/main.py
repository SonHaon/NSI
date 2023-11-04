import turtle as tu

def carre(x:int,y:int,c:int)->None:
    """dessine un carré de coté c avec comme point de départ les coordonnées (x,y)"""
    tu.up()
    tu.goto(x,y)
    tu.setheading(0)
    tu.down()
    for i in range(4):
        tu.fd(c)
        tu.rt(90)
    tu.up()
    tu.fd(c)
    

def triangle(x:int,y:int,c:int)->None:
    """dessine un triangle équilatérale de coté c"""
    tu.up()
    tu.goto(x,y)
    tu.setheading(0)
    tu.down()
    for i in range(3):
        tu.fd(c)
        tu.rt(120)
    tu.up()
    tu.fd(c)
    

def frise1():
    tu.pencolor("red")
    for i in range(10):
        carre(i*15,0,10)
    tu.done()

def frise2():
    tu.pencolor("red")
    for i in range(5):
        carre(i*15,0,10)
    tu.done()

def frise3():
    tu.pencolor("red")
    x=0
    c=10
    for i in range(5):
        c+=5
        tu.pencolor("red")
        carre(tu.xcor(),0,c)
        tu.fd(5)
        tu.pencolor("blue")
        triangle(tu.xcor(),0,c)
        tu.fd(5)
    tu.done()


frise3()