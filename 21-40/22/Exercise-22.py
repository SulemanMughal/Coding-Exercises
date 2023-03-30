matches = {'Bread': 'bag', 'Milk': 'bottle', 'Eggs': 'carton', 'Cereals': 'box', 'Candy': 'plastic'}


def get_container(product) :
    return matches.get(product)