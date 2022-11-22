def mobile_billing(call, data):
    pricecall = call * 2
    pricedata = data * 50
    price = pricecall + pricedata
    return price

def discount(amount):
    if amount <= 500:
        discounts = amount * 0.03
    elif amount <= 800:
        discounts = amount * 0.04
    elif amount <= 1000:
        discounts = amount * 0.05
    else:
        discounts = amount * 0.06
    return discounts

def vatable(amount):
    tax = amount * 0.07
    return tax