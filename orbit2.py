from math import sqrt
from drawtraj import drawtraj
def force(x,y,m,mstar):
    r2=x**2+y**2
    r32=r2*sqrt(r2)
    fx=-x*m*mstar/r32
    fy=-y*m*mstar/r32
    return fx,fy
def integrate(x,y,vx,vy,fx,fy,m,dt):
    ax,ay=fx/m,fy/m
    vx+=ax*dt
    vy+=ay*dt
    x+=vx*dt
    y+=vy*dt
    return x,y,vx,vy
# Main part of the program
mstar=100
m=1.2
nsteps=100000
dt=0.01
r=50
x,y=0,r
vx,vy=0,0
trajx,trajy=[],[]
starx,stary=[],[]
sx,sy,svx,svy=0,0,0,0
for t in range(nsteps):
    fx,fy=force(x,y,m,mstar)
    x,y,vx,vy=integrate(x,y,vx,vy,fx,fy,m,dt)
    sx,sy,svx,svy=integrate(sx,sy,svx,svy,-fx,-fy,mstar,dt)
    trajx.append(x)
    trajy.append(y)
    starx.append(sx)
    stary.append(sy)
drawtraj(trajx,trajy,starx,stary,6*r)