import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")
print(budget_data_csv)
row_count = 0
total_sum = 0
rcount = 0
tsum = 0
last_month_value = 0
total_change = 0
monthly_change = 0
PreValue = 0
Diff = 0
DiffMax = 0
DiffMin = 0

with open(budget_data_csv,'r') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    month = row[0]
    Amount = row[1]
    rowAmount = int(Amount)
    Diff = rowAmount-PreValue
    for row in reader:
        month_count=month_count+1
        
    first_row = next(reader)
    last_month_value = first_row[1]
    row_count += 1
    total_sum += int(first_row[1])

    for row in reader:
        if row_count!=0:
            total_change += int(row[1])-last_month_value
        rcount += 1   
        last_month_value = int(row[1])
print(f'Average change in P/L: $ {total_change/rcount}')

for row in reader:
    month=row[0]
    Amount = row[1]
    rowAmount = int(Amount)
    Diff=rowAmount-PreValue
    if DiffMax < Diff:
        DiffMax = Diff
        DiffMaxDate = month
    if DiffMin > Diff:
       DiffMin = Diff
       DiffMinDate = month
    PreValue = rowAmount
    
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
print(f'Greatest Increase in Loses: {DiffMinDate} : ($ {DiffMin})')