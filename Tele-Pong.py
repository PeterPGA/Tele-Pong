#imports

import turtle
import random as rd

wn = turtle.Screen()
wn.title("Tele-Pong")
wn.bgcolor("black")
wn.setup(width=1600, height=1000)
wn.tracer(0)

#Objects

#Paddle Rs

paddleRs = turtle.Turtle()
paddleRs.speed(0)
paddleRs.shape("circle")
paddleRs.color("red")
paddleRs.shapesize(stretch_wid=1, stretch_len=1)
paddleRs.penup()
paddleRs.goto(780, 0)

#Paddle R

paddleR = turtle.Turtle()
paddleR.speed(0)
paddleR.shape("circle")
paddleR.color("green")
paddleR.shapesize(stretch_wid=5, stretch_len=1)
paddleR.penup()
paddleR.goto(750, 0)

#Paddle r

paddler = turtle.Turtle()
paddler.speed(0)
paddler.shape("circle")
paddler.color("blue")
paddler.shapesize(stretch_wid=2, stretch_len=1)
paddler.penup()
paddler.goto(700, 0)

#Paddle Ls

paddleLs = turtle.Turtle()
paddleLs.speed(0)
paddleLs.shape("circle")
paddleLs.color("red")
paddleLs.shapesize(stretch_wid=1, stretch_len=1)
paddleLs.penup()
paddleLs.goto(-780, 0)

#Paddle L

paddleL = turtle.Turtle()
paddleL.speed(0)
paddleL.shape("circle")
paddleL.color("green")
paddleL.shapesize(stretch_wid=5, stretch_len=1)
paddleL.penup()
paddleL.goto(-750, 0)

#Paddle l

paddlel = turtle.Turtle()
paddlel.speed(0)
paddlel.shape("circle")
paddlel.color("blue")
paddlel.shapesize(stretch_wid=2, stretch_len=1)
paddlel.penup()
paddlel.goto(-700, 0)

#Balls

balla = turtle.Turtle()
balla.speed(0)
balla.shape("circle")
balla.color("grey")
balla.penup()
balla.goto(0,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ballb = turtle.Turtle()
ballb.speed(0)
ballb.shape("circle")
ballb.color("grey")
ballb.penup()
ballb.goto(0,0)

ballc = turtle.Turtle()
ballc.speed(0)
ballc.shape("circle")
ballc.color("grey")
ballc.penup()
ballc.goto(0,0)

ball.dx = 0.5
ball.dy = 1

lista = [1, -1]
listb = [1, -1]
a = rd.choice(lista)
b = rd.choice(listb)
ball.dx = a
ball.dx = b


balla.dx = ball.dx
balla.dy = ball.dy
ballb.dx = ball.dx
ballb.dy = ball.dy
ballc.dx = ball.dx
ballc.dy = ball.dy



#Score

L = 0
R = 0

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 450)
pen.write("LEFT {}      {} RIGHT".format(L, R), align="center", font=("Ubuntu", 24, "normal"))

ven = turtle.Turtle()
ven.speed(0)
ven.color("white")
ven.penup()
ven.hideturtle()
ven.goto(0, -450)
ven.write("VERTICAL SPEED {}      {} HORIZONTAL SPEED".format(round(abs(ball.dx), 2), round(abs(ball.dy), 2)), align="center", font=("Ubuntu", 24, "normal"))

void = turtle.Turtle()
void.speed(0)
void.shape("circle")
void.color("white")
void.shapesize(stretch_wid=10, stretch_len=10)

#Primary Functions

def paddleL_up():
    L = paddleL.ycor()
    if (L < 430):
        L += 12.5
        paddleL.sety(L)

def paddleL_down():
    L = paddleL.ycor()
    if (L > -420):
        L -= 12.5
        paddleL.sety(L)

def paddleR_up():
    R = paddleR.ycor()
    if (R < 430):
        R += 12.5
        paddleR.sety(R)

def paddleR_down():
    R = paddleR.ycor()
    if (R > -420):
        R -= 12.5
        paddleR.sety(R)

#Secondary Functions


def paddlel_up():
    l = paddlel.ycor()
    if (l < 470):
        l += 25
        paddlel.sety(l)

