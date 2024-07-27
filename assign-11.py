"""
Problem 1:

create class Item
add instance properties
  name, price, quantity
create method calcualte_total_price
create method apply_discount
create method all_items

all items have 20% discount by default

# use these items and store it in items.csv
"Phone", 100, 1
"Laptop", 1000, 3
"Cable", 10, 5
"Mouse", 50, 5
"Keyboard", 75, 5

# read items.csv and create objects for each item
# I should be able to print all the items
"""

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
        
    def apply_discount(self):
        self.price = self.price * 0.8
        
    def all_items(self):
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"
    
items = [
    Item("Phone", 100, 1),
    Item("Laptop", 1000, 3),
    Item("Cable", 10, 5),
    Item("Mouse", 50, 5),
    Item("Keyboard", 75, 5)
]

for item in items:
    item.apply_discount()
    print(item.all_items())
    print(f"Total Price: {item.calculate_total_price()}")
    print()

# Problem 2:
# extend the above application restrict updating the price directly i.e item.price = 100

"""
Problem 3:

# extend the above application
# There are extra attributes in laptop i.e gpu, port_count and also it has 30% discount

# application folder structure
1. items.py
2. laptop.py
3. data/items.csv

# use this link if you are unable to create the assignment even after taking help on the group
# use this link only on the next saturday
Ref: https://www.youtube.com/watch?v=Ej_02ICOIgs
"""






