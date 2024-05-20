
# TODO Class called order which store item and its price. Use dunder funct __gt__ to convey that:
# order1>order2 if price of order1 > price of order 2


class Oder:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __gt__(self,ord2):
        return self.price > ord2.price

ord1=Oder("chips",34)
ord2=Oder("chocolate",50)
print(ord1<ord2)
