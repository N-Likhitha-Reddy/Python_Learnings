#Implement a Python function that takes a date string in a specific format (e.g., "YYYY-MM-DD") as input and returns the corresponding day of the week (e.g., "Monday").
# Use the datetime module for date parsing and manipulation.

import datetime


def calculate_day(year, month, day):
    date_object = datetime.date(year, month, day)
    day_of_week = date_object.strftime("%A")
    return day_of_week


year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter date: "))

print("The day for {}-{}-{} is: {}".format(year, month, day, calculate_day(year, month, day)))