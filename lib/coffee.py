#!/usr/bin/env python3

class Coffee:
     # Initialize a new Coffee with size and price
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Add tip (increase price and show message)
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size (validates value, show message if invalid)
    @size.setter
    def size(self, value):
        if value != "Small" and value != "Medium" and value != "Large":
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price
    @price.setter
    def price(self, value):
        self._price = value
