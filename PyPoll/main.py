# Modules
import os
import csv

# set path for file to read and write
csvpath = os.path.join("Resources","election_data.csv")

output_path = os.path.join("analysis", "election_anlysis.txt")

# initialize the total votes into zero before counting row by row
total_votes= 0

# start with an empty dictionary to fill
candidates ={}

max_vote_count=0


# open CSV file for reading

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # counting each vote row by row in CSV
        total_votes = total_votes + 1

        # create a variable for the candidates name based on the index in CSV    
        name= row[2]


        # adding the candidates name into an empty dictionary if itisnot there
        if name not in candidates:

             candidates[name]=1
        # if the name is in the candidates list, start counting the vote
        else:

            candidates[name]=candidates[name] + 1
            
# after looping through whole csv row by row we get the total count of votes
print(f"Total votes: {total_votes}")


# loop through the key and values in the dictionary 
for candidate_name, vote_count in candidates.items():

    # calculates the percentage of each candidates vote /first changing string into int
    percentage= int(vote_count)/(total_votes)

    # finding the greatest vote count in the dictionary and then associated key gives us winner candidate
    if vote_count > max_vote_count:

        max_vote_count = vote_count

        winner = candidate_name

        print(winner)

    # prints each candidates name, the vote count and calculated percentage of vote count
    print(f"{candidate_name}:{percentage:.3%} ({vote_count})")

# open the text file using write mode 
with open(output_path, 'w') as text_file:


    # Write the first row 
    text_file.write(f"Election Results\n")
    text_file.write(f"------------------------------\n")
    text_file.write(f"Total_votes: {total_votes}\n")
    text_file.write(f"------------------------------\n")

    for candidate_name, vote_count in candidates.items():

        percentage= int(vote_count)/(total_votes)

        text_file.write(f"{candidate_name}:{percentage:.3%} ({vote_count}) \n")

    text_file.write(f"------------------------------\n")

    text_file.write(f"Winner: {winner}")
   
    

        