# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.a.com"  

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    print("........................")
    for i in stores: 
      print(i.name)
      
def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for i in stores:
        if i.name.lower() == store_name.lower():
            return i
    return False



def pick_store():
    store_found = False
    while not store_found:
        print_stores()
        store_name = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
        if store_name.lower() == "checkout":
            return "checkout"
        picked_store = get_store(store_name)
        if picked_store:
            break

        print("No store with that name. Please try again.")

    return picked_store

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
   
    pr = input("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above type \"back\" to go back to the main menu or \"checkout\" to pay your bills \n" )
   
    while pr.lower() != "back" and pr.lower() != "checkout"  :
        for product in picked_store.products:
            if pr.lower() == product.name.lower():
                cart.add_to_cart(product)
        pr = input()
  
    return pr

  


def shop():
    cart = Cart()
    pr = ""
    while pr.lower() != "checkout":
        pr = ""
        picked_store = pick_store()
        if picked_store == "checkout":
            break
     
        pr = pick_products(cart, picked_store)

    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
