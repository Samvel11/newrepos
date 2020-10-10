
import random
from heapq import nlargest

dictionary = {}
newdict = {}

class Homework:

	def __init__(self,word):
		self.word = word

	def dictionary(self):
		for i in self.word:
			dictionary[i] = random.randint(1,10)
		return(dictionary)

	def remove_(self):
		for key, value in dictionary.items():
			if value not in newdict.values():
				newdict[key] = value
		return(newdict)

	def max_3(self):
		maximum = nlargest(3,newdict, key = newdict.get)
		return(maximum)

word =  input("input a word\n")
example = Homework(word)

print("Dictionary ")
print(example.dictionary(),"\n")
print("without duplicates")
print(example.remove_(),"\n")
print("highest 3 values")
print(example.max_3())

