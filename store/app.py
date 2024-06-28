from store.cart import  Cart
from store import Product

cart= Cart()
cart.add_product(Product("Earbud",6.75))
cart.add_product(Product("mouse",3.99))
cart2=Cart()
cart2.show()



