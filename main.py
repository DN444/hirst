#import colorgram
#rgb_colors=[]
#colors=colorgram.extract('images.jpeg',30)
#for i in colors:
#    r=i.rgb.r
#    g=i.rgb.g
#    b=i.rgb.b
#    new_color=(r,g,b)
#    rgb_colors.append(new_color)
#print(rgb_colors)
from turtle import *
import random
tutel=Turtle()
colormode(255)
tutel.speed(0)
tutel.penup()
tutel.hideturtle()
colours=[(206, 157, 107),(107, 109, 128),(141, 141, 154),(223, 211, 116),(175, 73, 37),(203, 148, 174),(178, 157, 43),(106, 112, 168),(187, 15, 4),(16, 18, 59),(16, 33, 17),(226, 169, 195),(33, 32, 15),(213, 83, 60),(233, 173, 161),(192, 10, 19),(42, 45, 114),(154, 168, 157),(140, 77, 88),(89, 104, 93),(181, 181, 218),(202, 79, 92),(33, 17, 32),(223, 210, 20),(72, 76, 40),(179, 200, 182)]
tutel.setheading(225)
tutel.forward(300)
tutel.setheading(0)
dots=100
for i in range(1,dots+1):
    tutel.dot(20,random.choice(colours))
    tutel.forward(50)
    if i%10==0:
        tutel.left(90)
        tutel.forward(50)
        tutel.left(90)
        tutel.forward(500)
        tutel.setheading(0)
scr=Screen()
scr.exitonclick()