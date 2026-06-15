def purchase(product,price):
    discount = 10
    tot = price - price*discount/100
    print("Total price of ", product , "is", str(tot))
    
purchase("iphone",70000)

"""Consider the below code which allows you to purchase different products. All products have discount of 10%.

Run the below code and observe the output."""
