# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(file):
    portfoliovalue = 0.0


    p = open(file)
    rows = csv.reader(p)
    headers = next(rows)


    #with open(file, 'rt') as p:
     #   headers = next(p)

    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            numshares = int(record['shares'])
            currprice = float(record['price'])
            portfoliovalue += numshares * currprice
        except ValueError:
            print(f'Shit value in row {rowno}, value is {row} ')

    return portfoliovalue

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print('Total cost:', cost)
