# class Text(object):  # karanq grenq def__init__(self,age) u 10rd toxum grenq Text(568)

# 	def __init__(self):
# 		self.name = input("tell smthing\n")


# 	def printing(self):
# 		print(self.name)

# my_object = Text()
# my_object.printing()		



# my_object2 = Text()




class triangle:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def makeres(self,):
		s = self.a + self.b + self.c
		print(s)

erankyun = triangle(6,8,12)	
erankyun.makeres()	 

		
# def rem_dub(self):
# 	d = {}

# 	for i in self.dict1:
# 		if self.dict_1[i] not in d.value():
# 			d[i] = self.dict_1[i]

# 	self.dict_1 = d
	
# def max_3(self):
# 	list_1 = list(self.dict_1.values())
# 			



class Vehicle:

	def __init__(self,seats):
		self.seats = seats

class Car(Vehicle):
	def __init__(self,name,color,seats):
		self.name = name
		self.color = color
		Vehicle.__init__(self,seats)


bmw = Car("bmw","red",9)

print(bmw.name, bmw.color, bmw.seats)		


class bysicle(Vehicle):

	def __init__(self,mass,country,seats):
		self.mass = mass
		self.country = country
		Vehicle.__init__(self,seats)

bsc = bysicle("20","Germany",9)
print(bsc.mass, bsc.country,bsc.seats)		