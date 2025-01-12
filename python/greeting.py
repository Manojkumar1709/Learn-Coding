# Write a Python program to fetch the current time using the time module and print a greeting 
# (Mid Night, Good Morning, Good Afternoon, Good Evening, or Good Night) based on the time of day.

import time

timestamp = time.strftime('%H:%M:%S %p')
print("Current Time:", timestamp)

amorpm = time.strftime('%p')
hour = int(time.strftime('%I'))  


if amorpm == 'AM' and hour == 12:  
    print("Mid Night")
elif amorpm == 'AM' and 4 <= hour < 12:
    print("Good Morning")
elif amorpm == 'PM' and hour == 12:  
    print("Good Afternoon")
elif amorpm == 'PM' and 1 <= hour < 5:
    print("Good Afternoon")
elif amorpm == 'PM' and 5 <= hour < 7:
    print("Good Evening")
elif amorpm == 'PM' and 7 <= hour <= 11:
    print("Good Night")
