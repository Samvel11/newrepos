class Country:
	def __init__(self,Cname,continent):
		self.continent = continent
		self.Cname = Cname

	def text(self):
		print(F"{self.Cname} is a country in {self.continent}")

class Brand:
	def __init__(self,brand_name,date):
		self.brand_name = brand_name
		self.start_date = date

	def method(self):
		print(f"{self.brand_name} start date is {self.start_date}")

class Season:
	def __init__(self,Season_name,average_temperature):
		self.Season_name = Season_name
		self.average_temperature = average_temperature

	def presentation(self):
		print(f"In {self.Season_name} the average_temperature is {self.average_temperature}")


class Product(Country,Brand,Season):
	def __init__(self,name,type_,price,quantity,Cname,brand_name,Season_name,continent,date,average_temperature):
		self.pr_name = name
		self.type = type_
		self.price = price
		self.quantity = quantity
		Country.__init__(self,Cname,continent)
		Brand.__init__(self,brand_name,date)
		Season.__init__(self,Season_name,average_temperature)

	def product_present(self):
		print(f"Product name - {self.pr_name}")
		print(f"Country - {self.Cname}")
		print(f"Brand - {self.brand_name}")
		print(f"Price - {self.price}")
		print(f"Quantity - {self.quantity}")

	def discount(self,percent):	
		newprice = self.price - (self.price * percent)/100
		print(f"Product price with {percent} percent is {newprice} ")

	def increase_quantity(self):
		if self.Season_name == "summer" or self.Season_name == "spring":
			self.quantity += 0.5 * self.quantity

		print("The available quantity of a product - ",self.quantity)	


Italy = Country("Italy","Europe")		
Beretta = Brand("Beretta",1800)
summer = Season("summer",35)
Beretta950 = Product("Beretta950","m9",500,2500,"Italy","Beretta","summer","Europe",1800,35)

Italy.text()
Beretta.method()
summer.presentation()
print("")

Beretta950.product_present()
print("")

Beretta950.discount(30)
Beretta950.increase_quantity()




