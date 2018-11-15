# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name =name
        self.products = []
      

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        print("------------------")
        print("%s:" % self.name)
        
        for x in self.products :
          print(x)
          print()
          


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name 
        self.description = description
        self.price = price

    def __str__(self):
        return "(\tProduct Name: %s,\n\tDescription: %s,\n\tPrice: %d)" % (self.name,self.description,self.price)
       

class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.cart = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        
        self.cart.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0
        for i in self.cart:
            total += i.price

        return total
            
        

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("your total price is: KD %s" % self.get_total_price() )

    def checkout(self):
        """
        Does the checkout.
        """
        print("________________")
        self.print_receipt()
        y = input("confirm ?(yes/no) ")
        while y.lower() != "no" and y.lower() != "yes" :
              x = input()

        if  y.lower() == "no" :
           print("Your order has been cancelled")
        elif y.lower() == "yes" :
           self.cart = []
           print("Your order has been placed")
