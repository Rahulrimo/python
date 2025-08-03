cost_price =(int(input("Enter the cost price: ")))
selling_price=(int(input("Enter the selling price: ")))
if selling_price> cost_price:
    profit = selling_price - cost_price
    print("we have made a profit of:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("we have made a loss of:", loss)
else:
    print("There is no profit or loss")