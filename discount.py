def purchase(product,price):
    discount = 10
    tot = price - price*discount/100
    print("Total price of ", product , "is", str(tot))
    
purchase("iphone",70000)
