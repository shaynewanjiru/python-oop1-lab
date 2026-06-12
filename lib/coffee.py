#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = input("The size of coffee available is either Small, Medium or Large. your chosen size is: ")
        self.price = int(input("Please enter the price of the coffee: "))

    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, value):    
        if value in ["Small", "Medium", "Large"]:
            self._size = value
            print(f"You chose a {value} size coffee")
        else:
            print("size must be small, medium, or large") 
            self._size = None

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1




        
    
    