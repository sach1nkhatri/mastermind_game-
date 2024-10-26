import random
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Mastermind Game")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create the Turtle for drawing the game
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Define constants
ROWS = 10
COLUMNS = 4
FEEDBACK_SIZE = 2
COLORS = ["white", "red", "yellow", "green", "blue", "purple"]
answer = []
winnerFound = False
numRounds = 10
curRound = 0

# Draw the board
def draw_board():
    y_start = 250  # Adjust starting point for the rows
    for row in range(ROWS):
        draw_row(y_start - row * 50)  # Adjust the spacing as needed

def draw_row(y_pos):
    x_start = -150  # Adjust starting point for the guess circles
    for _ in range(COLUMNS):
        draw_circle(x_start, y_pos, 20)  # Adjust radius as needed
        x_start += 50  # Adjust spacing between circles
    
    x_start = 100  # Adjust starting point for feedback circles
    for i in range(FEEDBACK_SIZE):
        for j in range(FEEDBACK_SIZE):
            draw_circle(x_start + i * 15, y_pos - j * 15, 5)  # Adjust radius as needed

def draw_circle(x, y, radius, color="white"):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def update_guess(row, guess_colors):
    y_pos = 250 - row * 50
    x_start = -150
    for color in guess_colors:
        draw_circle(x_start, y_pos, 20, color)
        x_start += 50

def update_feedback(row, black_count, white_count):
    y_pos = 250 - row * 50
    x_start = 100
    # Draw black pins
    for _ in range(black_count):
        draw_circle(x_start, y_pos, 5, "black")
        x_start += 15
    # Draw white pins
    for _ in range(white_count):
        draw_circle(x_start, y_pos, 5, "white")
        x_start += 15

# Initialize the game
draw_board()
userChoice = input("Do you wish to manually enter answer (y/n): ")
if userChoice == "y":
    inputAnswer = input("For answer: list your four colors, comma separated: ")
    answer = inputAnswer.replace(" ", "").split(",")
else:
    answer = [random.choice(COLORS) for _ in range(4)]

# Main game loop
while not winnerFound and curRound < numRounds:
    userInput = input("For a guess: list your four colors, comma separated: ")
    userColors = userInput.replace(" ", "").split(",")

    # Check for correct positions
    positionsCorrect = 0
    for index in range(len(answer)):
        if answer[index] == userColors[index]:
            positionsCorrect += 1

    # Check for correct colors
    colorsCorrect = 0
    copyOfUserColors = userColors.copy()
    for answerColor in answer:
        for userColor in copyOfUserColors:
            if answerColor == userColor:
                colorsCorrect += 1
                copyOfUserColors.remove(userColor)
                break

    # Update the Turtle GUI with the guess and feedback
    update_guess(curRound, userColors)
    update_feedback(curRound, positionsCorrect, colorsCorrect - positionsCorrect)

    # Print the result in the console
    print("Your guess:", userColors)
    print("Black pegs (correct position):", positionsCorrect)
    print("White pegs (correct color, wrong position):", colorsCorrect - positionsCorrect)

    # Check for a win
    if positionsCorrect == 4:
        winnerFound = True
        print("You won!")
    else:
        curRound += 1

# Show the correct answer on the Turtle screen when the game ends
if winnerFound:
    print("Congratulations! You solved the puzzle!")
else:
    print("Game over. The correct answer was:", answer)
    update_guess(curRound, answer)  # Display the correct answer visually

# Keep the screen open
turtle.done()
