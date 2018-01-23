import math

#creating a class object
class point():
    print('FirstCode')

#creating an instances of 'point' class
inst = point()

#Assigning an attributes
inst.x,inst.y = 15,10

def distance_between_points(inst):
    return math.sqrt(inst.x**2+inst.y**2)

print(distance_between_points(inst))
