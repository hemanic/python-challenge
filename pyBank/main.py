import os
import csv
bankcsv= os.path.join('Resources','budget_data.csv')
#total number of months in dataset
total=0
with open(bankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
         data = list(csvreader)
    row_count = len(data)
    print(row_count)
#net total of profits and losses
n = []
with open(bankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        for col in row[1]:
            n.append(int(row[1]))
        
sum(n)
total= sum(n)
print(total)
average= total/row_count
print(int(average))

###for some reason, getting very high numbers for the total and average, so greatest increase/decrease is thrown off too

minVal, maxVal = [], []
with open(bankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        for col in row[1]:
            minVal.append(int(row[1]))
            maxVal.append(int(row[1]))
    print min(minVal)
    print max(maxVal)
    
##lines 37 and 38 are gettin "invalid syntax" message but I've tried a few different methods and googled other functions to obtain min and max value but min(variable) and max(variable) are the only ones i've found

        