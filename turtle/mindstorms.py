# Use Python's turtle graphics to draw shapes

import turtle

def draw_square(some_turtle):
	for i in range(5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	#create an instance/object of the class Turtle
	# The turtle Brad draws a square
	brad = turtle.Turtle()
	# class Turtle methods
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	
	for i in range(1, 37):
		draw_square(brad)
		brad.right(10)
	
	

	# Create the turtle Angie. Angie draws a circle.

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)



	# Create the turtle Sam. Sam draws a triangle.
	sam = turtle.Turtle()
	sam.shape("square")

	i = 0
	while i < 3:
		sam.backward(60)
		sam.right(120)
		i += 1



	window.exitonclick()

draw_art()
