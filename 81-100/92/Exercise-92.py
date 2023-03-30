def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as ze:
    print("You may not divide a number by ZERO!!")
except:
    print("Any other exception")