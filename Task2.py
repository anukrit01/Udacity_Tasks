"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_numbers = []
for number in texts:
	phone_numbers.append(number[0])
	phone_numbers.append(number[1])
for number in calls:
	phone_numbers.append(number[0])
	phone_numbers.append(number[1])

phone_numbers = list(set(phone_numbers))

# Getting the time spent of the calling and receiving phone numbers.
calling_time = {}
total_time = 0

for number in phone_numbers:
	for item in calls:
		if item[0] == number or item[1] == number:
			total_time += int(item[3])
			calling_time[number] = total_time		
	total_time = 0

longest_time_spent = max(calling_time.values())

# Print (longest_time_spent)
for key, value in calling_time.items():
	if value == longest_time_spent:
		print (key, "spent the longest time,", longest_time_spent, "seconds, on the phone during September 2016.")