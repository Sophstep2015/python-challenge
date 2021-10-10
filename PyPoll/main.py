import os
import csv
from collections import Counter

#Set Directory
os.chdir("C:\\UTSADBC\\python-challenge\\PyPoll\\Resources")
csvpath = os.path.join('..', 'Resources', "election_data.csv")

#Establish list for Candidates 
candid = []

# Create name variables
Name1 = ("Khan")
Name2 = ("Correy")
Name3 = ("Li")
Name4 = ("O'Tooley")

#Import CSV File with headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        candid.append(str(row[2]))

    # Reference Count of All Candidates & Winner       
    counts = Counter(candid)
    winner = (counts.most_common(1)[0][0])

    # Count each Candidate 
    Count1 = (counts['Khan'])  
    Count2 = (counts['Correy'])
    Count3 = (counts['Li'])
    Count4 = (counts["O'Tooley"])
    totalvotes = len(candid)

    #Calculate Percentages 
    per1 = ((Count1/totalvotes * 100))
    per2 = ((Count2/totalvotes * 100))
    per3 = ((Count3/totalvotes * 100))
    per4 = ((Count4/totalvotes * 100))

    #Print Results Table in Terminal

    print("Election Results")
    print("------------------------------")
    print(f'Total Votes: {totalvotes}')
    print("------------------------------")
    print(f'{Name1}: {format(per1, ",.3f")}% ({Count1})')
    print(f'{Name2}: {format(per2, ",.3f")}% ({Count2})')
    print(f'{Name3}: {format(per3, ",.3f")}% ({Count3})')
    print(f'{Name4}: {format(per4, ",.3f")}% ({Count4})')
    print("------------------------------")
    print(f'Winner: {winner}')
    print("------------------------------")

    #Print to text file 
    os.chdir("C:\\UTSADBC\\python-challenge\\PyPoll\\Analysis")
    f = open("PyPoll_output.txt", "a")
    print("Election Results", file=f)
    print("------------------------------", file=f)
    print(f'Total Votes: {totalvotes}', file=f)
    print("------------------------------", file=f)
    print(f'{Name1}: {format(per1, ",.3f")}% ({Count1})', file=f)
    print(f'{Name2}: {format(per2, ",.3f")}% ({Count2})', file=f)
    print(f'{Name3}: {format(per3, ",.3f")}% ({Count3})', file=f)
    print(f'{Name4}: {format(per4, ",.3f")}% ({Count4})', file=f)
    print("------------------------------", file=f)
    print(f'Winner: {winner}', file=f)
    print("------------------------------", file=f)
    f.close()














