from abc import ABC,abstractmethod
class Payment:
    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Payment Credit Card Payment of {amount}")

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing of Cash Payment {amount}")
    
def process_payment(order_amount,payment_method:Payment):
    payment_method.process_payment(order_amount)

#base class functionality shodule not be broken 
credit_payment = CreditCardPayment()
cash_payment = CashPayment()
process_payment(500,credit_payment)
process_payment(500,cash_payment)