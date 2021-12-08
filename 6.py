# ERROR HANDLING IN PYTHON

# TRY AND EXCEPT BLOCK USED FOR HANDLING ERROR IN PYTHON

# print(a/b)
try:
    a = input()
    b = int(input())
    print(a/b)
except Exception as e :
    print(e)
    print("PLEASE DONT GIVE 0 IN SECOND NUMBER")

print("hello world")