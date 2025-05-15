#DATE 15/05/2025
#PROGRAM Maths Quiz
#AUTHOR William Eric Eames

# inputs the random library
import random
from operator import index

# initialise game variables for game history
questions_answered = 0
questions_correct = 0
questions_wrong = 0

# description of what you need to do
# and how to play
print("Hello, welcome to my maths quiz!")
print("Answer these basic facts questions...\n")

# asks how many rounds they would like to do
num_questions = int(input("How many questions? "))

# producing the random number equations
for index in range(num_questions):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

# asking the question
    answer = int(input(f"Question {index + 1}: What is {num1} + {num2}? "))

# checking the answer
    if answer == num1 + num2:
        print("Correct! \n")
        questions_correct += 1
    else:
        print(f"Oh no! The correct answer is {num1 + num2}!\n")
        questions_wrong += 1

# asking if you want to see the game history
game_history = input("Do you want to see your game history? yes/no ")

# adding onto the questions_answered variable
questions_answered += 1

# calculate game history
questions_correct = questions_answered - questions_correct - questions_wrong
percent_won = questions_correct / questions_answered * 100
percent_lost = questions_wrong / questions_answered * 100
percent_tied = 100 - percent_won - percent_lost

# producing the game history
if game_history == "yes":
    print("📈📈📈 Game Statistics 📈📈📈")
    print(f" Won: {percent_won:.2f} \t "
          f" Lost: {percent_lost:.2f}\n")

# output for after the game history
print("👍👍👍 Thanks for playing my maths quiz 👍👍👍")