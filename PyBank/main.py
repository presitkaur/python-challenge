import os 
import csv 
pybankxl = os.path.join('PythonHomework', 'python-challenge', 'PyBank', 'Resources', 'budget_data_pybank.csv')


date = [] 
profitloss = [] 

with open (pybankxl,encoding='UTF8') as csvfile: 
    budget_data = csv.reader(csvfile,delimiter=',')
    csv_header = next(budget_data)
    for row in budget_data: 
        date.append((row[0]))
        profitloss.append(int((row[1])))

totalmonths = len(date)

net = 0 
for x in range(0, len(profitloss)):
    net = net + profitloss[x]

change = []
for y in range(len(profitloss)-1): 
    change.append(profitloss[y+1]-profitloss[y])
average_change = (sum(change)/len(change))

max_profit = max(change)
maxpm = change.index(max(change))+1 
max_profit_month = date[maxpm]

min_profit = min(change)
minpm = change.index(min(change))+1
min_profit_month = date[minpm]

net_formatted = "{:,.2f}".format(net)
formatted_average_change = "{:,.2f}".format(average_change)
max_p_formatted = "{:,.2f}".format(max_profit)
min_p_formatted = "{:,.2f}".format(min_profit)

final = (
    f"------------------------------------------------------------ \n"
    f"                   PyBank Analysis \n"
f"------------------------------------------------------------ \n"
f"Total Months:  {totalmonths} \n"
f"Net Total: $ {net_formatted} \n"
f"Average Change: $ {formatted_average_change} \n"
f"Greatest Increase in Profits: $ {max_p_formatted} in {max_profit_month} \n"
f"Greatest Decrease in Profits: $ {min_p_formatted} in {min_profit_month} \n"
f"------------------------------------------------------------- \n"
)

print(final)

finalfile = os.path.join("PythonHomework", "python-challenge", "PyBank", "Analysis", "analysis.txt")
with open(finalfile, "w") as file: 
    file.write(final)