# Function for the simple calculator that handles basic operations
def simpl_calc():
    while True:
        # Display operation choices
        print("\nChoose your operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")  # Instead of back, prompt to choose again

        simpl_choice = input("\nChoose your desired operation (1/2/3/4/5): ")

        # Perform the selected operation
        if simpl_choice == '1':
            # Take two numbers as input from the user
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            c = a + b
            print("The result of addition is:", c)

        elif simpl_choice == '2':
            # Take two numbers as input from the user
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            c = a - b
            print("The result of subtraction is:", c)

        elif simpl_choice == '3':
            # Take two numbers as input from the user
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            c = a * b
            print("The result of multiplication is:", c)

        elif simpl_choice == '4':
            # Take two numbers as input from the user
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            try:
                # Attempt to divide the numbers
                c = a / b
                print("The result of division is:", c)
            except ZeroDivisionError:
                # Handle division by zero
                print("Error: Division by zero is not allowed!")

        elif simpl_choice == '5':
            calculator()
        else:
            # Invalid input case
            print("Invalid choice! Please select a valid operation.")

# Function for the multi-operational calculator that handles complex expressions
def mul_calc():
    while True:
        print("\nYou can enter a complex arithmetic expression (e.g., 5 + 3 * 2 - 8 / 4).")
        print("1. Enter a new expression")
        print("2. Back to Main Menu")

        choice = input("Choose an option (1/2): ")

        if choice == '2':
            # Go back to the main menu
            return

        elif choice == '1':
            expression = input("Enter the expression: ")

            try:
                # Evaluate the entered expression
                result = eval(expression)
                print("The result is:", result)
            except Exception as e:
                # Handle invalid expressions or other errors
                print(f"Error: {e}. Please enter a valid expression.")
        else:
            print("Invalid choice! Please select a valid option.")

# Main calculator function to provide a menu for selecting between simple or multi-operational calculators
def calculator():
    while True:
        # Display the main menu options
        print("\n1. Simple operational calculator")
        print("2. Multi-operational calculator")
        print("3. Exit")

        choice = input("Choose the type of calculator you want (1/2/3): ")

        if choice == '1':
            # Run the simple calculator
            simpl_calc()
        elif choice == '2':
            # Run the multi-operational calculator
            mul_calc()
        elif choice == '3':
            # Exit the program
            print("Exiting the calculator. Goodbye!")
            break
        else:
            # Handle invalid input for the main menu
            print("\nInvalid input! Please choose again.")

# Run the calculator program
calculator()
