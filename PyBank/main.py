import os
import csv
import statistics

datafile = "budget_data.csv"


monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ''
greatestDecrease = 0
worstMonth = ''

change = []
monthToMonthChange = []

with open(datafile, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
         monthCount += 1
         totalVolume += int(row[1])
    
    if int(row[1]) > greatestIncrease:
            bestMonth = (row[0])
            greatestIncrease = int(row[1])
        
    elif int(row[1]) < greatestDecrease:
            worstMonth = (row[0])
            greatestDecrease = int(row[1])
            change.append(int(row[1]))

for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   

#Printing the final Results

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(monthCount))
print("Total: $" + str(totalVolume))
print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")


#Creating a text file with the analysis

f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(monthCount))
f.write("Total: $" + str(totalVolume))
f.write("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
f.write("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

