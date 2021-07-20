# To get current date and time
# we need the datetime library
from datetime import datetime,timedelta

current_date = datetime.now()
# the now fxn returns a datetime object
print("Today's date is: " + str(current_date))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday's date was: " + str(yesterday))

one_week = timedelta(weeks=1)
last_week = current_date - one_week
print ("Last week was " + str(last_week))

# Printing date to screen
print("Day: " + str(current_date.day))
print("Month: " + str(current_date.month))
print("Year: " + str(current_date.year))

print("Hour: " + str(current_date.hour))
print("Month: " + str(current_date.minute))
print("Year: " + str(current_date.second))

# formatting date
birthday = input("Enter your birthday (dd/mm/yyyy): ")
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print("Birthday " + str(birthday_date))