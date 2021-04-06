#all imports
import turtle
import time
import random

#the delay
delay=0.1

#Score
score=0
high_score=0

#screen title
wn=turtle.Screen()
wn.title("Snake by coder-lg")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#Head of the snake

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#snake body
segments=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color=("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260) 
pen.write("Score=0,High Score=0",align="center",font=("Courier",24,"normal"))


#Function
def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)    

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#keyboard commands here below
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


#game loop       
while True:
    wn.update()

    #Border collision check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #Hide segment
        for segment in segments:
            segment.goto(1000,1000)

        #Clear list of segments
        segments.clear() 

        #Reset the normal score
        score=0

        pen.clear()
        pen.write("Score={},High Score={}".format(score,high_score),align="center",font=("Courier",24,"normal"))   

    #COllision check with food
    if head.distance(food)<20:
        #Food movement
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        #Add a segment of the body
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay-=0.001

        #Reset the delay
        delay=0.1

        #Score increase
        score+=10

        if score>high_score:
            high_score=score
        
        pen.clear()
        pen.write("Score={},High Score={}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    
    #Movement of body to head
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move 0 segment to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    

     
    move()

    time.sleep(delay)

wn.mainloop()
