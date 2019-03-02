from readCsv import readCsv

fileName = 'dji.csv'

stocks = readCsv(fileName)

for stock in stocks:
    print("Date: " + stock['date'] + " Adj Close: " + stock['adjClose'])
