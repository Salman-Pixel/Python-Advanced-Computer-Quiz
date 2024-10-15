import random
import time

# Function to display questions and collect answers
def ask_question(question, correct_answer, score, question_number):
    print(f"\nQuestion {question_number}: {question}")
    start_time = time.time()  # Start timing
    answer = input("Your answer: ").lower()
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    
    if elapsed_time > 10:  # Time limit of 10 seconds
        print("Time's up! You took too long to answer.")
        return score  # No score if time is up
    
    if answer == correct_answer:
        print("Correct!")
        score += 3  # Points for correct answer
    else:
        print("Incorrect :| The correct answer is:", correct_answer)
    
    return score

# Main program
def play_quiz():
    print("Welcome to my computer quiz!")
    playing = input("Do you want to play? (yes/no) ").lower()

    if playing != "yes":
        print("Aight mate! Goodbye...")
        quit()

    print("Alright! Let's play :)")
    score = 0
    questions = 0
    
    # List of questions
    question_list = [
        ("What does the CPU stand for?", "central processing unit"),
        ("What does the GPU stand for?", "graphics processing unit"),
        ("What does IBM stand for?", "international business machine"),
        ("What does the RAM stand for?", "random access memory"),
        ("What does the ROM stand for?", "read only memory"),
        ("What does HTTP stand for?", "hypertext transfer protocol"),
        ("What does URL stand for?", "uniform resource locator"),
        ("What does SSD stand for?", "solid state drive"),
        ("What does OS stand for?", "operating system"),
        ("What does AI stand for?", "artificial intelligence")
    ]

    # Shuffle questions
    random.shuffle(question_list)

    for question, answer in question_list:
        questions += 1
        score = ask_question(question, answer, score, questions)

    print(f"\nYou got {score} out of {questions} questions correct!")
    print(f"Your percentage is {(score/questions * 100):.2f}%")

    # Scoreboard feature
    with open("scoreboard.txt", "a") as f:
        f.write(f"Score: {score}/{questions}, Percentage: {(score/questions * 100):.2f}%\n")
    
    print("Your score has been saved to scoreboard.txt.")

# Retry option
def main():
    while True:
        play_quiz()
        retry = input("\nDo you want to play again? (yes/no) ").lower()
        if retry != "yes":
            print("Thanks for playing! Goodbye...")
            break

if __name__ == "__main__":
    main()
