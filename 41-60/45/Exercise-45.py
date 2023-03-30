def pizza_points(customers, min_orders, min_price):
    return sorted([k for k, v in customers.items() if sum(1 for i in v if i >= min_price) >= min_orders])