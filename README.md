# Object Oriented Programming

I'm learning object oriented programming and I will add here all programs that I develop during this learning.

## person.py and main.py files

The first two files are the *main.py*, which is the file in which we can apply call our classes and write code using them; and the *person.py*, in which I created the class **Person** to learn the basics of defining attributes and methods.

Example for using the class **Person**:
```
from person import Person

alex = Person('Alex',29,'male')
luana = Person('Luana',32,'female')
luna = Person('Luna',5,'female')

alex.talk('Physics')
luana.talk('English')
luna.talk('games')
alex.eat('lunch')
luana.eat('lunch')
luana.talk('movies')
```

## product.py file

The third file is the *product.py* file, in which I practice what I learned about ***getters*** and ***setters***.

Example for using the class **Product**:
```
from product import Product

prod1 = Product('First PRODUCT', '$50')
prod2 = Product('SeCoNd product', 1750)

prod1.discount(50)
prod2.discount(10)

print(prod1.name, prod1.price)
print(prod2.name, prod2.price)
<<<<<<< HEAD
```
=======
```
>>>>>>> 0e8ad0ca63c9224b343c97bd801838d0b4dc1a32
