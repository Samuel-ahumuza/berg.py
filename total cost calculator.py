def calculate_total_price(item_price, quatity):
    item_total = item_price * quatity
    tax_rate = 0.07
    tax_amount = item_total * tax_rate
    total_price = item_total * tax_amount
    return total_price
    discount = 0.1
    discounted_price = total_price - (total_price * discount)
    return discounted_price
item_price = 25.0
quatity = 4
print ("Total_price:", calculate_total_price(item_price, quatity))