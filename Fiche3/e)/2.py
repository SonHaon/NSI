def calcul1(a,b) :
    n = 0
    while n < 20 :
        n = a + b
        a = 2*a
        b = 3*b
        n = b*n
        print("a : ",a)
        print("b : ",b)
        print("n : ",n)
    return n


def calcul2(a,b) :
    n = 0
    while n < 20 :
        n = a + b
        a = 2*a
        b = 3*b
        print("a : ",a)
        print("b : ",b)
        print("n : ",n)
    n = b*n
    return n


def calcul3(a,b) :
    n = 0
    while n < 20 :
        n = a + b
        a = 2*a
        print("a : ",a)
        print("b : ",b)
        print("n : ",n)
    b = 3*b
    n = b*n
    return n

print(calcul3(5,1))