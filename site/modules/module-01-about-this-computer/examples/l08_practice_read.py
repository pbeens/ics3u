price = 89.99
copy = price
price = price * 2
print(price, copy)
print(id(price) == id(copy))
