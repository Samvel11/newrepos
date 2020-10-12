
import math

class Circle:
	def __init__(self,radius):
		self.radius = radius

	def parametr(self):
		p = 2 * math.pi * int(self.radius)
		print(p) 

	def area(self):
		s = math.pi * int(self.radius)**2
		print(s)

a = input("enter the radius\n")
shrjan = Circle(a)
print("parametr", end = "\t")
shrjan.parametr()	
print("area", end = "\t\t")	
shrjan.area()


# 2

class Class:

	def __init__(self,list_,target):
		self.list = list_
		self.target = target

	def function(self):
		a = list(self.list)
		c = []

		for i in a:
			for j in a:
				if  i + j == self.target and self.list.index(i) != self.list.index(j):
					
					b = {i,j}
					if b not in c:
						print(f"Numbers  {i}, {j}")
						c.append(b)
						
				

a = Class([10,20,10,40,50,60,70],50)	
a.function()				



# # 3RD

class Person:
	def __init__(self, name,age,country):
		self.name = name
		self.age = age
		self.country = country

class Student(Person):
	def __init__(self,name,age,university,proffesion,country):
		self.university = university
		self.proffesion = proffesion
		Person. __init__(self,name,age,country)


Bob = Student("Bob",19,"YSU","physicist","Brazil")	

print("name") 
print(Bob.name) 

print("age")
print(Bob.age)

print("university")
print(Bob.university)


print("Bob.proffesion")
print(Bob.proffesion)

print("Bob.country")
print(Bob.country)
