#!/usr/bin/env python3

class Book:
    # Initialize a new Book with title and page_count
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Method to simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # Getter for title
    @property
    def title(self):
        return self._title

    # Setter for title
    @title.setter
    def title(self, value):
        self._title = value

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter for page_count (must be an integer)
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
