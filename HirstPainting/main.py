# up-coming code extracts a color pallet from a picture using a module called 'Colorgram'
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle
import random
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = turtle.Turtle()
screen = turtle.Screen()
tim.penup()
tim.setx(-200)
tim.sety(-200)
tim.penup()
screen.colormode(255)
tim.speed("fastest")

for i in range(1,11):
    for j in range(1,11):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.setx(tim.xcor()+50)

    tim.setx(-200)
    tim.sety(tim.ycor()+60)
tim.hideturtle()




screen.exitonclick()

print(color_list)
