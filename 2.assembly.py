from cadquery import *
from cadquery.vis import show

r1 = 10
r2 = 20
h1 = 50
h2 = 10

shaft = Workplane().cylinder(h1, r1)
collar = Workplane().cylinder(h2, r2)

assy = (
    Assembly(shaft, loc=Location(Vector(0, 0, 0)), color=Color(1, 0, 0, 1))
    .add(collar, loc=Location(Vector(0, 0, 0)), color=Color(0, 1, 0, 1)) 
)

show(assy)