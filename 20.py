
import json
import requests
import threading

class Images():

	def __init__(self):
		print("class Images is created\n")


	def reader(self):
		with open("h20.json","r") as f:
			text  = json.load(f)
		text = text["items"]
		self.text = text
		return(text, "\n")

	def downloader(self):
		jpg_dict = {}
		png_dict = {}
		self.reader()
		for i in self.text:
			if i["url"].endswith("png"):
				png_dict[i["name"]] = i["url"]
			elif i["url"].endswith("jpg"):
				jpg_dict[i["name"]] = i["url"]
			else:
				pass

		# print(jpg_dict)
		# print("\n")
		# print(png_dict)	


		def jpeg(k):
			print(k)
			response = requests.get(jpg_dict[k])
			with open(f"{k}.jpg", "wb") as j:
				j.write(response.content)

		def png(url):
			print(url)			
			response = requests.get(png_list[url])
			with open(f"{url}.png", "wb") as j:
				j.write(response.content)

		for i in jpg_dict:
			x = threading.Thread(target = jpeg,args=(i,))
			x.start()	
				
		for i in png_dict:
			x = threading.Thread(target = png,args=(i,))
			x.start()	
				

a = Images()
# print(a.reader(), "\n")

a.downloader()

