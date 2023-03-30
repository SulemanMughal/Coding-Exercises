prices = {"Strawberries" : 2.5, "Banana" : 1.5, "Mango" : 3.5,
"Blueberries" : 2, "Raspberries" : 3, "Apple" : 2.75,
"Pineapple" : 4.5}

class Smoothie:
    def __init__(self,ingredients):
        self.ingredients = ingredients
        self.cost = sum(prices[fruit] for fruit in self.ingredients)
        self.price = self.cost * 2.5
    def get_cost(self):
        return '${:.2f}'.format(self.cost)
    
    def get_price(self):
        return '${:.2f}'.format(self.price)
    
    def get_name(self):
        lst = sorted(i.replace('ies','y') for i in self.ingredients)
        return '{} {}'.format(' '.join(lst), 'Fusion' if len(lst)>1 else 'Smoothie')