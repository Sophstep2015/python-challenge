import os
import csv
from collections import Counter

os.chdir("C:\\UTSADBC\\python-challenge\\PyPoll\\Resources")
csvpath = os.path.join('..', 'Resources', "election_data.csv")
#Import CSV File with headers

candid = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header =next(csvreader)
    
    for row in csvreader:
        candid.append(str(row[2]))

# Reference Count of all candidates       
counts = Counter(candid)
win = (counts.most_common(1))

# Count each Candidate 
KhanCount = (counts['Khan'])  
CorreyCount = (counts['Correy'])
LiCount = (counts['Li'])
Otooleycount = (counts["O'Tooley"])
totalvotes = len(candid)

#Calculate Percentages 
kper = ((KhanCount/totalvotes * 100))
cper = ((CorreyCount/totalvotes * 100))
lper = ((LiCount/totalvotes * 100))
oper = ((Otooleycount/totalvotes * 100))

#Print Results Table 
print("Election Results")
print("------------------------------")
print(f'Total Votes: {totalvotes}')
print("------------------------------")
print(f'Khan: {format(kper, ",.3f")}% ({KhanCount})')
print(f'Correy: {format(cper, ",.3f")}% ({CorreyCount})')
print(f'Li: {format(lper, ",.3f")}% ({LiCount})')
print(f'OTooley: {format(oper, ",.3f")}% ({Otooleycount})')
print("------------------------------")
print(f'Winner: {win} ')