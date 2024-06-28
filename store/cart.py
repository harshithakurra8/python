class Cart:
      _instance=None
def __new__(cls):
   if cls._instance is None:
      print("creating new instance")
      cls._instance=super().__new__(cls)
      cls._instance._init()
   return cls._instance
def _init(self):
   self.products=[]
def add_product(self,product):
   self._products.append(product)