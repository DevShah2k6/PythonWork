class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def apply_discount(self,discount_strategy):
        return discount_strategy.apply(self.price)
        # if discount_strategy=="seasonal":
        #     return self.price*0.9
        # elif discount_strategy=="clearnace":
        #     return self.price*0.7
        
#here probvlem is ther if some discunt value is chnaged then evrey time we ewnat to chnage it here so 
# we can make the seperate classes for each disocunt type

class SeasonalDisocunt:
    def apply(self,price):
        return price*0.9



class ClearnaceDisocunt:
    def apply(self,price):
        return price*0.7
        
product = Product(name="fevicol",price=240)
print(product.apply_discount(SeasonalDisocunt()))
