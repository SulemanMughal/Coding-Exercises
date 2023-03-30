def get_total_price(groceries):
    return round(sum([i['price'] * i['quantity'] for i in groceries]), 1)