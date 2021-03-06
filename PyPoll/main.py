#import dependencies 
import os 
import csv 
pypollxl = os.path.join("PythonHomework", "python-challenge", "PyPoll", "Resources", "election_data_pypoll.csv")

#Declare list variables for applicable rows of the original data csv file 
voterid = [] 
candidate_name = [] 

#Collect the information from the csv provided and deposit it into the appropriate list variables 
with open(pypollxl, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader)     
    for row in csvreader: 
        voterid.append((row[0]))
        candidate_name.append((row[2]))

#Find the unique candidates by importing Counter
from collections import Counter 
candidates = Counter(candidate_name).keys()
#running "print(candidates)" will allow us to see the list of unique candidates 
#as this is only a short list, we can use the following code 

#Create empty numeric variables for each candidate
Khan = 0
Correy = 0 
Li = 0 
OTooley = 0 

#collecting the vote numbers for each candidate by using a for loop and a conditional statement
for x in range(len(candidate_name)):
    if candidate_name[x] == "Li":
        Li = Li + 1 
    elif candidate_name[x] == "Khan":
        Khan = Khan + 1 
    elif candidate_name[x] == "Correy":
        Correy = Correy + 1 
    else: 
        OTooley = OTooley + 1 

#compile the above into a list so that it can later be zipped into a dictionary 
# @NOTE it is very important that it is in the same order as within the "candidates" list 
votes = [Khan, Correy, Li, OTooley]

#Total number of votes can be found by running the below 
total_votes = int((len(voterid)))

#calculate the percentages for each candidate
khanp = (Khan/total_votes)*100 
correyp = (Correy/total_votes)*100 
lip = (Li/total_votes)*100 
otooleyp = (OTooley/total_votes)*100

#create a dictionary to extract the winner 
dictionary = dict(zip(candidates, votes))
winner = max(dictionary, key=dictionary.get)

#optional: format values so that they are easier to read 
khanp = "{:,.2f}".format(khanp)
correyp = "{:,.2f}".format(correyp)
lip = "{:,.2f}".format(lip)
otooleyp = "{:,.2f}".format(otooleyp)
total_votes = "{:,.2f}".format(total_votes)

#the below will store our analysis findings into a variable called "final"
#this will make it easier to transport the infromation gathered into the analysis text file in the 
#analysis folder 
final = (
    f"------------------------------------------------------------ \n"
    f"                   PyPoll Analysis \n"
    f"------------------------------------------------------------ \n"
    f"Total votes: {total_votes} \n"
    f"------------------------------------------------------------ \n"
    f"Khan: {Khan:,.2f} ({khanp}%) \n"
    f"Correy: {Correy:,.2f} ({correyp}%) \n"
    f"Li: {Li:,.2f} ({lip}%) \n"
    f"O'Tooley: {OTooley:,.2f} ({otooleyp}%) \n"
    f"------------------------------------------------------------ \n"
    f"                      Winner: {winner} \n"
    f"------------------------------------------------------------ \n"
)
print(final)

#Export the analysis variable to the "analysis.txt" file 
finalfile = os.path.join("PythonHomework", "python-challenge", "PyPoll", "Analysis", "analysis.txt")
with open(finalfile, "w") as file: 
    file.write(final)