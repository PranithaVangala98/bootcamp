def order_item(product, quantity, /, price, discount=0):
    total = (price * quantity) * (1 - discount)
    print(
        f"Product: {product}, Quantity: {quantity}, Price: {price}, Discount: {discount}, Total: {total}"
    )


order_item("Laptop", 2, price=1000, discount=0.1)  # Works fine
