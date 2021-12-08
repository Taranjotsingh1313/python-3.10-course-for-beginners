# CALCULATOR USING STRUCTURAL PATTERN MATCHING
'''
    4 option : +,-,*,/
    two inputs from user
    perform action 
'''
# ESCAPE CAHARCTERS : \t--> space  \n--> new line
print("\tCALCULATOR USING PYTHON 3.10 (STRUCTURAL PATTERN MATCHING)")
print(" 1)ADDTION \n 2)SUBTRACTION \n 3)MULTIPLY \n 4)DIVIDE")

option = int(input('PLEASE CHOOSE ONE OPTION FROM ABOVE:\t'))

number1 = int(input("PLEASE ENTER THE FIRST NUMBER:\t"))
number2 = int(input("PLEASE ENTER THE SECOND NUMBER:\t"))


# STRUCTURAL PATTERN MATCHING
match option:
    case 1:
        print(f'ADDITION OF {number1} and {number2} = {number1 + number2} ')
    case 2:
        print(f'SUBTRACTION OF {number1} and {number2} = {number1 - number2} ')
    case 3:
        print(f'MULTIPLICATION OF {number1} and {number2} = {number1 * number2} ')
    case 4:
        print(f'DIVIDATION OF {number1} and {number2} = {number1 / number2} ')
    

# OPERATORS IN PYTHON
# ARITHMETIC OPERATORS :
# +
# -
# *
# /
# ASSIGNMENT OPERATORS:
