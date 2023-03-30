def notbut():
    for num in range(1,1001):
        msg = ''
        if num % 3 == 0:
            msg += 'not'
        if num % 5 == 0:
            msg += 'but'
        if not msg:
            msg = str(num)
        print(msg)


