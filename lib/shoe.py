#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, condition="New"):
        self.brand = brand
        self.condition = condition

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
