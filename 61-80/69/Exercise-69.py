def sum_digits(*n):
    return sum(int(i) for i in str(sum(n)))


def carry_digits(n1, n2):
    return (sum_digits(n1) + sum_digits(n2) - sum_digits(n1, n2)) // 9