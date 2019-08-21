# Reading file csv noramlly
path = "./Google Stock Market Data - google_stock_data.csv"

csvFile = open(path, newline='')
lines = [line for line in csvFile]

print("header of file is:", lines[0].split(","))
print("The first line of data is", lines[1].split(","))


from datetime import datetime
def fun(cols):
    """Converts string into list of values"""
    return [ datetime.strptime(cols[0], '%m/%d/%Y'), float(cols[6]) ]

import csv
csvFile = open(path, newline='')
csvReader = csv.reader(csvFile)

print("Printing the header:", next(csvReader))
csvLines = [fun(line)  for line in csvReader]
for line in csvLines:
    print("line is:", line[0], line[1])

#print("Header of file is", csvLines[0])


# Calcualting the avg change and writing to a file
path = './output.csv'
writer = open(path,'w')
output_writer = csv.writer(writer)
output_writer.writerow(['Date', 'Returns'])
for i in range(1, len(csvLines)-1):
    present_day = csvLines[i+1][0].strftime('%d-%m-%Y')
    val_cal = (csvLines[i+1][1] - csvLines[i][1])/csvLines[i][1] * 100
    output_writer.writerow([present_day, val_cal])






