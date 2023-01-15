from tkinter import *
import random

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 15
BACKGROUND_COLOR = "black"
SNAKE_HEAD_COLOR = "skyblue"
SNAKE_BODY_COLOR = "blue"
FOOD_COLOR = "purple"
SCORE = 0
direction='right'

snakeHead = [0, 150]
snakePosition = [[0, 150], [0, 150-SPACE_SIZE]]
food = [int((random.randint(0, GAME_WIDTH))/SPACE_SIZE)*SPACE_SIZE, int((random.randint(0, GAME_HEIGHT))/SPACE_SIZE)*SPACE_SIZE]

window = Tk()
window.title("LAKPA'S GAME")
window.config(bg="black")
window.geometry("650x700")
window.resizable(0, 0)

title=Label(window, text=" SUNWAY SNAKE GAME FOR KIDS", font=('consolas', 25), bg="black", fg="white")
title.pack()

scoreBoard = Label(window, text="SCORE:{}".format(SCORE), font=('consolas', 15), bg="black", fg="white")
scoreBoard.pack(side=BOTTOM)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


def drawSnake():
    for position in snakePosition:
        canvas.create_rectangle(position[0], position[1], position[0]+SPACE_SIZE, position[1]+SPACE_SIZE, fill=SNAKE_BODY_COLOR, tag="snake")
    canvas.create_rectangle(snakeHead[0], snakeHead[1], snakeHead[0]+SPACE_SIZE, snakeHead[1]+SPACE_SIZE, fill=SNAKE_HEAD_COLOR, tag="snake")

def showFood():
    global food, SCORE
    canvas.create_oval(food[0], food[1], food[0]+SPACE_SIZE, food[1]+SPACE_SIZE, fill=FOOD_COLOR, tag="food")
    if(snakeHead==food):
        SCORE += 1
        scoreBoard.config(text="Score: {}".format(SCORE))
        food = [int((random.randint(0, GAME_WIDTH))/SPACE_SIZE)*SPACE_SIZE, int((random.randint(0, GAME_HEIGHT))/SPACE_SIZE)*SPACE_SIZE]    
        snakePosition.append(food)

    if check_collision():
        game_over()

def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction
    else:
        direction = direction


window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))


def move():
    global direction, snakeHead, snakePosition

    if direction == 'up':
        snakeHead[1] -= SPACE_SIZE
        snakePosition.insert(0, list(snakeHead))
        snakePosition.pop()
    elif direction == 'down':
        snakeHead[1] += SPACE_SIZE
        snakePosition.insert(0, list(snakeHead))
        snakePosition.pop()
    elif direction == 'right':
        snakeHead[0] += SPACE_SIZE
        snakePosition.insert(0, list(snakeHead))
        snakePosition.pop()
    elif direction == 'left':
        snakeHead[0] -= SPACE_SIZE
        snakePosition.insert(0, list(snakeHead))
        snakePosition.pop() 
 
def check_collision():
    if snakeHead[0] < 0 or snakeHead[0] > GAME_WIDTH:
        return True
    elif snakeHead[1] < 0 or snakeHead[1] > GAME_HEIGHT:
        return True
    for bodyPart in snakePosition[1:]:
        if snakeHead[0] == bodyPart[0] and snakeHead[1] == bodyPart[1]:
            canvas.delete(ALL)
            return True
    return False


def game_over():
    global snakePosition
    snakePosition.clear()
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 20), text="      GAME OVER!!!\nYOU HAVE SCORED {} POINTS".format(SCORE), 
    fill="white", tag="gameover")

def update():
    move()
    canvas.delete('all')
    showFood()
    drawSnake()
    window.update()
    window.after(SPEED, update) 

update()

window.mainloop()