def profit(info):
    return round((info["inventory"])*(info["sell_price"] - info["cost_price"]))


profit(({ "cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}))