class Auto:
	def __init__(self, wheels, body):
		self.wheels = wheels
		self.body = body

	def drive(self):
		print("Не поеду!!")

tesla = Auto(2, True)
print(tesla.wheels)
print(tesla.body)
tesla.drive()

tesla.wheels += 2

oka = Auto(10, False)