def cyc_shift(x, steps):
    if steps < 0 :
        steps = abs(steps)
        for i in range(steps):
            x.append(x.pop(0)) 
    else:
        for i in range(steps):
            x.insert(0, x.pop())          


nums =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)
cyc_shift(nums, -2)
print(nums)
cyc_shift(nums, 3)
print(nums)