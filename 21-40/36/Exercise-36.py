def sweetest_icecream(lst):
    flavor_values = {
    'Plain' : 0,
    'Vanilla' : 5,
    'ChocolateChip' : 5,
    'Strawberry' : 10,
    'Chocolate' : 10
    }
    return max(i.num_sprinkles + flavor_values[i.flavor] for i in lst)