import turtle

def draw_name():

	window = turtle.Screen()
	window.bgcolor("blue")

	key = turtle.Turtle()
	key.shape("turtle")
	key.color("white")
	key.speed()

	# Draw the K
	key.penup()
	key.backward(250)
	key.left(90)
	key.pendown()
	
	key.forward(200)
	key.backward(100)
	key.right(45)
	key.forward(150)
	key.backward(150)
	key.right(90)
	key.forward(150)


	# Draw the E
	key.penup()
	key.left(45)
	key.forward(30)
	key.pendown()
	key.left(90)
	key.forward(200)
	key.right(90)
	key.forward(100)
	key.penup()
	key.backward(100)
	key.left(90)
	key.forward(50)

	window.exitonclick()

draw_name()