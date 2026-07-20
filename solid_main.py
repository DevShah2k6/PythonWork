class Order:
    def __init__(self,products):
        self.products = products

    def calculate_total(self):
        pass
    def get_order_item(self):
        pass
#here process p[ayment is not related to the order class so siong;e reposniblity shoudle be
# there
    def process_payment(self):
        pass
class PaymentProcesser:
    def __init__(self,order):
        self.order=order
    def process_payment(self):
        pass

products=["item1","item2"]

orders = Order(products)
orders.calculate_total()
#for payment i have created the new class
payment=PaymentProcesser()
payment.process_payment()