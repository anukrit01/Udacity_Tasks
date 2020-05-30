"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Creating an empty set
phone_nums = set()

for row in texts:
    phone_nums.add(row[0])
    phone_nums.add(row[1])

for row in calls:
    phone_nums.add(row[0])
    phone_nums.add(row[1])

count = len(phone_nums)
print("There are", count, "different telephone numbers in the records.")