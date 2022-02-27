from product import Product

prod1 = Product('First PRODUCT', '$50')
prod2 = Product('SeCoNd product', 1750)

prod1.discount(50)
prod2.discount(10)

print(prod1.name, prod1.price)
print(prod2.name, prod2.price)