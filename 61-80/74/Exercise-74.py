def profit(merchant_price, customer_price): 
    return str(round((customer_price - merchant_price) / customer_price*100,1))+'%' 


profit(50, 50)
profit(30, 70)
profit(20, 80)