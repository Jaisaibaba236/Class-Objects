#creating a class object named rectangle
class rectangle():
  'Finding centre point of Rectangle'

#Creating instances
instance = rectangle()

#Creating attributes
instance.height = 200
instance.width = 100
instance.x = 0
instance.y = 0

def find_center(instance):
   dx = instance.x + (instance.width/2)
   dy = instance.y + (instance.height/2)
   print('Center of rectangle is','(',dx,',',dy,')')
   return dx,dy

instance.x_axis, instance.y_axis = find_center(instance)

position = rectangle()
position.x, position.y = 10,10

def move_rectangle(instance,position):
   new_dx = instance.x_axis + position.x
   new_dy = instance.y_axis + position.y
   print('Relocated center of rectangle is','(',new_dx,',',new_dy,')')

move_rectangle(instance,position)
