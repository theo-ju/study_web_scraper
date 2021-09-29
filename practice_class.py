class Car():

	def __init__(self, **kwargs):
		self.wheels = 4
		self.doors = 4
		self.windows = 4
		self.seats = 4
		self.color = kwargs.get('color', 'black')
		self.price = kwargs.get('price', '$20')

	def __str__(self):
		return f'Car with {self.wheels} wheels'


class Convertible(Car):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)  # Class 상속
		self.time = kwargs.get('time', 20)

	def __str__(self):
		return f'Car without roof'

	def take_off():
		return 'taking off'


porche = Car(color='green', price='$20')


mini = Car()
print(mini.price, mini.color)

