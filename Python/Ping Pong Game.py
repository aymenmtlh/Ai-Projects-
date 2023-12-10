from tkinter.tix import Balloon
import turtle 

wind = turtle.Screen()
wind.title(' ping pong by aymen')
wind.bgcolor("Black")
wind.setup(width=800 , height= 600 )
wind.tracer(0)



#### rassm lmadrab 1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("Blue")
madrab1.penup()  
madrab1.goto(-350 , 0)
madrab1.home
madrab1.shapesize(stretch_len=1 , stretch_wid=5)
#### rasm l madrab 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350 , 0)
madrab2.shapesize(stretch_len=1 , stretch_wid=5)
## rasmm l bola 
kora = turtle.Turtle()
kora.speed(0)
kora.shape("circle")
kora.color("white")
kora.penup()
kora.goto(0 , 0)

### score 
score1=0
score2=0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write(" Player 1 : 0 , Player 2 : 0 " ,  align=("center") , font=("courier" , 24 , " normal"))

### mouvment
def madrab1_up() :
    y = madrab1.ycor()
    y+= 20
    madrab1.sety(y)
def madrab1_down() :
    y = madrab1.ycor()
    y-= 20
    madrab1.sety(y)
def madrab2_up() :
    y = madrab2.ycor()
    y+= 20
    madrab2.sety(y)
def madrab2_down() :
    y = madrab2.ycor()
    y-= 20
    madrab2.sety(y)    


### keyboard mouvementt 
wind.listen()
wind.onkeypress(madrab1_up , "8")
wind.onkeypress(madrab1_down , "2")
wind.onkeypress(madrab2_up , "Up")
wind.onkeypress(madrab2_down , "Down")

## ball mouvement 
kora.dx = 0.5

kora.dy = 0.5


while True : 
    wind.update()
    kora.setx(kora.xcor() + kora.dx )
    kora.sety(kora.ycor() + kora.dy )
        ## borders cheak 
    if kora.ycor() > 290 :
        kora.sety(290)
        kora.dy *= - 1
    if kora.ycor() < -290 :
        kora.sety(-290)
        kora.dy *= - 1
    if kora.xcor() > 390 : 
        kora.goto (0,0)
        score1 += 1
        score.clear()
        score.write(" Player 1 : {} , Player 2 : {} ".format(score1, score2) ,  align=("center") , font=("courier" , 24 , " normal"))
    if kora.xcor()  < -390 :
        kora.goto(0,0)
        score2 +=1
        score.clear()
        score.write(" Player 1 : {} , Player 2 : {} ".format(score1, score2) ,  align=("center") , font=("courier" , 24 , " normal"))
        #tasadom amdrab w kora 
    if (kora.xcor() > 340 and kora.xcor() < 350 ) and (kora.ycor() < madrab2.ycor() + 40 and kora.ycor() > madrab2.ycor() -40 ) :
        kora.setx(340)
        kora.dx *= -1 

    if (kora.xcor() < -340 and kora.xcor() > -350 ) and (kora.ycor() < madrab1.ycor() + 40 and kora.ycor() > madrab1.ycor() -40 ) :
        kora.setx(-340)
        kora.dx *= -1 
