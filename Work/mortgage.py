# mortgage.py
#
# Exercise 1.7
import math

principal = 660000.0
rate = 0.014
payment = 2300
total_paid = 0.0
month = 1
extra_payment_start_month = int(input('Start Month of Extra Payment (enter a number)'))
extra_payment_end_month = int(input('End Month of Extra Payment (enter a number)'))
extra_payment = int(input('Extra Payment Amount'))

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

        if principal < (payment + extra_payment):
            break
    year = int(math.ceil(month/12))
    print(f'In month {month} (year {year}) you paid ${total_paid:0.0f}. Remaining dept is ${principal:0.0f}')
    month += 1

    if principal < payment:
        break



print(f'You paid a total of {total_paid:0.0f}. It took you {year} years.')
