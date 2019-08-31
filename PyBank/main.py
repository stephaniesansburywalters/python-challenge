import os
import csv

budget_data_CSV = os.path.join('budget_data.csv')

with open(budget_data_CSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    Profit_Losses = []
    Date = []
    Change = []

    for row in csvreader:

        Profit_Losses.append(int(row[1]))
        Date.append(row[0])

    for i in range(1,len(Profit_Losses)):
        Change.append(Profit_Losses[i] - Profit_Losses[i-1])   
        Average_Change = sum(Change)/len(Change)

        Max_PL_Change = max(Change)

        Min_PL_Change = min(Change)

        Max_PL_Change_Date = str(Date[Change.index(max(Change))])
        Min_PL_Change_Date = str(Date[Change.index(min(Change))])

    print("Financial Analysis")
    print("-----------------------------------")
    print(f'Total Months: {len(Date)}')
    print(f'Total: ${sum(Profit_Losses)}')
    print(f'Avereage Change: ${round(Average_Change)}')
    print(f'Greatest Increase in Profits: {Max_PL_Change_Date} (${Max_PL_Change})')
    print(f'Greatest Decrease in Profits: {Min_PL_Change_Date} (${Min_PL_Change})')

    f = open('Financial_Analysis.txt', 'w')
    print("Financial Analysis", file=f)
    print("-----------------------------------", file=f)
    print(f'Total Months: {len(Date)}', file=f)
    print(f'Total: ${sum(Profit_Losses)}',file=f)
    print(f'Avereage Change: ${round(Average_Change)}',file=f)
    print(f'Greatest Increase in Profits: {Max_PL_Change_Date} (${Max_PL_Change})', file=f)
    print(f'Greatest Decrease in Profits: {Min_PL_Change_Date} (${Min_PL_Change})',file=f)
    f.close()