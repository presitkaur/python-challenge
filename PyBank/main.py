#Import dependencies and the csv file required for this analysis
import os 
import csv 
pybankxl = os.path.join('PythonHomework', 'python-challenge', 'PyBank', 'Resources', 'budget_data_pybank.csv')

#Create empty lists to hold the information provided in the columns of the csv file 
date = [] 
profitloss = [] 

#Read the csv and extract the infromation for analysis 
with open (pybankxl,encoding='UTF8') as csvfile: 
    budget_data = csv.reader(csvfile,delimiter=',')
    #the below variable is the header row in the csv. we can skip this as it is not useful
    csv_header = next(budget_data)
    for row in budget_data: 
        #information in the "date" column of the csv will be deposited into the list assigned as "date"
        date.append((row[0]))
        #information in the "profit/losses" column of the csv will be deposited into the list assigned as "profitloss"
        profitloss.append(int((row[1])))

#to calculate the total number of time periods we can find the length of the "date" list by using len(VAR)
totalmonths = len(date)

#a loop can be used to find the sum of all the values in the "profitloss" list to find the net total
    #create an inital empty variable with the value of 0
net = 0 
    #create a loop to provide a value for the above variable
for x in range(0, len(profitloss)):
    net = net + profitloss[x]

#the average change will be required for the next parts of the analysis 
#create a list variable to store the changes between successive values in the "profitloss" list 
change = []
#this loop will calculate the change between two values in the "profitloss" list
#and store that change in the "change" list
for y in range(len(profitloss)-1): 
    change.append(profitloss[y+1]-profitloss[y])
#average change can be found by finding the sum of all the values in the "change" list
#and then diving this number by the total length of the list 
average_change = (sum(change)/len(change))

#finding the max profit requires using the "max" function on the "change" list
max_profit = max(change)

#the corresponding date can be found by finding the index for the max value in the "change" list, 
#adding 1 to this number and then finding this index in the "date" list 
maxpm = change.index(max(change))+1 
max_profit_month = date[maxpm]

#the above can be repeated for the minimum 
min_profit = min(change)
minpm = change.index(min(change))+1
min_profit_month = date[minpm]

#the following will format the currency values to be divided into ones, tens, thousands etc
#and round them to two decimal values 
#it is not necessary however it increases readability
net_formatted = "{:,.2f}".format(net)
formatted_average_change = "{:,.2f}".format(average_change)
max_p_formatted = "{:,.2f}".format(max_profit)
min_p_formatted = "{:,.2f}".format(min_profit)

#the below will store our analysis findings into a variable called "final"
#this will make it easier to transport the infromation gathered into the analysis text file in the 
#analysis folder 
final = (
    f"------------------------------------------------------------ \n"
    f"                   PyBank Analysis \n"
f"------------------------------------------------------------ \n"
f"Total Date Periods:  {totalmonths} \n"
f"Net Total: $ {net_formatted} \n"
f"Average Change: $ {formatted_average_change} \n"
f"Greatest Increase in Profits: $ {max_p_formatted} during {max_profit_month} \n"
f"Greatest Decrease in Profits: $ {min_p_formatted} during {min_profit_month} \n"
f"------------------------------------------------------------- \n"
f"\n"
f"------------------------------------------------------------- \n"
)

#print the above into the output terminal
print(final)

#Export the analysis variable to the "analysis.txt" file 
finalfile = os.path.join("PythonHomework", "python-challenge", "PyBank", "Analysis", "analysis.txt")
with open(finalfile, "w") as file: 
    file.write(final)