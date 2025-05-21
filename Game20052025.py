# DATE 15/05/2025
# PROGRAM Maths Quiz
# AUTHOR William Eric Eames

# imports the random library
import random

# Word to number conversion dictionary
word_to_number = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12
}

# initialise game variables for game history
questions_answered = 0
questions_correct = 0
questions_wrong = 0

# description of what you need to do
# and how to play
print("Hello, welcome to my maths quiz!")
print("Answer these basic facts questions...\n")

# asking the question
while True:
    answer = input("How many questions? ").strip().lower()

    # converting the word into a number
    if answer.isdigit():
        num_questions = int(answer)
        break
    elif answer in word_to_number:
        num_questions = word_to_number[answer]
        break
    else:
        print("Please enter a valid number (digit or word up to twelve).")

# asking the questions
for index in range(num_questions):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

    while True:
        try:
            answer = int(input(f"Question {index + 1}: What is {num1} + {num2}? "))
            break
        except ValueError:
            print("Please enter a number.")

    if answer == num1 + num2:
        print("Correct! \n")
        questions_correct += 1
    else:
        print(f"Oh no! The correct answer is {num1 + num2}!\n")
        questions_wrong += 1
    questions_answered += 1

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