def paddlel_down():
    l = paddlel.ycor()
    if (l > -450):
        l -= 25
        paddlel.sety(l)

def paddler_up():
    r = paddler.ycor()
    if (r < 470):
        r += 25
        paddler.sety(r)

def paddler_down():
    r = paddler.ycor()
    if (r > -450):
        r -= 25
        paddler.sety(r)

#Tertiary Functions

def paddlers_up():
    rs = paddleRs.ycor()
    if (rs < 485):
        rs += 5
        paddleRs.sety(rs)

def paddlers_down():
    rs = paddleRs.ycor()
    if (rs > -480):
        rs -= 5
        paddleRs.sety(rs)

def paddlels_up():
    ls = paddleLs.ycor()
    if (ls < 485):
        ls += 5
        paddleLs.sety(ls)

def paddlels_down():
    ls = paddleLs.ycor()
    if (ls > -480):
        ls -= 5
        paddleLs.sety(ls)

def ix():
    ball.dx += 1
def dx():
    ball.dx -= 1
def iy():
    ball.dy += 1
def dy():
    ball.dy -= 1
def stop():
    ball.dx = 0
    ball.dy = 0

def restart():
    ball.dx = -1
    ball.dy = 1

    ball.goto(0,0)
    balla.goto(0,0)
    ballb.goto(0,0)
    ballc.goto(0,0)

def inversionx():
    ball.dx *= -1

def inversiony():
    ball.dy *= -1


# Keyboard binding

wn.listen()

#Hacks
wn.onkey(ix, "1")
wn.onkey(dx, "2")
wn.onkey(iy, "3")
wn.onkey(dy, "4")
wn.onkey(stop, "z")
wn.onkey(restart, "t")

#Movement
wn.onkey(paddlels_up, "q")
wn.onkey(paddlels_down, "a")
wn.onkey(paddleL_up, "w")
wn.onkey(paddleL_down, "s")
wn.onkey(paddlel_up, "e")
wn.onkey(paddlel_down, "d")
wn.onkey(paddlers_up, "p")
wn.onkey(paddlers_down, ";")
wn.onkey(paddleR_up, "o")
wn.onkey(paddleR_down, "l")
wn.onkey(paddler_up, "i")
wn.onkey(paddler_down, "k")
wn.onkey(inversionx, "x")
wn.onkey(inversiony, "c")

