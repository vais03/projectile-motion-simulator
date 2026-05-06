Projectile Motion Simulator

Overview:
This project was aimed to plot the trajectory of a particle projected in a 2-D frame with certain velocity at a certain angle from the ground.

Libraries imported:
Numpy
Matplotplib

Input:
Initial velocity of particle
Angle of projection with respect to base

Process:
Equations of Motion of a body in 2 Dimensions.
x=v*cos(theta)*t
y=v*sin(theta)*t - (0.5*9.8)(t**3)
In the above equations, variables used are:
x -> range/displacement in horizontal direction/x-axis in m
y -> height/displacement in vertical direction/y-axis in m
v- -> initial velocity of projection of the particle in m/s
theta -> angle of projection with respect to x-axis, in degrees or radians
t -> time in s
The constants used:
g -> acceleration due to gravity, in m/s^2, euqal to 9.8 m/s^2

Output:
[Graph](output_graph.png)