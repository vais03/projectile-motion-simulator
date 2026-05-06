import numpy as np
import matplotlib.pyplot as plt

#take input of initial veloticy and angle of projection
v0=float(input("Enter initial velocity with which body is thrown, in m/s:"))
angle=float(input("Enter angle of projection in degrees:"))

#convert angle into radians
theta=np.radians(angle)

#take input of time values
time=np.linspace(0,5,100)

#expressions for x and y coordinates of the projectile
x=v0*np.cos(theta)*time
y=v0*np.sin(theta)*time-0.5*9.8*time**2

#plot the tranjectory of the projectile
plt.plot(x,y)
plt.title("Trajectory of a Projectile")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()
