"""
Unit Standard 18740 Assessment - Program Code
Topic: Space Exploration Quiz
Language: Python 3
Author: NSI Student
Date: [Current Date]
"""

def get_valid_input(prompt):
    """
    Sub procedure to handle user input and bad input validation.
    It loops until the user provides a non-empty string.
    
    Parameters:
        prompt (str): The text displayed to the user asking for input.
        
    Returns:
        str: A valid, stripped string entered by the user.
    """
    while True:
        try:
            # Get raw input from user
            user_input = input(prompt)
            
            # Check if input is empty or just whitespace (Bad Input Handling)
            if not user_input.strip():
                print(">> Error: Input cannot be empty. Please type an answer.")
                continue
            
            return user_input.strip()
        except EOFError:
            # Handles cases where the user closes the terminal (Ctrl+D/Ctrl+C)
            print("\n\nEnd of input detected. Exiting program.")
            exit()

def check_answer(user_response, correct_response):
    """
    Sub procedure to compare answers case-insensitively.
    
    Parameters:
        user_response (str): The answer provided by the user.
        correct_response (str): The expected correct answer.
        
    Returns:
        bool: True if they match, False otherwise.
    """
    # Convert both to lowercase for comparison to handle case sensitivity
    return user_response.lower() == correct_response.lower()

def main():
    """
    Main function to orchestrate the quiz logic.
    Contains Variables (score), Sequence (flow of execution), 
    Selection (if/else), and Repetition (loop).
    """
    
    # Variable: Initialize score tracker
    user_score = 0
    
    # Data Structure: List of questions and answers
    # Using a list of dictionaries to store question data clearly
    quiz_data = [
        {"question": "Which planet is closest to the Sun?", "answer": "Mercury"},
        {"question": "What is the name of our galaxy?", "answer": "Milky Way"},
        {"question": "Who was the first person to walk on the Moon?", "answer": "Neil Armstrong"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "In which year did the Apollo 11 moon landing occur?", "answer": "1969"},
        {"question": "Which celestial body does Earth orbit around?", "answer": "Sun"},
        {"question": "What is the name of the first artificial satellite launched into space?", "answer": "Sputnik 1"}
    ]

    # Sequence: Program Introduction
    print("=" * 40)
    print("Welcome to the Space Exploration Quiz!")
    print(f"There are {len(quiz_data)} questions in total.")
    print("=" * 40)
    
    # Repetition: Loop through each question in the list
    for i, item in enumerate(quiz_data):
        current_question = item["question"]
        correct_answer = item["answer"]
        
        # Display Question Number and Text
        print(f"\nQuestion {i + 1}: {current_question}")
        
        # Call sub-procedure to get valid input (handles bad input)
        user_input = get_valid_input("Your Answer: ")
        
        # Selection: Check if the answer is correct
        if check_answer(user_input, correct_answer):
            print(">> Correct! Well done.")
            
            # Variable Update: Increment score
            user_score += 1
        else:
            print(f">> Wrong. The correct answer was '{correct_answer}'.")

    # Sequence: Final Results Display
    print("\n" + "=" * 40)
    print("Quiz Finished!")
    
    # Selection: Provide feedback based on score
    if user_score == len(quiz_data):
        print("Perfect Score! You are a space expert.")
    elif user_score > len(quiz_data) / 2:
        print("Good job! You know your stuff.")
    else:
        print("Keep learning about the universe!")

    # Display final score (Requirement: Keep track of score and display at end)
    print(f"Your Final Score: {user_score} out of {len(quiz_data)}")
    print("=" * 40)

# Entry point for the script
if __name__ == "__main__":
    main()
