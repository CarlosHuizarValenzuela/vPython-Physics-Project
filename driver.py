from visual import *
from math import sin,cos,sqrt

initialHeight = vector(0, 4.6, 0)
initialVelocity = 25
Angle = 60
energy = 1
bounce = 0


# this sets up our display window
scene = display(title = "Projectile Motion",
                x = 0, y = 0, width = 800, height = 600,
                range = 10, background = color.white,
                center = (10, initialHeight.y, 0))
table = box(pos=(-1,initialHeight.y - 1,0), size =(5,1,4),
                color=color.orange,material=materials.wood)

# table legs
frontright = box(pos=(1,initialHeight.y - 3.5,1.5),
               size =(.5,4,.5),
               color=color.orange,
               material=materials.wood)
frontleft = box(pos=(1,initialHeight.y - 3.5,-1.5),
               size =(.5,4,.5),
               color=color.orange,
               material=materials.wood)
backright = box(pos=(-3,initialHeight.y - 3.5,1.5),
               size =(.5,4,.5),
               color=color.orange,
               material=materials.wood)
backleft = box(pos=(-3,initialHeight.y - 3.5,-1.5),
               size =(.5,4,.5),
               color=color.orange,
               material=materials.wood)


# ball will travel using vectors
ball = sphere (pos = (0,initialHeight.y, 0) , radius = 1,
               color = color.green,
               material=materials.silver,
               make_trail = true)


floor = box(pos=(0,-1.11,0), size = (125,0.25,125),
             color=color.red,material=materials.wood)

#times
t = 0
dt = 0.001  #time increment
g = -32     #-32ft/s**2 = -9.8 m/s**2

Fgrav = vector(0,g*dt, 0) #3D Vector for the Force of Gravity

#velocity vector for ball:
ballv = vector(initialVelocity * cos(Angle*pi/ 180),
                initialVelocity * sin(Angle*pi/180),0)
#Putting the balls into motion

#Vector ball
while bounce < 15:
    rate(300)
    ballv = ballv + Fgrav

    #incrementing the positon everytime
    ball.pos += ballv * dt
        
    

    if ball.y < 0:
        ballv = vector(initialVelocity * energy * cos(Angle*pi/ 180),
                initialVelocity * energy * sin(Angle*pi/180),0)
        energy -= energy * .2
        bounce += 1

    t += dt
       
