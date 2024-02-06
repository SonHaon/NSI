import matplotlib.pyplot as plt

m=15e-3
g=9.81

z = [3.13,2.92,2.72,2.51,2.24,1.90,1.63,1.36,1.22]
t = [0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36]
v = [4.16,4.32,4.47,4.76,5.16,5.54,5.89,6.11,6.22]

Ec = [0.5*m*V**2 for V in v]
Epp = [m*g*Z for Z in z]
Em = []

for i in range(0,len(Epp)):
    Em.append(Ec[1]+Epp[1])

plt.plot(t,Ec, marker="+",label="Ec")
plt.plot(t,Epp, marker="+",label="Epp")
plt.plot(t,Em, marker="+",label="Em")
plt.title("Etude energetique")
plt.xlabel("Temps(s)")
plt.ylabel("Energie(J)")
plt.legend()
plt.grid()
plt.show()