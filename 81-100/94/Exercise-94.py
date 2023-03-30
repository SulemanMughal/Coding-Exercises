try:   
    f = open("python.txt") 
except:   
    print("Something went wrong when try to open the file") 
finally:   
    f.close()