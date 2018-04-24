# cs435 2018 spring section 002
# created by Jae Young Choi
# homework 1 part b
# january 30th 2018

import product

item1 = product.Product('001', '1 head of lettuce')
item2 = product.Product('002', '1 lb of tomatoes')
item3 = product.Product('003', '16 oz loaf of bread')

supermarket = [item1, item2, item3]

item1.setPrice(1.49)
item2.setPrice(1.99)
item3.setPrice(0.00)

basket = ['001', '002', '003', '999']

for i in supermarket:
    i.printInformation()
    print()

price = 0
def checkout(supermarket, basket):
    for x in supermarket:
        if x.outOfStock() == True:
            print(x.code, 'is out of stock.')
            
    for x in basket:
        if x != item1.code and x != item2.code and x != item3.code:
            print(x, 'is an unidentifiable product.')
            
    for x in supermarket:
        global price
        price += x.dollarAmount
            
checkout(supermarket, basket)
print(price)
    
