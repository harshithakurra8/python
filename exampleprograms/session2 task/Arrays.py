#Arrays 

#Objective: Create and manipulate arrays with a real-world example. 

#Concept: Inventory Management System for a Store. 

#Tasks: 

#Initialize an array of product prices. 

#Perform insertion and deletion operations to add/remove products. 

#Implement a search function to find a product price. 

#Search for products in array with same prices existing more than n/3 times using while-loop. 

#Use list comprehensions to filter products above a certain price. 

products=["phone","laptop","Speaker","wifi","bluetooth"]

product_prices = [15.59, 18.49, 5.99, 3.46, 9.69]

product_prices.append(25.79)             #Insert a product

product_prices.remove(5.99)              #Delete a product

class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price


class Inventory_management():
    def __init__(self):
        self.products = []
        self.stock = [] 

    def search_product_price(product_name, prices):
        try:
            index = products.index(product_name)                             #Search tht product price
            return prices[index]
        except ValueError:
            return "Product not found"
    print(search_product_price("laptop", product_prices))

def find(prices, n):
    counts = {}
    for price in prices:
        counts[price] = counts.get(price, 0) + 1

    result = []
    i = 0
    while i < len(prices):
        price = prices[i]                                         #Search for products in array with same prices existing more than n/3 times. 

        if counts[price] > len(prices) / 3 and price not in result:    
            result.append(price)
        i += 1

    return result
print(find(product_prices, 3))

expensive_products = [price for price in product_prices if price > 8.00]           #filter products above certain price
print(expensive_products)

