#creating a class object named point
class point():
    print('FirstCode')

#creating a class object named rectangle
class rectangle():
  'Finding centre point of Rectangle'

#Creating instances
direct_instance = rectangle()
corner = point()

#Creating attributes
direct_instance.height = 200
direct_instance.width = 100
corner.x = 0
corner.y = 0

def find_center(direct_instance,corner):
   dx = corner.x + (direct_instance.width/2)
   dy = corner.y + (direct_instance.height/2)
   print('Center of rectangle is','(',dx,',',dy,')')

find_center(direct_instance,corner)
