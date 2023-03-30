x = [10,20,30,40,50,60]
y = ['a','b','c','d','e','f']
z = {}
for i in range(len(x)):
    z[y[i]] = x[i]  
print (z)