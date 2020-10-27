# Create a class, which has
# a method which reads a text file and takes all the rows(image links) as attributes of self.image_list
# a method which make request to downloads jpeg image
# a method which make request to downloads png image
# extensions: try to create last two methods in a different class to use polymorphism.
# Ex class Image_jpeg:
# 	def download()
# class Image_png:
# 	def download()


import requests

class Images:

	def __init__(self):
		print("class Images is created")


	def method(self):
		self.image_list = []
		with open("text.txt","r") as file:
			for i in file.readlines():
				self.image_list.append(i)
		return(self.image_list)


	# def download_jpeg(self,url):
	# 	response = requests.get(url)
	# 	if response.status_code == 200:
	# 		with open("first.jpeg", 'wb') as f:
	# 			f.write(response.content)				


	# def download_png(self,url):
	# 	response = requests.get(url)
	# 	if response.status_code == 200:
	# 		with open("second.png", 'wb') as f:
	# 			f.write(response.content)		


	def download_jpeg(self):

		with open ("text.txt","r") as text:
			for line in text.readlines():
				list_ = line.split(" ")

				for i in list_:
					with open ("second.jpeg","wb") as file:
						response = requests.get(f"{i}")
						file.write(response.content)
		print("picture is downloaded successfully")	


	def download_png(self):

		with open ("text.txt","r") as text:
			for line in text.readlines():
				list_ = line.split(" ")

				for i in list_:
					with open ("second.png","wb") as file:
						response = requests.get(f"{i}")
						file.write(response.content)
		print("picture is downloaded successfully")				

				

# extensions

class Image_jpeg:
	def __init__(self,url):
		self.url = url

	def download(self):
		response = requests.get(self.url)
		with open("pict.jpeg", 'wb') as f:
			f.write(response.content)
		print("finish")	


class Image_png:
	def __init__(self,url):
		self.url = url

	def download(self):
		response = requests.get(self.url)
		with open("pict.png", 'wb') as f:
			f.write(response.content)
		print("finish")	



a = Images()
# print(a.method())			
# a.download_jpeg("http://craphound.com/images/1006884_2adf8fc7.jpg")
# a.download_png("http://craphound.com/images/1006884_2adf8fc7.jpg")

a.download_jpeg()
a.download_png()

b = Image_jpeg("http://www.httpbin.org/image/jpeg")
b.download()

c = Image_jpeg("http://www.httpbin.org/image/jpeg")
c.download()