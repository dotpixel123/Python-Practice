
import turtle 
import math 
import random

# turtle.speed(10)
# # Constructing a coloured square using 'for' loop
# turtle.color('magenta','purple')
# turtle.begin_fill()
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.end_fill()

# # Constructing a arrow
# turtle.color('red') 
# turtle.forward(100)
# turtle.left(135)
# turtle.forward(14.14)
# turtle.left(135)
# turtle.penup()
# turtle.forward(20)
# turtle.pendown()
# turtle.left(135)
# turtle.forward(14.14)
# turtle.hideturtle()

# # Making a flower
# for i in range(100):
#     turtle.color('brown')
#     turtle.forward(300)
#     turtle.left(175)

# # Circle
# for i in range(360): 
#     turtle.forward(1)
#     turtle.right(1)

# # Infinity square
# turtle.penup()
# turtle.left(135)
# turtle.forward(300*1.414)
# turtle.right(135)
# turtle.pendown()
# y = int(600)
# while y != 0:
#     y -= 2
#     for j in range(2): 
#         turtle.forward(y)
#         turtle.right(90)

# # Realistic flower
# turtle.speed(0)
# y = 201
# while y != 0:
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#     for i in range(5):
#         turtle.left(20)
#         turtle.circle(y,90)
#         turtle.left(90)
#         turtle.circle(y,90)
#     y -= 3
# turtle.hideturtle()

# # Turtle race
# turtle.bgcolor('light green')
# main_turtle = turtle.Turtle()
# turtle1 = turtle.Turtle()
# turtle2 = turtle.Turtle()
# turtle3 = turtle.Turtle()
# turtle4 = turtle.Turtle()
# main_turtle.penup()
# turtle1.penup()
# turtle2.penup()
# turtle3.penup()
# turtle4.penup()
# turtle1.goto(-500,100)
# turtle2.goto(-500,0)
# turtle3.goto(-500,-100)
# turtle4.goto(-500,-200)
# turtle1.pendown()
# turtle2.pendown()
# turtle3.pendown()
# turtle4.pendown()
# main_turtle.pencolor('dark green')
# main_turtle.goto(400,200)
# main_turtle.pendown()
# main_turtle.pensize(10)
# main_turtle.right(90)
# main_turtle.forward(500)
# t1list = []
# t2list = []
# t3list = []
# t4list = []
# for i in range(1000) :
#     t1 = random.randrange(0,10)
#     t2 = random.randrange(0,10)
#     t3 = random.randrange(0,10)
#     t4 = random.randrange(0,10)
#     t1list.append(t1)
#     t2list.append(t2)
#     t3list.append(t3)
#     t4list.append(t4)
#     turtle1.speed(random.randrange(1,10))
#     turtle2.speed(random.randrange(1,10))
#     turtle3.speed(random.randrange(1,10))
#     turtle4.speed(random.randrange(1,10))
#     if sum(t1list) >= 900: 
#         turtle1.color('dark green')
#         style = ('Times New Roman', 30, 'italic')
#         turtle1.write('  TURTLE 1 WON', font=style, align='left')
#         break
#     elif sum(t2list) >= 900: 
#         turtle2.color('dark green')
#         style = ('Times New Roman', 30, 'italic')
#         turtle2.write('  TURTLE 2 WON', font=style, align='left')
#         break
#     elif sum(t3list) >= 900: 
#         turtle3.color('dark green')
#         style = ('Times New Roman', 30, 'italic')
#         turtle3.write('  TURTLE 3 WON', font=style, align='left')
#         break
#     elif sum(t4list) >= 900: 
#         turtle4.color('dark green')
#         style = ('Times New Roman', 30, 'italic')
#         turtle4.write('  TURTLE 4 WON', font=style, align='left')
#         break
#     else: 
#         turtle1.forward(t1)
#         turtle2.forward(t2)
#         turtle3.forward(t3)
#         turtle4.forward(t4)

# # Making a clock 
# sec = turtle.Turtle()
# min = turtle.Turtle()
# hour = turtle.Turtle()
# sec.speed(10)
# sec.penup()
# sec.goto(0,-200)
# sec.pendown()
# sec.circle(200)
# sec.penup()
# sec.goto(0,0)
# sec.left(90)
# min.left(90)
# hour.left(90)
# sec.pendown()
# for i in range(61):
#     hour.speed(2)
#     hour.forward(200)
#     for i in range(61):
#         min.speed(10)
#         min.forward(200)
#         for i in range(61):
#             sec.speed(2)
#             sec.forward(200)
#             sec.undo()
#             sec.right(6)
#         min.undo()
#         min.right(6)
#     hour.undo()
#     hour.right(6)

# # Spiral
# turtle.speed(0)
# turtle.penup()
# turtle.goto(0,-400)
# turtle.pendown()
# i = 300
# while i != 0:
#     turtle.circle(i,180)
#     i -= 5

# # Random Pattern
# turtle.speed(0)
# turtle.bgcolor('Black')
# turtle.penup()
# turtle.goto(-150,0)
# turtle.pendown()
# turtle.pensize(3)
# colour_list = ['Red','Blue','Green','Yellow','Violet','Purple','Orange']
# side = 200
# while side != 1200:
#     turtle.color(random.choice(colour_list))
#     for i in range(4):
#         turtle.forward(side)
#         turtle.right(90)
#     turtle.left(90)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
#     turtle.right(95)
#     side += 5

# # 3-d shapes
# turtle.speed(0)
# y = 300
# while y != -300: 
#     turtle.penup()
#     turtle.goto(-900,y)
#     turtle.pendown()
#     turtle.forward(500)
#     turtle.right(30)
#     turtle.circle(200,60)
#     turtle.right(30)
#     turtle.forward(200)
#     turtle.right(70)
#     turtle.forward(50)
#     turtle.left(70)
#     turtle.forward(300)
#     turtle.left(70)
#     turtle.forward(50)
#     turtle.setheading(0)
#     turtle.forward(400)
#     y -= 5

# # Snake game
# turtle.bgcolor('light green')
# snakehead = turtle.Turtle()
# snakehead.shape('square')

# Nibbles game 

turtle.done()