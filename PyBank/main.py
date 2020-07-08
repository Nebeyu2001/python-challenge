# Modules
import os
import csv

# set path for file to read and then to write our output
csvpath = os.path.join("Resources","budget_data.csv")

output_path = os.path.join("analysis", "bank_anlysis.txt")

#initialize the starting value into 0
Total_months = 0

Net_total_amount= 0

change=0

previous = 0

# creat an empty list to fill later
avg_change=[]

# To find the greatest increase in profits,with the corresponding month, creating a list, with zero as first profit value
inc=["",0]


# To find the greatest decrease in losses,with the corresponding month,creating a list, with random high number to compare
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

        # counting each month row by row in the CSV
        Total_months= Total_months + 1 
        
        # adding the total amount row by row, changing the string value of profits and losses(index[1])
        Net_total_amount= Net_total_amount + int(row[1])

        # the change of profits/losses between the previous month and the curruent one 
        change= int(row[1])-previous

        # put the changes in am empty list to calculate the average change later
        avg_change.append(change)
        
        # resets the previous value
        previous=int(row[1])

        # The greaetst increase in profits means the "greatest change" , using indexes we get both month and profits 
        # if the current change is higher than the previous, then it resets the value of change, till it finds the greatest in the entire period
        if change > inc[1]:
            inc[0] = row[0]
            inc[1]= change
            #print(inc)

        
        # the greatest decrease in losses means the "lowest change", using indexes gets both month and profits
        # if the current change is lower than the previous,then it resets the value of change till it finds the lowest change in the list
        if change < dec[1]:
            dec[0] = row[0]
            dec[1]= change
            #print(dec)


     # calculates the average amount of changes by adding all changes in the list divided by the lenght of list, excluding the first value which isnot a change from perious value,       
    avg_amount= sum(avg_change[1:])/(len(avg_change)-1)


    # final outputs after looping through every row starting from the top excluding header
    
    print(f"Total_months: {Total_months}")
    print(f"Net_total_amount: ${Net_total_amount}")
    #print(f"avg_change:${avg_change}")
    print(f"avg_amount:{avg_amount :.2f}")
    #print(max(avg_change))
    #print(min(avg_change))
    print(f"Greatest increase in profits:{inc}")
    print(f"Greatest decrease in profits:{dec}")


# open the text file using write mode 
with open(output_path, 'w') as text_file:


    # Write the first row 

    text_file.write(f"Financial Analysis \n")
    text_file.write(f"--------------------------- \n")
    text_file.write(f"Total_months: {Total_months}\n")
    text_file.write(f"Net_total_amount: ${Net_total_amount}\n")
    text_file.write(f"avg_amount:${avg_amount :.2f}\n")
    text_file.write(f"Greatest increase in profits:{inc}\n")
    text_file.write(f"Greatest decrease in profits:{dec}")
    

      





