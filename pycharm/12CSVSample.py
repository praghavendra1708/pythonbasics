path = "./Google Stock Market Data - google_stock_data.csv"

lines = [line for line in open(path)]

print(lines[0])


import csv
#returns a stream
gfile = open(path,newline='')
reader = csv.reader(gfile)

header = next(reader)
print('The header of csv file is:', header )


