"""Prompts user to take a break every two hours."""

import webbrowser
import time

total_breaks = 3
break_count = 0

# ctime is current time
print("This program started on "+ time.ctime())
while break_count < total_breaks:
	# This measures in seconds and sleep suspends program for that amount of time
	# Set sleep timer for 2 hours/7200 seconds
	time.sleep(7200) 
	webbrowser.open("https://www.youtube.com/watch?v=Ob7vObnFUJc")
	break_count += 1