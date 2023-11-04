nombre=int(input("un nombre : "))
i=2
premier=True
while i<nombre:
    if nombre%i==0:
        premier=False
    i+=1

if premier:
    print(f"{nombre} est premier")
else:
    print(f"{nombre} est pas premier")