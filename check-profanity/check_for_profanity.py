"""Mini program to check a file for profanity"""

import urllib.request

def read_text():
	# Open content from file on my computer
	# quotes is an object/instance of File
	quotes = open("/home/lurial/src/build_programs/check-profanity/movie_quotes.txt")
	contents_of_file = quotes.read() # use the quotes object
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)


def check_profanity(text_to_check):
	# urllib - python module that helps get info from internet.
	# urlopen - function that takes in link to a website
	# The url is a profanity editor service
	# connection is anothe object/instance
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + urllib.parse.quote(text_to_check))
	output = connection.read().decode('UTF-8')
	print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document does not have curse words.")
	else:
		print("Could not scan the document properly.")

read_text()
