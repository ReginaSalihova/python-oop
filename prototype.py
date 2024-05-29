class Order:
    def __init__(self, order_number=None, products=None, total_price=None):
        self.order_number = order_number
        self.products = products if products is not None else []
        self.total_price = total_price

    def clone(self):
        return Order(self.order_number, self.products.copy(), self.total_price)

    def __str__(self):
        return f"Order Number: {self.order_number}, Products: {', '.join(self.products)}, Total Price: {self.total_price}"


class OrderPrototype:
    def __init__(self):
        self.prototype_order = Order()

    def set_order(self, order_number, products, total_price):
        self.prototype_order.order_number = order_number
        self.prototype_order.products = products
        self.prototype_order.total_price = total_price

    def clone(self):
        return self.prototype_order.clone()


prototype_order = OrderPrototype()
prototype_order.order_number = 1001
prototype_order.products = ["Product A", "Product B", "Product C"]
prototype_order.total_price = 150.00

# Создаем новый заказ на основе прототипа
order1 = Order(prototype_order.clone())
order1.order_number = 1002  # Изменяем номер заказа
order1.total_price = 200.00  # Изменяем общую сумму заказа

# Создаем еще один новый заказ на основе прототипа
order2 = Order(prototype_order.clone())
order2.order_number = 1003  # Изменяем номер заказа
order2.products.append("Product D")  # Добавляем новый товар

# Выводим информацию о заказах
print("Order 1:")
print("Order Number:", order1.order_number)
print("Products:", order1.products)
print("Total Price:", order1.total_price)

print("\nOrder 2:")
print("Order Number:", order2.order_number)
print("Products:", order2.products)
print("Total Price:", order2.total_price)
