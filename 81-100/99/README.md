# Exercise No. 99

Create a specialized exception that this module might raise on error, This needs to define an `__init__()` constructor that takes a a number, assumed to be meters, Implement `__str__` to give a string representation used by str() and print Implement a function, convert(string) that returns the value converted to 'feet', 'mm', 'inch' Implement a function to add two classes together and return the sum as a class 

**STRETCH:** Change the constructor so it can take a number and a string, 

**Example:**

    `l = Length(21.2, "inch")`

**STRETCH:** Change the function that adds two classes together to be more flexible so that it can add a number to a class Length returning a class Length.


**Example:**

    `l = Length(23)`
    
    `m = l + 21`