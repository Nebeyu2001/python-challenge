# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources","budget_data.csv")

output_path = os.path.join("analysis", "bank_anlysis.txt")

Total_months = 0

Net_total_amount= 0

change=0

previous = 0

avg_change=[]

inc=["",0]

dec=["",99999]

# open the CSV

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        Total_months= Total_months + 1 
        
        
        Net_total_amount= Net_total_amount + int(row[1])

        change= int(row[1])-previous

        avg_change.append(change)

        previous=int(row[1])

        if change > inc[1]:
            inc[0] = row[0]
            inc[1]= change
            #print(inc)

        if change < dec[1]:
            dec[0] = row[0]
            dec[1]= change
            #print(dec)
    avg_amount= sum(avg_change[1:])/(len(avg_change)-1)
    
    print(f"Total_months: {Total_months}")
    print(f"Net_total_amount: {Net_total_amount}")
    #print(f"avg_change:{avg_change}")
    print(f"avg_amount:{avg_amount}")
    #print(max(avg_change))
    #print(min(avg_change))
    print(inc)
    print(dec)



with open(output_path, 'w') as text_file:


    # Write the first row (column headers)
    text_file.write(f"Total_months: {Total_months}\n")
    text_file.write(f"Net_total_amount: {Net_total_amount}\n")
    text_file.write(f"avg_amount:{avg_amount}\n")
    #text_file.write(inc)
    #text_file.write(dec)
    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


      





