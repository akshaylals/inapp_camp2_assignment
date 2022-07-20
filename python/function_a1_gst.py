# Assignment 1
# 
# Create a function to calculate the price after imposing GST on
# an Item
# The user will be giving the bare price of the item and its GST
# rate as input.
#  
# 1) CGST - Applicable GST Rate / 2 
# (eq: for 12%, CGST will be 12/2-6%)
# 
# 2) SGST = Applicable GST Rate / 2
# 
# The output should contain the following details
# Actual price of item
# Price after CGST
# Price after applying SGST
# Total price  

def gst(price, rate):
    priceCGST = price * (rate / 200)
    priceSGST = price * (rate / 200)
    priceTotal = price + priceSGST + priceCGST
    print('Price :', price)
    print('CGST :', priceCGST)
    print('SGST :', priceSGST)
    print('Price :', priceTotal)


price = float(input('Enter Price: '))
rate = float(input('Enter GST: '))
gst(price, rate)