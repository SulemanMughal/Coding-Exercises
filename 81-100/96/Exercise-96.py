class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def compare_age(self, other):
        if other.age < self.age:
            s = 'younger than'
        elif other.age > self.age:
            s = 'older than'
        elif other.age == self.age:
            s = 'the same age as'
        return '{} is {} me.'.format(other.name,s)