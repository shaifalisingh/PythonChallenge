import os
import shutil
import csv

print("Financial Analysis")
print("---------------------")
input_file = open("budget_data_1.csv","r")
reader_file = csv.reader(input_file)
value = (len(list(reader_file))-1)
print("Total Months: ",value)

with open("budget_data_1.csv","r") as fh:
    headerline = next(fh)
    total = 0
    average = 0

    for row in csv.reader(fh):
    	# print(row[1])
    	total += int(row[1])
    average = (total / value)

max_value = max(row)
print("Total Revenue: $",total)
print("Average Revenue Change: $",average)

temp = open("budget_data_1.csv","r")
totaln = 0
maxt = 0
mint = 0

for line in temp:
    try:
        p = int(line.split(",")[1])
        totaln += 1
        if p > maxt:
            maxt = p
            maxdate = line.split(",")[0]
        if p < mint:
            mint = p
            mindate = line.split(",")[0]
    except:
        pass
print("Greatest Increase in Revenue:",maxdate,maxt)
print("Greatest Decrease in Revenue:",mindate,mint)


#Text file for the Output in the same folder as Code
with open('Output PyBank.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("-----------------\n")
    f.write("Total Months: {}\n".format(value))
    f.write("Total Revenue: {}\n".format(total))
    f.write("Average Revenue Change: $ {}\n".format(average))
    f.write("Greatest Increase in Revenue: {} \n".format(maxt))
    f.write("Greatest Decrease in Revenue: {} \n".format(mint))