def free_shipping(order):
    return sum(order.values())>=100