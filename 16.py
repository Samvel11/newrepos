
import random

class House_heating:
	current1 = random.randint(1,40)
	current2 = random.randint(1,40)
	current3 = random.randint(1,40)
	current4 = random.randint(1,40)


	def __init__(self,goal1, goal2,goal3,goal4):
		self.goal1 = goal1
		self.goal2 = goal2
		self.goal3 = goal3
		self.goal4 = goal4

	def __del__(self):
		print("Object is succesfully deleted")	


	def display(self):
		print(f"Room1:\t Current temperature  {self.current1}, goal temperature {self.goal1}")
		print(f"Room2:\t Current temperature  {self.current2}, goal temperature {self.goal2}")
		print(f"Room3:\t Current temperature  {self.current3}, goal temperature {self.goal3}")
		print(f"Room4:\t Current temperature  {self.current4}, goal temperature {self.goal4}")


	def fix(self):
		list1 = [self.current1,self.current2,self.current3,self.current4]
		list2 = [self.goal1,self.goal2,self.goal3,self.goal4]

		for i in range(0,4):
			if list1[i] != list2[i]:
				list1[i] = (int(list1[i]) + 2 * int(list2[i]))/3


		self.current1 = int(list1[0] + 0.5)
		self.current2 = int(list1[1] + 0.5)
		self.current3 = int(list1[2] + 0.5)
		self.current4 = int(list1[3] + 0.5)

		self.display()
		print("")


	def amount(self):
		list1 = [self.current1,self.current2,self.current3,self.current4]
		list2 = [self.goal1,self.goal2,self.goal3,self.goal4]
		amount = 0

		for i in range(0,4):
			if list1[i] == list2[i]:
				amount += 1

		print(amount, "houses have normal temperatures")		
	
	def __bool__(self):
		if self.current1 == self.goal1:
			check = True
		else:
			check = False
		return check	

		
a = House_heating(1,39,15,22)	
a.display()
a.fix()
a.amount()
# a.fix()
# a.amount()
# a.fix()
# a.amount()
# print(bool(a))



