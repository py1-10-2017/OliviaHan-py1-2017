class product(object):

    def __init__(self, price, item_name, weight, brand, status = 'for_sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        # self.display_info()

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        self.tax = tax
        whole_price = self.price * (1 + tax)
        return whole_price

    def return_item(self, reason):
        self.reason = reason
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0

        elif reason == 'new':
            self.status = 'for_sale'

        elif reason == 'used':
            self.status ='used'
            self.price = self.price * 0.8
        return self

    def display_info(self):
        print 'price:' + str(self.price)
        print 'Item' + str(self.item_name)
        print 'price:' + str(self.price)
        print 'weight:' + str(self.weight)
        print 'brand:' + str(self.brand)
        print 'status:' + str(self.status)


        return self


product1 = product(10, "eyeliner", "3 ounce", "lamer")

product1.sell().display_info().add_tax(0.1)
