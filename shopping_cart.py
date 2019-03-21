#Update your shopping_cart.py file to include an init method. This should define three default attributes: 'total', which should be set to 0, 'employee_discount', set to None and 'items', set to a blank list. The line of code below should work and produce the previewed output once you do this.

class ShoppingCart:
    
    def __init__(self, total = 0, employee_discount=None):
        self.total = 0
        self.employee_discount = employee_discount
        self.items = []
      
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({'name' : name, "price" : price})
        self.total += price * quantity
        return self.total

#Define two more instance methods: mean_item_price and median_item_price, which should return the average price per item and the median price of the items in your cart, respectively.
    def mean_item_price(self):
        return self.total / len(self.items)
    
    def get_items(self):
        return self.items

    def median_item_price(self):
        item_list = []
        for item in self.items:
            item_list.append(item["price"])
            sorted_list = sorted(item_list)
        n = len(item_list)
        if n % 2 == 1: 
            median = sorted_list[n // 2]
        else:
            median = sum(sorted_list[n//2-1:n//2+1]) / 2
        return median

#Now, let's define an instance method called apply_discount that applies a discount if one is provided and returns the discounted total. For example, if we initialize a new shopping cart with a discount of 20% then our total should be discounted in the amount of 20%. So, if our total were $100, after the discount we only would owe $80.

#If our shopping cart does not have an employee discount, then it should return a string saying: "Sorry, there is no discount to apply to your cart :("
 
    def apply_discount(self):
        if self.employee_discount:
            discount_price = (1 - (self.employee_discount / 100)) * self.total
            return discount_price
        else:
            return "Sorry, there is no discount to apply to your cart :("

        #Finally, we are missing one piece of functionality. What if we just accidentally added something to our cart or decided that this item is too expensive for our budget? Let's define a method called void_last_item that removes the last item from our shopping cart and updates its total. If there are no items in the shopping cart, void_last_item should return "There are no items in your cart!".
    
    def void_last_item(self):
        if self.items:
            self.total -= self.items[-1]["price"]
            self.items.pop()
        else:
            return "There are no items in your cart!"