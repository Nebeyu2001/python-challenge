# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources","election_data.csv")

output_path = os.path.join("analysis", "election_anlysis.txt")

total_votes= 0

candidates ={}

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        total_votes = total_votes + 1

        name= row[2]

        if name not in candidates:

             candidates[name]=1

        else:

            candidates[name]=candidates[name] + 1

print(total_votes)

for candidate_name, vote_count in candidates.items():
    print(f"{candidate_name}:{vote_count}")
        