def operation(num1, num2):
    dd = {(num1+num2): 'added', (num1-num2): 'subtracted', (num1*num2): 'multiplied', (num1/num2): 'divided'}
    if 30 in dd.keys():
        return dd[30]
    else:
        return None