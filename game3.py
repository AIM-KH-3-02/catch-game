import turtle
import random

wn = turtle.Screen()
wn.title("Catch game by @AIM1")
wn.bgcolor("green")
wn.bgpic("sky.gif")
wn.setup(width=800, height=600)
wn.register_shape("pygame_left_1.gif")
wn.register_shape("pygame_right_1.gif")
wn.register_shape("chees.gif")
wn.register_shape("bomb.gif")
wn.register_shape("pygame_idle.gif")


score = 0
lives = 3

#Добавляем игрока
player = turtle.Turtle()
player.speed(0)
player.shape("pygame_idle.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

cheess = []
#Добавляем сыр
for  _ in range(5):
    chees = turtle.Turtle()
    chees.speed(0)
    chees.shape("chees.gif")
    chees.color("blue")
    chees.penup()
    chees.goto(-100, 250)
    chees.speed = random.randint(5, 10)
    cheess.append(chees)

bombs = []
#Добавляем сыр
for  _ in range(5):
    bomb = turtle.Turtle()
    bomb.speed(0)
    bomb.shape("bomb.gif")
    bomb.color("red")
    bomb.penup()
    bomb.goto(100, 250)
    bomb.speed = random.randint(5, 10)
    bombs.append(bomb)


txt = turtle.Turtle()
txt.hideturtle()
txt.speed(0)
txt.shape("square")
txt.color("white")
txt.penup()
txt.goto(0, 260)
font = {"Courier", 24, "normal"}
txt.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)

def go_left():
    player.direction = "left"
    player.shape("pygame_left_1.gif")

def go_right():
    player.direction = "right"
    player.shape("pygame_right_1.gif")

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



while True:
    wn.update()
    #Передвежение игрока
    if player.direction == "left":
        x = player.xcor()
        x -= 20
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 20
        player.setx(x)
    #Передвежение сыров
    for  chees in cheess:
        y = chees.ycor()
        y -= chees.speed
        chees.sety(y)
        #Проверка если предмет за пределами экрана
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            chees.goto(x, y)

        #Проверка collision
        if chees.distance(player) < 60:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            chees.goto(x, y)
            score += 10
            txt.clear()
            txt.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)


    #Передвежение бомбы
    for  bomb in bombs:
        y = bomb.ycor()
        y -= bomb.speed
        bomb.sety(y)
        #Проверка если предмет за пределами экрана
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bomb.goto(x, y)

        #Проверка collision
        if bomb.distance(player) < 60:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bomb.goto(x, y)
            score -= 10
            lives -= 1
            txt.clear()
            txt.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)


wn.mainloop()
