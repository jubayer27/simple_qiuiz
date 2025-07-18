import questions
from source import questions as source

test_questions = []

for question in source:
    test_questions.append(
        questions.Question(
            question["question"],
            question["options"],
            question["answer"]
    )

    )

user_score = 0
prize_money = 10000

# Print the questions to verify they are created correctly


#get user data
user_name = input("What is your name?: ")
print(f"Hello {user_name}, welcome to the quiz!")
print(f"Your score is {user_score}")
print("Let's start the quiz!")
print("************************************")

# Loop through each question
for i in range(len(test_questions)):
    print(f"Question {i + 1}: {test_questions[i].question}")
    for j, option in enumerate(test_questions[i].options):
        print(f"{j + 1}. {option}")

    # Get user's answer
    user_answer = input("Please enter the number of your answer: ")
    while int(user_answer) < 1 or int(user_answer) > len(test_questions[i].options):
        print("Invalid input. Please enter a number corresponding to one of the options.")
        user_answer = input("Please enter the number of your answer: ")


    # Check if the answer is correct
    if test_questions[i].options[int(user_answer) - 1] == test_questions[i].answer:
        print("Correct!")
        user_score += 1
    else:
        print(f"Wrong! The correct answer is: {test_questions[i].answer}")
        prize_money = prize_money - user_score * 1000

    print(f"Your current score is: {user_score}")

    print(f"Your prize money is: {prize_money}")

    print("************************************")
