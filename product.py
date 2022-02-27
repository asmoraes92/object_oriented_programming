class Product:
	def __init__(self, name, price, sold=False):
		self.name = name
		self.price = price
		self.sold = sold

	def discount(self, percentage):
		self.price = self.price - (self.price*percentage/100)

	#getter
	@property
	def price(self):
		return self._price

	#setter
	@price.setter
	def price(self, value):
		if isinstance(value, str):
			value = float(value.replace('$',''))
		self._price = value

	#getter
	@property
	def name(self):
		return self._name

	#setter
	@name.setter
	def name(self, value):
		value = value.title()
		self._name = value

	def sell_product(self):
		self.sold = True