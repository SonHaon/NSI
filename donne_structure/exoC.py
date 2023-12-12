# def moyenne_1(tableau):
#     somme=0
#     coef=0
#     for i in range(len(tableau[0])):
#         somme+=tableau[0][i]*tableau[1][i]
#         coef+=tableau[1][i]
#     return somme/coef

# def moyenne_2(tableau):
#     somme=0
#     coef=0
#     for i in range(len(tableau)):
#         somme+=tableau[i][0]*tableau[i][1]
#         coef+=tableau[i][1]
#     return somme/coef

# notes1=[[12,14,14.5,16,18,14,11,14],[4,1,3,5,3,2,1,1]]
# notes2=[[12,4],[14,1],[14.5,3],[16,5],[18,3],[14,2],[11,1],[14,1]]
# print(moyenne_2(notes2))
# print(moyenne_1(notes1))
    


# def tableau(n):
#     tabl=[[0 for i in range(n)] for a in range(n)]
#     tabl[4][7]=47
#     for ligne in tabl:
#         for chiffre in ligne:
#             print(chiffre,end=" ")
#         print()

# tableau(10)



def f():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tableau[i][j] = i * j
        print(*tableau[i], sep="\t")
    return tableau

def f1():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i==j:tableau[i][j] = 1 
        print(*tableau[i], sep="\t")
    return tableau

def f2():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i>j:tableau[i][j] = 1 
        print(*tableau[i], sep="\t")
    return tableau

def f3():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i<=j:tableau[i][j] = 1 
        print(*tableau[i], sep="\t")
    return tableau

def f4():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tableau[i][j] = i+j
        print(*tableau[i], sep="\t")
    return tableau

def f5():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tableau[i][j] = (i+1)*(j+1)
        print(*tableau[i], sep="\t")
    return tableau

def f6():
    tableau = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i<j:tableau[i][j] = i
            else:tableau[i][j] = j
        print(*tableau[i], sep="\t")
    return tableau


f6()