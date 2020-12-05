# report.py
#
# Exercise 2.4

import csv
from typing import Dict, Any


def read_portfolio(portfoliofile):  # reads a portfolio and creates a list of tuples

    portfolio = []

    with open(portfoliofile, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)




                # portfolio[shares] = int(row[1])
                # portfolio[price] = float(row[2])

            # portfolio[line] = (headers[0], row[0], headers[1], int(row[1]), headers[2], float(row[2]))
            # portfolio[row[0]] = (int(row[1]), float(row[2]))
            # for name, shares, price in rows:
            # portfolio['shares'] = int(row[1])
            # portfolio['price'] = float(row[2])
            # portfolio[row[0]] = [int(row[1]), float(row[2])]
            # for name, shares, price in rows:
            # portfolio = (row[0], int(row[1]), float(row[2]))
            # portfolio.append(holding)
    return portfolio


def read_prices(pricefile):  # reads prices and creates a dict

    prices = {}

    with open(pricefile, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices



def make_report(portfolio, prices):

    summary = []
    total_change = 0.0

    for stock in portfolio:
        current_price = prices[stock['name']]
        change_stock = current_price - stock['price']
        change_share = change_stock * stock['shares']
        line = (stock['name'], stock['shares'], current_price, change_stock, change_share)
        summary.append(line)
        total_change += change_share

    headers = ('Name', 'Shares', 'Price', 'Change by Stock', 'Change by Share')
    print(f'%10s %10s %10s  %10s  %10s' % headers)
    print(f'%10s %10s %10s  %10s  %10s' % (('_' * len(headers[0])), ('_' * len(headers[1])), ('_' * len(headers[2])), ('_' * len(headers[3])), ('_' * len(headers[4]))))
    for name, shares, price, change_stock, change_share in summary:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f}$ {change_stock:>15.2f} {change_share:>15.2f}$')
    print(f'Your total loss/gain is ${total_change:0.2f}')

    return summary, total_change





#portfolio = read_portfolio(portfoliofile)
#prices = read_prices(pricefile)