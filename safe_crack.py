"""Use hill climbing to crack a lock combination."""

import time
from random import randint, randrange

def fitness(combo, attempt):
    """
    Compare items in two lists and count number of matches.
    
    Parameters:
    combo (list of int): The target lock combination as a list of digits.
    attempt (list of int): The current guess at the combination.
    
    Returns:
    int: The number of digits in the attempt that match the combo in the exact position.
    
    Explanation:
    This function evaluates how close the current guess (attempt) is to the actual combination (combo).
    It iterates through both lists simultaneously and increments a score (grade) for each matching digit
    in the same position. This score serves as a fitness measure for the hill climbing algorithm.
    """
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def main():
    """
    Enter lock combination & run hill climbing algorithm to find solution.
    
    Explanation:
    This function implements a simple hill climbing algorithm to guess the lock combination.
    It starts with an initial guess (all zeros), then iteratively mutates one digit at a time.
    If the mutation improves the fitness score (more digits match), it accepts the new guess.
    This process repeats until the guess matches the actual combination exactly.
    """
    combination = '6822858902'  # The secret lock combination as a string
    print("Combination = {}".format(combination))
    
    # Convert combination string to a list of integers for easier comparison
    combo = [int(i) for i in combination]

    # Initialize the best attempt with all zeros (worst guess)
    best_attempt = [0] * len(combo)
    # Calculate fitness score of the initial guess
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0  # Counter for number of attempts

    # Loop until the guess matches the combination exactly
    while best_attempt != combo:
        # Create a copy of the current best attempt to mutate
        next_try = best_attempt[:]
        
        # Randomly select one digit position to mutate (lock wheel)
        lock_wheel = randrange(0, len(combo))
        
        # Mutate the selected digit to a random number between 0 and 9
        next_try[lock_wheel] = randint(0, 9)
        
        # Calculate fitness score of the mutated guess
        next_try_grade = fitness(combo, next_try)
        
        # If the mutated guess is better (more matching digits), accept it
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        
        # Print the current mutated guess and the best guess so far for debugging
        print(next_try, best_attempt)
        
        count += 1  # Increment attempt counter

    # Once the combination is cracked, print the result and number of tries
    print()
    print("Cracked! {}" .format(best_attempt), end=' ')
    print("in {} tries!".format(count))

if __name__ == '__main__':    
    start_time = time.time()  # Record start time
    main()                    # Run the main hill climbing function
    end_time = time.time()    # Record end time
    duration = end_time - start_time  # Calculate total runtime
    
    # Print the runtime with 5 decimal places
    print("\nRuntime for this program was {:.5f} seconds.".format(duration))
