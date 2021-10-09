import os
import csv
os.chdir("C:\\UTSADBC\\python-challenge\\PyBank\\Resources")
csvpath = os.path.join('..', 'Resources', "budget_data.csv")
#Establish Variables 
month =[]
totalpro =[]
monthchange =[]
#Import CSV File with headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header =next(csvreader)
#Establish total months and total profit in a table   
    for row in csvreader:
        month.append(str(row[0]))
        totalpro.append(int(row[1]))
    TOTAL_M = len(month)
    TOTAL_P = sum(totalpro)
#Calulate Month Change and append to list   
    for x in range(len(totalpro)-1):
        monthchange.append(totalpro[x+1]-totalpro[x])  
#Calculate and print Average Change
MCPL= sum(monthchange)    
DENOM = len(monthchange)  
averagepl = MCPL/DENOM
# Record Greatest and Least amounts from monthchange list
Greatest = max(monthchange)
Least = min(monthchange)
#Find index position of min and max values
index = monthchange.index(Greatest)
index2 = monthchange.index(Least)
#Record Index in variable the table is one longer(nextmonth - previous) equals change
month_location1 = (month[index+1])
month_location2 = (month[index2+1])

#Print Table in terminal

print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {TOTAL_M}')
print(f'Total: ${format(TOTAL_P,",.0f")}')
print(f'Average Change: ${format(averagepl, ",.2f")}')
print(f'Greatest Increase: {month_location1} (${format(Greatest, ",.0f")})')
print(f'Greatest Decrease: {(month_location2)} (${format(Least,",.0f")})')           

#Send output to text file
f = open("PyBank.txt", "a")
print("Financial Analysis", file=f)
print("------------------------------------------", file=f)
print(f'Total Months: {TOTAL_M}', file=f)
print(f'Total: ${format(TOTAL_P,",.0f")}', file=f)
print(f'Average Change: ${format(averagepl, ",.2f")}', file=f)
print(f'Greatest Increase: {month_location1} (${format(Greatest, ",.0f")})', file=f)
print(f'Greatest Decrease: {(month_location2)} (${format(Least,",.0f")})', file=f)  
f.close()