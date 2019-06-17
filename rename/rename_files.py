# This program shows a secret message in a collection of files

import os


def rename_files():
	""" Get file names from a folder and rename each file. 

	All file names start with two-digit numbers. 
	Ex. 48sunnyvale.jpg

	Remove numbers from each file name to reveal a secret message 
	in the file folders. 

	"""



	# Get file names from the folder.
	file_list = os.listdir("/home/lurial/src/build_programs/rename/prank")
	# print(file_list)
	saved_path = os.getcwd()
	print(saved_path)
	os.chdir("/home/lurial/src/build_programs/rename/prank")
	# Rename each file.
	for file_name in file_list:
		# Rename function takes in the file name and what you want to change it to
		print("Old Name - " + file_name)
		translation_table = file_name.maketrans("0123456789", "          ", "0123456789")
		print("New Name - " + file_name.translate(translation_table))
		os.rename(file_name, file_name.translate(translation_table))

	os.chdir(saved_path)
		#string.translate(table, list of characters to remove)
		