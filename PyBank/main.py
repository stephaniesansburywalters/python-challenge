import os
import csv

budget_data_CSV = os.path.join('budget_data.csv')

# Define the function and have it accept the 'budget_data' as its sole parameter
def simple_analysis(metrics):
    Date = str(metrics[0])
    Profits_Losses = int(metrics[1])
    
    print (f"Date: {date}, P/L: {Profits_Losses}")

with open(budget_data_CSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader: