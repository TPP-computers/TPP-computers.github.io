"""
Unit Standard 18740 Assessment - Program Code
Topic: Monthly Budget Calculator
Language: Python 3
Author: NSI Student
Date: [Current Date]
"""

def get_valid_number(prompt):
    """
    Sub procedure to ensure the user enters a valid number.
    Handles bad input (text) without crashing using try-except block.
    
    Parameters:
        prompt (str): The text displayed to the user asking for input.
        
    Returns:
        float: A valid positive number entered by the user.
    """
    while True:
        try:
            # Attempt to convert input to a floating point number
            amount = float(input(prompt))
            
            if amount < 0:
                print(">> Error: Amount cannot be negative.")
            else:
                return amount
                
        except ValueError:
            # This block catches errors if the user types text instead of numbers
            print(">> Error: Invalid input. Please enter a valid number (e.g., 25.50).")

def main():
    """
    Main function to orchestrate the budget calculation logic.
    Contains Variables, Sequence, Selection, and Repetition.
    """
    
    # Variable: Initialize total spending tracker
    total_spending = 0
    
    # Constant: Define a monthly budget limit for comparison later
    BUDGET_LIMIT = 500.00
    
    # Data Structure: List of categories to iterate through (Repetition)
    categories = [
        "Food", 
        "Transport", 
        "Entertainment", 
        "Clothing", 
        "Bills", 
        "Savings", 
        "Gifts", 
        "Miscellaneous"
    ]

    # Sequence: Program Introduction
    print("=" * 40)
    print("Welcome to the Monthly Budget Calculator")
    print(f"Your monthly budget limit is ${BUDGET_LIMIT}")
    print("=" * 40)
    
    # Repetition: Loop through each of the 8 categories
    for category in categories:
        
        # Sequence: Ask user for input for specific category
        prompt_text = f"How much did you spend on {category}? "
        
        # Call sub-procedure to get valid number (handles bad input)
        amount_spent = get_valid_number(prompt_text)
        
        # Variable Update: Add current expense to total
        total_spending += amount_spent
        
        print(f"  -> Recorded ${amount_spent:.2f} for {category}")

    # Sequence: Final Results Display
    print("\n" + "=" * 40)
    print("Budget Summary")
    print("=" * 40)
    
    # Selection (if/else): Compare total spending against the budget limit
    if total_spending > BUDGET_LIMIT:
        over_amount = total_spending - BUDGET_LIMIT
        print(f"Total Spent: ${total_spending:.2f}")
        print(">> Status: OVER BUDGET")
        print(f">> You are over by ${over_amount:.2f}")
    else:
        remaining = BUDGET_LIMIT - total_spending
        print(f"Total Spent: ${total_spending:.2f}")
        print(">> Status: WITHIN BUDGET")
        print(f">> You have ${remaining:.2f} remaining.")

if __name__ == "__main__":
    main()
