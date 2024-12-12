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

# Define a function to run the quiz for the selected difficulty level
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

# Define the quiz questions for each difficulty level
easy_questions = {
    "What is the capital of France?": {
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    "What is the square root of 64?": {
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    "What is the color of the sky on a clear day?": {
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": "Blue"
    },
    "How many days are there in a week?": {
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    "What is 2 + 2?": {
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    "What is the capital of England?": {
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "London"
    },
    "What is the largest planet in our solar system?": {
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    "What is the chemical symbol for water?": {
        "options": ["O2", "H2O", "CO2", "NaCl"],
        "answer": "H2O"
    },
    "How many continents are there on Earth?": {
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    "What is the color of a ripe banana?": {
        "options": ["Red", "Green", "Yellow", "Blue"],
        "answer": "Yellow"
    }
}

medium_questions = {
    "What is the smallest prime number?": {
        "options": ["1", "2", "3", "5"],
        "answer": "2"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    "Who wrote 'Romeo and Juliet'?": {
        "options": ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "George Orwell"],
        "answer": "William Shakespeare"
    },
    "What is the capital of Japan?": {
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
    },
    "Which gas do plants absorb from the atmosphere?": {
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    "Which language is primarily used for Android app development?": {
        "options": ["Swift", "Kotlin", "JavaScript", "Python"],
        "answer": "Kotlin"
    },
    "Which country is known as the Land of the Rising Sun?": {
        "options": ["China", "India", "Japan", "Thailand"],
        "answer": "Japan"
    },
    "What is the freezing point of water in degrees Celsius?": {
        "options": ["0", "32", "100", "212"],
        "answer": "0"
    },
    "Who painted the Mona Lisa?": {
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    "What is the largest ocean on Earth?": {
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    }
}

difficult_questions = {
    "What is the chemical symbol for gold?": {
        "options": ["Au", "Ag", "Pb", "Fe"],
        "answer": "Au"
    },
    "Which organelle is known as the powerhouse of the cell?": {
        "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi Apparatus"],
        "answer": "Mitochondria"
    },
    "In which year did the Titanic sink?": {
        "options": ["1910", "1912", "1914", "1916"],
        "answer": "1912"
    },
    "What is the capital of Australia?": {
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "answer": "Canberra"
    },
    "Who developed the theory of relativity?": {
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Niels Bohr"],
        "answer": "Albert Einstein"
    },
    "Which element has the atomic number 1?": {
        "options": ["Helium", "Hydrogen", "Oxygen", "Carbon"],
        "answer": "Hydrogen"
    },
    "What is the hardest natural substance on Earth?": {
        "options": ["Gold", "Iron", "Diamond", "Quartz"],
        "answer": "Diamond"
    },
    "What is the longest river in the world?": {
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    "What is the square root of 256?": {
        "options": ["12", "14", "16", "18"],
        "answer": "16"
    },
    "Which planet is known for its rings?": {
        "options": ["Earth", "Mars", "Saturn", "Venus"],
        "answer": "Saturn"
    }
}

# Main function to run the quiz with chosen difficulty level
def main():
    while True:
        # Prompt the user to select a difficulty level
        print("\nSelect a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Difficult")
        print("4. Exit")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                run_quiz(easy_questions)
            elif choice == 2:
                run_quiz(medium_questions)
            elif choice == 3:
                run_quiz(difficult_questions)
            elif choice == 4:
                print("Exiting the quiz.")
                break
            else:
                print("Please enter a valid choice (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
