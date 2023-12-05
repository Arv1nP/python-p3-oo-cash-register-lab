#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.items.append({"title": title, "price": price, "quantity": quantity})
        
        

    def apply_discount(self):
      if self.discount is None:
          print("There is no discount to apply.")
      else:
        discount_amount = (self.discount / 100) * self.total
        discounted_total = self.total - discount_amount
        self.total = discounted_total
        print(f"After the discount, the total comes to ${int(discounted_total)}.")

    def reset_total(self):
        self.total = 0
      
      
    



