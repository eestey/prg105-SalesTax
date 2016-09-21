print ("Enter the price for each item.")


item1 = float(raw_input("Enter price of item 1 = $"))
print item1
item2 = float(raw_input("Enter price of item 2 = $"))
print item2


cost = (item1 + item2)
print ("Subtotal = $" + str(cost))


salesTax = cost * 0.06
print ("Sales Tax = $" + str(salesTax))

totalAmount = (cost + salesTax)

print ("The total comes out to = $" + str(totalAmount))
