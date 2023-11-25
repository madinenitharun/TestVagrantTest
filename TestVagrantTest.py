class Product:
    def _init_(self, name, unit_price, gst, quantity):
        if unit_price >= 500:
            unit_price -= (0.05 * unit_price)
        self.name = name
        self.unit_price = unit_price
        self.gst = gst
        self.quantity = quantity

class Basket:
    def _init_(self, cart=[]):
        self.cart = cart

    def findMaximumGSTProduct(self):
        return max(self.cart, key = lambda x: (x.unit_price + (x.gst/100 * x.unit_price)) * x.quantity).name

    def addProduct(self, item):
        self.cart.append(item)

    def getTotalAmount(self):
        return sum((item.unit_price for item in self.cart))


n = int(input("Enter number of products:"))
basket = Basket()
for i in range(n):
    name = input("Enter Name of Product:")
    price = int(input("Enter the unit price:"))
    gst = float(input("Enter GST:"))
    quantity = int(input("Enter Quantity:"))
    basket.addProduct(Product(name, price, gst, quantity))

print(basket.findMaximumGSTProduct())
print(basket.getTotalAmount())