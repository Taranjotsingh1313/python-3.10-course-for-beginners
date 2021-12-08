# GUESS THE NUMBER GAME
# IF ELSE STATEMENT IN PYTHON
# a = input()

# if a == "hello":
#     print("Hi")
# elif a == 'hi':
#     print("Hello")
# else:
#     print("You SHOULD TYPE HELLO ")
import random


while True:
    try:
        random_num = random.randint(1,10)
        a = int(input("ENTER YOUR NUMBER HERE BETWEEN 1 TO 10:\t"))
        if a == random_num:
            print(f"Number Was {random_num}")
            print("User Wins")
            break
        else:
            print(f"Number Was {random_num}")
            print("Computer Wins")
    except:
        random_num = random.randint(1,10)
        a = int(input("ENTER YOUR NUMBER HERE BETWEEN 1 TO 10:\t"))
        if a == random_num:
            print(f"Number Was {random_num}")
            print("User Wins")
            break
        else:
            print(f"Number Was {random_num}")
            print("Computer Wins")
