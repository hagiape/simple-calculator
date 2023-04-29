# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

# initialize public variables
operation = ''
first_number = ''
second_number = ''
result = ''
print('Welcome to a simple calculator program.')
# try block
try:
# while loop
    while True:
# ask operation to be used from user
        operation = input('"+" for addition\n"-" for subtraction\n"x" for multiplication\n"/" for division\nWhat operation would you like to be performed? ')
# first number = input
        first_number = input('What is the first number? ')
# second number = input
        second_number = input('What is the second number?' )
# perform operation if else
        match operation:
        # if +:
            case '+':
                # add two variables
                result = int(first_number) + int(second_number)
        # if -:
            case '-':
                # subtract two varibles
                result = int(first_number) - int(second_number)
        # if *:
            case '*':
                # multiply two variables
                result = int(first_number) * int(second_number)
        # if /:
            case '/':
            # divide two variables
                result = int(first_number) / int(second_number)
# display output
        print(result)
        # ask if user wants to try again
        prompt_answer = input('Would you like to perform another calculation?\n(answer with "yes" or "no" only:' )
        prompt_answer.lower()
            # if yes
            # if no break loop
        if prompt_answer == 'no':
            # print 'Thank you'
            print('Thank you for using the program!')
            break
            # if neither yes or no, break loop
        # raise exception 'please answer only yes or no'
        else:
            if prompt_answer != 'yes':
                raise Exception('Please answer with "yes" or "no" only.')
# implement except block
except ZeroDivisionError:
    print('You cannot divide by zero!')