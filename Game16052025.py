# DATE 15/05/2025
# PROGRAM Maths Quiz
# AUTHOR William Eric Eames

# imports the random library
import random

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

    # count this question as the user answers it
    questions_answered += 1

# checking to see if the answer for the number of
# questions are only numbers


# checking to see if the answer for the questions
# are numbers


# calculate the percentages for the statistics
percent_correct = (questions_correct / questions_answered) * 100
percent_wrong = (questions_wrong / questions_answered) * 100

# asking if you want to see the game history
game_history = input("Do you want to see your game history? yes/no ").lower()

# producing the game history
if game_history == "yes":
    print("\n📈📈📈 Game Statistics 📈📈📈")
    print(f"Questions Answered: {questions_answered}")
    print(f"Correct Answers: {questions_correct} ({percent_correct:.2f}%)")
    print(f"Wrong Answers: {questions_wrong} ({percent_wrong:.2f}%)\n")

# output for after the game history
print("👍👍👍 Thanks for playing my maths quiz 👍👍👍")