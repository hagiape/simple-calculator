# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

operation = ''
first_number = ''
second_number = ''
result = ''
print('Welcome to a simple calculator program')
try:
    while True:
        operation = input('"+" for addition\n"-" for subtraction\n"x" for multiplication\n"/" for division\nWhat operation would you like to be performed? ')
        first_number = input('What is the first number? ')
        second_number = input('What is the second number? ' )
        match operation:
            case '+':
                result = int(first_number) + int(second_number)
            case '-':
                result = int(first_number) - int(second_number)
            case '*':
                result = int(first_number) * int(second_number)
            case '/':
                result = int(first_number) / int(second_number)
            case _:
                raise Exception('Please enter only the mentioned operators.')
        print(result)
        prompt_answer = input('Would you like to perform another calculation?\n(answer with "yes" or "no" only:' )
        prompt_answer.lower()
        if prompt_answer == 'no':
            print('Thank you for using the program!')
            break
        else:
            if prompt_answer != 'yes':
                raise Exception('Please answer with "yes" or "no" only.')
except ZeroDivisionError:
    print('You cannot divide by zero!')
except ValueError:
    print('The calculator only accepts integers as input.')