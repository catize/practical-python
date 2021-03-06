# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(file):
    portfoliovalue = 0.0


    p = open(file)
    rows = csv.reader(p)
    headers = next(p)


    #with open(file, 'rt') as p:
     #   headers = next(p)

    for row in rows:
        try:
            numshares = int(row[1])
            currprice = float(row[2])
        except ValueError:
            print('Shit value')
        portfoliovalue += numshares * currprice
    return portfoliovalue

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print('Total cost:', cost)
