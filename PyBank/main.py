import os
import csv

csvpath = os.path.join("resources", "budget_data.csv")
my_report = open(os.path.join('analysis','budget_analysis.txt'), 'w')

months = 0
total = 0
pre_rev = 0
total_ch = 0
inc = ["",0]
dec = ["",0]

with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=",")

    header = next(csv_reader)

    for row in csv_reader:

        # months = months + 1 
        months += 1

        rev = int(row[1])

        total += rev

        ch = rev - pre_rev

        if pre_rev == 0:
            ch = 0

        total_ch += ch

        if ch > inc[1]:
            inc[0] = row[0]
            inc[1] = ch

        if ch < dec[1]:
            dec[0] = row[0]
            dec[1] = ch


        pre_rev = rev


output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)



     