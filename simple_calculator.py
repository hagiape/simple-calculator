# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

# implemented code from Stack Overflow
# https://stackoverflow.com/a/20757225
# function that creates text border based on the output
def border(string):
    text = string.splitlines()
    max_length = max(len(s) for s in text)
    column_width = max_length + 2
    print('+' + ('-' * column_width) + '+')
    for s in text:
        print('| %-*.*s |' % (max_length, max_length, s))
    print('+' + ('-' * column_width) + '+')

operation = ''
first_number = ''
second_number = ''
result = ''
prompt_answer = ''
print('Welcome to a simple calculator program')
try:
    while True:
        operation = input('"+" for addition\n"-" for subtraction\n"x" for multiplication\n"/" for division\nWhat operation would you like to be performed? ')
        first_number = input('What is the first number? ')
        second_number = input('What is the second number? ')
        if '.' in first_number or second_number:
            first_number = float(first_number)
            second_number = float(second_number)
        else:
            first_number = int(first_number)
            second_number = int(second_number)
        match operation:
            case '+':
                result = first_number + second_number
            case '-':
                result = first_number - second_number
            case '*':
                result = first_number * second_number
            case '/':
                result = first_number / second_number
            case _:
                raise Exception('Please enter only the mentioned operators.')
        border('The answer is: ' + str(result))
        prompt_answer = input('Would you like to perform another calculation?\nanswer with "yes" or "no" only: ' )
        prompt_answer = prompt_answer.lower()
        if prompt_answer == 'no':
            print('Thank you for using the program!')
            break
        elif prompt_answer != 'yes':
                raise Exception('Please answer with "yes" or "no" only.')
except ZeroDivisionError:
    print('You cannot divide by zero!')
except ValueError:
    print('The calculator only accepts numbers as input.')