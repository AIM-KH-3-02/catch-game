import turtle
import winsound
import time
import math
import random

wn = turtle.Screen()
wn.title("Catch game by @AIM1")
wn.bgpic("sky.gif")
wn.setup(width=800, height=600)
wn.register_shape("pygame_left_1.gif")
wn.register_shape("pygame_right_1.gif")
wn.register_shape("chees.gif")
wn.register_shape("bomb.gif")
wn.register_shape("pygame_idle.gif")


def game_menu():
    #Створюємо простеньке меню для игры
    menu1 = turtle.Turtle()
    menu1.penup()
    menu1.speed(0)
    menu1.hideturtle()
    menu1.goto(0, 180)
    menu1.write("Main Menu", align="center", font=("verdana", 30, "bold"))

    menu2 = turtle.Turtle()
    menu2.speed(0)
    menu2.penup()
    menu2.goto(0, 100)
    wn.register_shape("game_start.gif")
    menu2.shape("game_start.gif")

    menu3 = turtle.Turtle()
    menu3.speed(0)
    menu3.penup()
    menu3.goto(0, 20)
    wn.register_shape("quit_game.gif")
    menu3.shape("quit_game.gif")

    def click1 (x, y):
        if x > menu2.xcor() - 63 and x < menu2.xcor() + 63 and y > menu2.ycor() - 25 and y < menu2.ycor() +25:
            menu1.clear()
            menu2.goto(0, 500)
            menu3.goto(0, 500)
            star_game()
        if x > menu3.xcor() - 63 and x < menu3.xcor() + 63 and y > menu3.ycor() - 25 and y < menu3.ycor() +25:
            menu1.clear()
            menu2.goto(0, 500)
            menu3.goto(0, 500)
            menu4 = turtle.Turtle()
            menu4.penup()
            menu4.speed(0)
            menu4.hideturtle()
            menu4.goto(0, 180)
            menu4.write("Are you sure?", align="center", font=("verdana", 30, "bold"))
            menu9 = turtle.Turtle()
            menu9.speed(0)
            menu9.penup()
            menu9.goto(0, 100)
            wn.register_shape("yes.gif")
            menu9.shape("yes.gif")

            menu10 = turtle.Turtle()
            menu10.speed(0)
            menu10.penup()
            menu10.goto(0, 20)
            wn.register_shape("no.gif")
            menu10.shape("no.gif")
            def click3(x, y):
                if x > menu9.xcor() - 63 and x < menu9.xcor() + 63 and y > menu9.ycor() - 25 and y < menu9.ycor() +25:
                    wn.bye()
                if x > menu10.xcor() - 63 and x < menu10.xcor() + 63 and y > menu10.ycor() - 25 and y < menu10.ycor() +25:
                    menu4.clear()
                    menu9.goto(0, 500)
                    menu10.goto(0, 500)
                    game_menu()
        turtle.listen()
        turtle.onscreenclick(click3, 1)

    turtle.listen()
    turtle.onscreenclick(click1, 1)


def star_game():
    score = 0
    lives = 5
    x = 50

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
    wn.onkey(go_left, "Left")
    wn.onkey(go_right, "Right")

    game_play = True

    while game_play:
        wn.update()

        def go_menu():
            wn.clear()
            txt.clear()
            game_play = False
            wn.bgpic("sky.gif")
            game_menu()

        turtle.listen()
        turtle.onkeypress(go_menu, "q")

        #Передвежение игрока
        if player.direction == "left" and player.xcor() > -360:
            x = player.xcor()
            x -= 20
            player.setx(x)

        if player.direction == "right" and player.xcor() < 360:
            x = player.xcor()
            x += 20
            player.setx(x)
        #Передвежение сыров
        for  chees in cheess:
            y = chees.ycor()
            y -= chees.speed
            chees.sety(y)
            #Проверка если предмет за пределами экрана (убавление очки ели это так)
            if y < -300:
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                chees.goto(x, y)
                score -= 5
                txt.clear()
                txt.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)

            #Проверка collision + добавление звука
            if chees.distance(player) < 60:
                winsound.PlaySound("smb_chees.wav", winsound.SND_ASYNC)
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                chees.goto(x, y)
                score += 20
                txt.clear()
                txt.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)
                if score == 500:
                    chees.speed = random.randint(10, 20)


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

            #Проверка collision + добавление звука
            if bomb.distance(player) < 60:
                winsound.PlaySound("smb_kick.wav", winsound.SND_ASYNC)
                x = random.randint(-380, 380)
                y = random.randint(300, 400)
                bomb.goto(x, y)
                score -= 10
                lives -= 1
                txt.clear()
                txt.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)
                if lives == 0:
                    wn.clear()
                    txt.clear()
                    game_play = False
                    wn.bgpic("sky.gif")
                    menu7 = turtle.Turtle()
                    menu7.color("yellow")
                    menu7.penup()
                    menu7.speed(0)
                    menu7.hideturtle()
                    menu7.goto(0, 180)
                    menu7.write("Game Over", align="center", font=("verdana", 30, "bold"))

                    menu6 = turtle.Turtle()
                    menu6.speed(0)
                    menu6.penup()
                    menu6.goto(0, 100)
                    wn.register_shape("go_to_menu.gif")
                    menu6.shape("go_to_menu.gif")
                    def click2 (x, y):
                        if x > menu6.xcor() - 63 and x < menu6.xcor() + 63 and y > menu6.ycor() - 25 and y < menu6.ycor() +25:
                            menu7.clear()
                            menu6.goto(0, 500)
                            game_menu()
                    turtle.listen()
                    turtle.onscreenclick(click2, 1)
game_menu()
wn.mainloop()
