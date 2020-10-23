
import os

base_dir = os.getcwd()
print("we are now in  {}".format(base_dir))


os.makedirs(F"{base_dir}/current/dir1/dir2/../dir3/dir4")

while True:
	try:
		a = input("Input the dir which you want to delete\n")

		if a == "dir4":
			os.rmdir((F"{base_dir}/current/dir1/dir3/dir4"))
			print("dir4 successfully deleted")

		elif a == "dir3":

			os.rmdir((F"{base_dir}/current/dir1/dir3/dir4"))
			os.rmdir((F"{base_dir}/current/dir1/dir3"))
			print("dir3 successfully deleted")
			
		elif a == "dir2":
			os.rmdir((F"{base_dir}/current/dir1/dir2"))
			print("dir2 deleted")

		elif a == "dir1":
			os.rmdir((F"{base_dir}/current/dir1/dir3/dir4"))
			os.rmdir((F"{base_dir}/current/dir1/dir3"))
			os.rmdir((F"{base_dir}/current/dir1/dir2"))
			os.rmdir(F"{base_dir}/current/dir1")	
			print("dir1 deleted")


		else:
			raise Exception("Input the dir which you want to delete\n")	
		break

	except Exception as error:
		print(error)		


def file_deleter:
	
	os.remove((F"{base_dir}/current/file.txt")
	print("file.txt is deleted") 



