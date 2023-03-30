x = [2, 5, 10, 25, 17, 30, 44]

while True:
    i = input("ID: ")
    if i == 's':
        break
    try:
        i = int(i)
        print(x[i])
    except ValueError:
        print('user input should be an integer')
    except IndexError:
        print('no item with such index = ', i)