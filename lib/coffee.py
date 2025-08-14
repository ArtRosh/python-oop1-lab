#!/usr/bin/env python3

class Coffee:

    def __init__(self, size, price):
        self.size = size
        self.price = price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value != "Small" and value != "Medium" and value != "Large":
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