while True:
    wn.update()
    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    balla.setx(balla.xcor() - (balla.dx))
    balla.sety(balla.ycor() + (balla.dy))
    ballb.setx(ballb.xcor() + (ballb.dx))
    ballb.sety(ballb.ycor() - (ballb.dy))
    ballc.setx(ballc.xcor() - (ballc.dx))
    ballc.sety(ballc.ycor() - (ballc.dy))

    # Border check

    if ball.ycor() > 490:
        ball.sety(490)
        ball.dy *= -1

    if ball.ycor() < -490:
        ball.sety(-490)
        ball.dy *= -1

    if ball.xcor() > 800:
        ball.goto(0, 0)
        ball.dx *= -1
        L += 1
        pen.clear()
        pen.write("LEFT {}      {} RIGHT".format(L, R), align="center", font=("Ubuntu", 24, "normal"))

    if ball.xcor() < -800:
        ball.goto(0, 0)
        ball.dx *= -1
        R += 1
        pen.clear()
        pen.write("LEFT {}      {} RIGHT".format(L, R), align="center", font=("Ubuntu", 24, "normal"))

    if balla.ycor() > 490:
        balla.sety(490)
        balla.dy *= -1

    if balla.ycor() < -490:
        balla.sety(-490)
        balla.dy *= -1

    if balla.xcor() > 800:
        balla.setx(800)
        balla.dx *= -1

    if balla.xcor() < -800:
        balla.setx(-800)
        balla.dx *= -1

    if ballb.ycor() > 490:
        ballb.sety(490)
        ballb.dy *= -1

    if ballb.ycor() < -490:
        ballb.sety(-490)
        ballb.dy *= -1

    if ballb.xcor() > 800:
        ballb.setx(800)
        ballb.dx *= -1

    if ballb.xcor() < -800:
        ballb.setx(-800)
        ballb.dx *= -1

    if ballc.ycor() > 490:
        ballc.sety(490)
        ballc.dy *= -1

    if ballc.ycor() < -490:
        ballc.sety(-490)
        ballc.dy *= -1

    if ballc.xcor() > 800:
        ballc.setx(800)
        ballc.dx *= -1

    if ballc.xcor() < -800:
        ballc.setx(-800)
        ballc.dx *= -1

     # Paddle and ball collisions

    #normal

    if (ball.xcor() > 740 and ball.xcor() < 760) and (ball.ycor() < paddleR.ycor() + 50 and ball.ycor() > paddleR.ycor() - 50):
        ball.setx(741)
        ball.dx *= -1
        if (abs(ball.dy) > 1):
            ball.dy /= 2
            ball.dy = int(ball.dy)
        balla.dx = ball.dx
        balla.dy = ball.dy
        ballb.dx = ball.dx
        ballb.dy = ball.dy
        ballc.dx = ball.dx
        ballc.dy = ball.dy
        ven.clear()

    if (ball.xcor() < -740 and ball.xcor() > -760) and (ball.ycor() < paddleL.ycor() + 50 and ball.ycor() > paddleL.ycor() - 50):
        ball.setx(-741)
        ball.dx *= -1
        balla.dx = ball.dx
        balla.dy = ball.dy
        ballb.dx = ball.dx
        ballb.dy = ball.dy
        ballc.dx = ball.dx
        ballc.dy = ball.dy
        ven.clear()

    # fast

    if (ball.xcor() > 680 and ball.xcor() < 720) and (ball.ycor() < paddler.ycor() + 20 and ball.ycor() > paddler.ycor() - 20):
        ball.setx(125)
        ball.dx *= -2
        balla.dx = ball.dx
        balla.dy = ball.dy
        ballb.dx = ball.dx
        ballb.dy = ball.dy
        ballc.dx = ball.dx
        ballc.dy = ball.dy

    if (ball.xcor() < -680 and ball.xcor() > -720) and (ball.ycor() < paddlel.ycor() + 20 and ball.ycor() > paddlel.ycor() - 20):
        ball.setx(-125)
        ball.dx *= -2
        balla.dx = ball.dx
        balla.dy = ball.dy
        ballb.dx = ball.dx
        ballb.dy = ball.dy
        ballc.dx = ball.dx
        ballc.dy = ball.dy

    # slow

    if (ball.xcor() > 775 and ball.xcor() < 800) and (ball.ycor() < paddleRs.ycor() + 10 and ball.ycor() > paddleRs.ycor() - 10):
        ball.setx(-300)
        ball.dy *= 4
        ball.dx *= -1
        balla.dx = ball.dx
        balla.dy = ball.dy
        ballb.dx = ball.dx
        ballb.dy = ball.dy
        ballc.dx = ball.dx
        ballc.dy = ball.dy

    if (ball.xcor() < -775 and ball.xcor() > -800) and (ball.ycor() < paddleLs.ycor() + 10 and ball.ycor() > paddleLs.ycor() - 10):
        ball.setx(300)
        ball.dy *= 4
        ball.dx *= -1
        balla.dx = ball.dx
        balla.dy = ball.dy
        ballb.dx = ball.dx
        ballb.dy = ball.dy
        ballc.dx = ball.dx
        ballc.dy = ball.dy

    #additional boundaries

   

    if (ball.dx > 8):
        ball.dx = 8

    if (ball.dx < -8):
        ball.dx = -8

    if (ball.dy > 8):
        ball.dy = 8

    if (ball.dy < -8):
        ball.dy = -8
    

    if ((ball.dx * ball.dy == 64) or (ball.dx * ball.dy == -64)):
        ball.dx = -1
        ball.dy = 1

        ball.goto(0,0)
        balla.goto(0,0)
        ballb.goto(0,0)
        ballc.goto(0,0)

    ven.clear()
    ven.write("VERTICAL SPEED {}      {} HORIZONTAL SPEED".format(round(abs(ball.dy), 2), round(abs(ball.dx), 2)), align="center", font=("Ubuntu", 24, "normal"))
