import csv
csvfile1 = open ("iris_data.csv", "r")
lines1 = csv.reader(csvfile1)
dataSet1 = list(lines1)