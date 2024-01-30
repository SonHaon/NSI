import matplotlib.pyplot as plt 

x=[1.20,1.19,1.176,1.147,1.11,1.06,0.994,0.926,0.850]
y=[0,0.1176,0.234,0.348,0.459,0.566,0.667,0.758,0.850]
dt=0.15

plt.plot(x,y,"x",markersize=4)
plt.xlabel("x (en m)")
plt.ylabel("y (en m)")
plt.title("Etde de mouvement")
plt.ylim(0,1.5)
plt.xlim(0,1.5)

Vx=[]
Vy=[]
for k in range(1, len(x)-1):
    Vx.append((x[k+1]-x[k-1])/(2*dt))
    Vy.append((y[k+1]-y[k-1])/(2*dt))
for i in range(0,len(x)-2):
    plt.quiver(x[i+1],y[i+1],Vx[i],Vy[i],color="r",scale=1,scale_units="xy")

dVx=[]
dVy=[]
for k in range(1,len(x)-3):
    dVx.append(Vx[k+1]-Vx[k-1])
    dVy.append(Vy[k+1]-Vy[k-1])
for i in range(0,len(x)-4):
    plt.quiver(x[2+i],y[2+i],dVx[i],dVy[i],color="b",scale=1,scale_units="xy")

plt.show()