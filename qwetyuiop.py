import random

# Define a function to display the quiz questions and options
def display_question(question, options):
    print("\n" + question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")

# Define a function to get the user's answer and validate it
def get_user_answer():
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Define a function to run the quiz
def run_quiz(questions):
    score = 0
    # Shuffle the questions to randomize their order
    question_items = list(questions.items())
    random.shuffle(question_items)

    for question, data in question_items:
        display_question(question, data['options'])
        user_answer = get_user_answer()

        # Check if the user's answer is correct
        if data['options'][user_answer - 1] == data['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {data['answer']}")

    # Display the final score
    print(f"\nYour final score is: {score} out of {len(questions)}")

    # Remove the questions that have been asked
    return question_items

# Define the quiz questions, options, and answers
quiz_questions = {
    "What is the capital of France?": {
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    "What is the largest planet in our solar system?": {
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    "Which language is primarily used for Android app development?": {
        "options": ["Swift", "Kotlin", "JavaScript", "Python"],
        "answer": "Kotlin"
    },
    "What is the square root of 64?": {
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    "Which element has the chemical symbol 'O'?": {
        "options": ["Gold", "Oxygen", "Silver", "Iron"],
        "answer": "Oxygen"
    }
}

# Track used questions to ensure they are not repeated
used_questions = []

# Main loop to run the quiz until there are no questions left
while quiz_questions:
    print("\nStarting a new quiz round...")
    
    # Run the quiz with the current set of questions
    used_questions = run_quiz(quiz_questions)
    
    # Remove used questions from the available questions
    for question, _ in used_questions:
        del quiz_questions[question]

    # Check if there are any questions left for the next round
    if not quiz_questions:
        print("All questions have been used. No more questions left!")

