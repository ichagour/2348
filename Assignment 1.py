import datetime
import math

year = int(input("Enter the year you born:"))
month = int(input("Enter the month you born:"))
day = int(input('Enter the day you born:'))
current_year = int(input("Enter the current year:"))
current_month = int(input("Enter the current month:"))
current_day = int(input("Enter the current day:"))
birthday = month, day, year
current_date = current_month, current_day, current_year
print("Your birthday is: ", birthday)
print("The current date is:", current_date)
Age = current_year - year
print('Your Age',Age,'years old')
if current_month == month and current_day == day:
      print("Happy Birthday to You!")
else:
      print('Thank you')
