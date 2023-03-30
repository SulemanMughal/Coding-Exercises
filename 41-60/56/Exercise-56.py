def transform(x):
    new_x = []
    for i in x:
        if i % 2 == 0:
            new_x.append(i - 1)
        else:
            new_x.append(i + 1)
    return new_x



transform([1, 2, 3, 4, 5])