def sum_of_evens(m):

    return sum(i for i in sum(m, []) if i%2 == 0)


sum_of_evens(([
    [1, 0, 2],
    [5, 5, 7],
    [9, 4, 3]
]))