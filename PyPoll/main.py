import os 
import csv 
pypollxl = os.path.join("PythonHomework", "python-challenge", "PyPoll", "Resources", "election_data_pypoll.csv")


voterid = [] 
candidate_name = [] 


with open(pypollxl, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader)     
    for row in csvreader: 
        voterid.append((row[0]))
        candidate_name.append((row[2]))

from collections import Counter 
candidates = Counter(candidate_name).keys()

Khan = 0
Correy = 0 
Li = 0 
OTooley = 0 

#collecting the vote numbers for each candidate 
for x in range(len(candidate_name)):
    if candidate_name[x] == "Li":
        Li = Li + 1 
    elif candidate_name[x] == "Khan":
        Khan = Khan + 1 
    elif candidate_name[x] == "Correy":
        Correy = Correy + 1 
    else: 
        OTooley = OTooley + 1 

#Total number of votes cast 
total_votes = int((len(voterid)))

#number of votes list 
votes = [Khan, Correy, Li, OTooley]

#percentages 
khanp = (Khan/total_votes)*100 
correyp = (Correy/total_votes)*100 
lip = (Li/total_votes)*100 
otooleyp = (OTooley/total_votes)*100

#create a dictionary to extract the winner 
dictionary = dict(zip(candidates, votes))
winner = max(dictionary, key=dictionary.get)

#formatted values
khanp = "{:,.2f}".format(khanp)
correyp = "{:,.2f}".format(correyp)
lip = "{:,.2f}".format(lip)
otooleyp = "{:,.2f}".format(otooleyp)
total_votes = "{:,.2f}".format(total_votes)

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