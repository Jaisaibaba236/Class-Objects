import turtle

#creating a class object named turtle_work
class turtle_work():
  'Rectangle formation by turtle BOB'
   

#Creating instances
bob = turtle_work()
bob = turtle.Turtle()

#Creating attributes
bob.width = 100
bob.angle = 90
bob.height = 50
bob.x, bob.y = 10,10


def draw_rectangle(bob):
    bob.penup()
    bob.setpos(bob.x,bob.y) 
    bob.pendown()
    for i in range(2):
        bob.fd(bob.width)
        bob.lt(bob.angle)
        bob.fd(bob.height)
        bob.lt(bob.angle)

draw_rectangle(bob)
