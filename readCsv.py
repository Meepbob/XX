import csv

def readCsv(fileName):
    quotes = []
    with open(fileName, newline='') as csvFile:
        next(csvFile)
        reader = csv.DictReader(csvFile, [
            'date',
            'open',
            'high',
            'low',
            'close',
            'adjClose',
            'volume'
        ])

        for quote in reader:
            quotes.append(quote)

    return quote
