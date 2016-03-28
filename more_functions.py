def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    my_price = price + 10000
    print "my_price (inside function) = ", my_price
    return total


