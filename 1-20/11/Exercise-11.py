

n = 30
def total_cups_cust(n):
    return n//6 + n


total_cups = total_cups_cust(n)

def total_cups_gets_free(total_cups):
    return round(total_cups/6, 0)


print(('Total cups for 30 days = ') + str(total_cups_cust(n)))
print(('Free cups in 30 days = ') + str(total_cups_gets_free(total_cups)))
n = 31
print(('Total cups for 31 days = ') + str(total_cups_cust(n)))
print(('Free cups in 31 days = ') + str(total_cups_gets_free(total_cups)))