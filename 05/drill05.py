import turtle

turtle.shape('turtle')
turtle.stamp()

def turtle_move(angle):
    turtle.setheading(angle)
    turtle.forward(50)
    turtle.stamp()
    
def w_move():
    turtle_move(90)
    
def a_move():
   turtle_move(180)
 
def s_move():
   turtle_move(270)
 
def d_move():
   turtle_move(0)

def restart():
    turtle.reset()
 
 
turtle.onkey(w_move,'w')
turtle.onkey(a_move,'a')
turtle.onkey(s_move,'s')
turtle.onkey(d_move,'d')
turtle.onkey(restart,'Escape')
turtle.listen()


