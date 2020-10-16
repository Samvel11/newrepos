
class Hotel:

	def __init__(self,hotel_name,place,mid_room,mid_room_price, lux_room, lux_room_price):
		self.hotel_name = hotel_name
		self.place = place
		self.mid_room = mid_room
		self.mid_room_price = mid_room_price
		self.lux_room = lux_room
		self.lux_room_price = lux_room_price

	def HotelPresentation(self):
		print(f"{self.hotel_name} hotel\nPlace: {self.place}\n"
			f"Middle rooms: \t {self.mid_room}\nPrice:\t\t {self.mid_room_price}\n"
			f"Lux rooms: \t {self.lux_room}\nPrice:\t\t{self.lux_room_price}")

	def booking(self):
		
		print("\nfree Middle rooms")
		c = []
		for key,value in self.mid_room.items():
			if value == "free":
				c.append(key)
				print(key)
		print("\n""Rooms price")		
		for j in c:
			print(j," - ",self.mid_room_price[j])	
		
		print("\nfree Lux rooms")
		d = []
		for key,value in self.lux_room.items():
			if value == "free":
				d.append(key)
				print(key)
		print("\n""Rooms price")		
		for j in d:
			print(j," - ",self.lux_room_price[j])
		print("\n")	


		while True:
			try:
				question = input("Which room do you want to book?\n")

				if question not in c and question not in d:
					raise Exception("Which room do you want to book? Enter room name")
				break

			except Exception as ex:
				print(ex)	

		if question in c:
			print(f"Thank you for choosing this hotel")
			self.mid_room[question] = "reserved"
			# print(self.mid_room)
		elif question in d:
			print(f"Thank you for choosing this hotel")
			self.lux_room[question] = "reserved"
		

	def available_room_check(self,type_):

		if type_  == "middle room" or type_ == "middle":
			print("\nfree Middle rooms")
			c = []
			for key,value in self.mid_room.items():
				if value == "free":
					c.append(key)
					print(key)
			print("\n""Rooms price")		
			for j in c:
				print(j," - ",self.mid_room_price[j])

		elif type_ == "lux" or type_ =="lux room":	
			print("\nfree Lux rooms")
			d = []
			for key,value in self.lux_room.items():
				if value == "free":
					d.append(key)
					print(key)
			print("\n""Rooms price")		
			for j in d:
				print(j," - ",self.lux_room_price[j])
			print("\n")		

		else:
			print("incorrect type of room")


	def discount(self,percent):	
		for key, value in self.mid_room_price.items():
			self.mid_room_price[key] = value - value * (percent/100)

		for key, value in self.lux_room_price.items():
			self.lux_room_price[key] = value - value * (percent/100)	

		print("Discounted price")
		print("\nmiddle rooms")
		for i in self.mid_room_price:
			print(i,self.mid_room_price[i])
		print("\nluxury rooms")	
		for i in self.lux_room_price:
			print(i,self.lux_room_price[i])


		

class Taxi:

	def __init__(self,t_name,car_types,price_for_tour):
		self.t_name = t_name
		self.car_types = car_types
		self.price_for_tour = price_for_tour


	def Taxi_presentation(self):	
		print(f"{self.t_name} taxi provides {self.car_types} cars and price for it is {self.price_for_tour}")

	def discount(self,percent):
		self.price_for_tour = self.price_for_tour * (1 - 0.01 * percent)
		print("Discounted price of taxi is  ", self.price_for_tour)


class Tour(Hotel,Taxi):

		def __init__(self,name,hotel_name,place,mid_room,mid_room_price, lux_room, lux_room_price,t_name,car_types,price_for_tour):
			self.name = name
			Hotel.__init__(self,hotel_name,place,mid_room,mid_room_price, lux_room, lux_room_price)
			Taxi.__init__(self,t_name,car_types,price_for_tour)
			
		def presentation(self):

			min_ = min(self.mid_room_price.values())
			max_ = max(self.lux_room_price.values())
			print(f" Welcome to the {self.name} tour\n",
			 	f"We offer you spend your vacation in {self.hotel_name} hotel which is located in {self.place} \n",
			 	f"It includes transport with {self.t_name} company which provides {self.car_types} cars\n",
			 	 "Price for hotel:  ", f"{min_} - {max_} " ,"\n Price for taxi - ", self.price_for_tour,  "\n Discounts for two or more people" )
			
			min_ = min(self.mid_room_price.values())
			max_ = max(self.lux_room_price.values())





a = Hotel("Marriott","Tsaxkadzor",{"room1":"free","room2":"free","room3":"reserved"},
	{"room1":15000,"room2":18000,"room3":20000},{"room4":"free","room5":"reserved","room6":"free"},{"room4":30000,"room2":30000,"room6":35000})
b = Taxi("Yandex","Nissan",500)
c = Tour("Armenia Travel","Marriott","Tsaxkadzor",{"room1":"free","room2":"free","room3":"reserved"}, {"room1":15000,"room2":18000,"room3":20000},
		{"room4":"free","room5":"reserved","room6":"free"},{"room4":30000,"room2":30000,"room6":35000},"Yandex","Nissan",500)


# a.HotelPresentation()	
# a.booking()	
# a.available_room_check("middle")
# a.discount(30)
# b.Taxi_presentation()
# b.discount(20)
# c.presentation()