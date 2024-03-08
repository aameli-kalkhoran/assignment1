#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2021
Program: assign1.py (replace student_id with your Seneca User name)
Author: "Amin Ameli Kalkhoran"
The python code in this file (assign1.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>
18773033013 
Date: 
'''


import sys

def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month, year):
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def after(today):
    day, month, year = map(int, today.split('-'))
    day += 1

    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    return f"{str(day).zfill(2)}-{str(month).zfill(2)}-{year}"

def before(today):
    day, month, year = map(int, today.split('-'))
    day -= 1

    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)

    return f"{str(day).zfill(2)}-{str(month).zfill(2)}-{year}"

def valid_date(date):
    try:
        day, month, year = map(int, date.split('-'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date, num_days):
    for _ in range(abs(num_days)):
        start_date = after(start_date) if num_days > 0 else before(start_date)
    return start_date

def usage():
    print("Usage: assign1.py DD-MM-YYYY NN")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    
    start_date, num_days_str = sys.argv[1], sys.argv[2]
    
    if not valid_date(start_date) or not num_days_str.lstrip('-').isdigit():
        usage()
    
    num_days = int(num_days_str)
    end_date = day_iter(start_date, num_days)
    
    print(f"The end date is {end_date}.")
