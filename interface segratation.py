class ProductManager:
    def list_products(self):
        pass
    def update_stock(self):
        pass

class StockManger():
    def update_stock(self,product_id,quantity):
        pass
class ProductListing(ProductManager):
    def list_products(self):
        print("Listing Product")
    def update_stock(self):
      raise NotImplemented("Stock Management not required for listing")
    
class ProductStockManager(StockManger):
    def update_stock(self, product_id, quantity):
        print("Updating stock for product")