from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self,payment:Payment):
        pass
class CreditCard:
    def process_payment(self,amount):
        print("Processing Payment")
    def process_payment(self,amount):
        print("Payment Done")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Processing Payment")


class PaypalPayment(Payment):
    def process_payment(self, amount):
        print("Paypal Payment processing")
class OrderProcessor:
      def __init__(self,payment:Payment):
          self.payment=payment
          pass
      def update_stock(self, product_id, quantity):
        print("Updating stock for product")
      
      def process_order(self,amount):
           self.payment.process_payment(amount)

# here if payment chnages then i have chnges the method so it is toight coupled so

orderprocessor  =OrderProcessor(PaypalPayment())
credit  =OrderProcessor(CreditCard())
credit.process_order(456)