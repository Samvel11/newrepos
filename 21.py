import logging
import random
import threading



logging.basicConfig(filename="numbers.log",level=logging.DEBUG,format="%(asctime)s %(message)s")

class Main():

	def __init__(self):
		list_ = []
		for i in range(50):
			number = random.randint(0,50)
			list_.append(number)
		self.list_ = list_
		print(list_)

	def Logg(self):
		for number in self.list_:
			if number >= 0 and number <= 9:
				logging.debug(f"Your number is {number}  and {number} in 0-9")
				print(f"DEBUG:\t Your number is {number} and {number} in 0-9 ") 
			elif number >= 10 and number <= 19:
				logging.info(f"Your number is {number} and  {number} in 10-19")
				print(f"INFO:\t Your number is {number} and {number} in 10-19")
			elif number >= 20 and number <= 29:
				logging.warning(f"Your number is {number} and {number} in 20-29")
				print(f"WARNING:  Your number is {number} and {number} in 20-29")
			elif number >= 30 and number <= 39:
				logging.error(f"Your number is {number} and  {number} in 30-39")
				print(f"ERROR:   Your number is {number} and {number} in 30-39")
			elif number >= 40 and number <= 50:
				logging.critical(f"Your number is {number} and  {number} in 40-49") 
				print(f"CRITICAL:   Your number is {number} and {number} in 40-49")


main = Main()
main.Logg()

