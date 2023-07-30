#import modules
import os
import csv


# create file path 

csvpath = os.path.join('Resources', 'election_data.csv')

#create variables
total_votes = 0
candidates ={}
winner_name =""
winner_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # read the header row
    csv_header = next(csvreader)
    
    # loop through each row in csv
    for row in csvreader:
        #count votes
        total_votes +=1

        # get canidate name from each row
        candidate_name = row[2]
        # if canidate name on list add him if not add 1
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else: 
            candidates[candidate_name] +=1
#calculate winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner_name = candidate

# print analysis
print("Election Results")
print("- "* 30)
print( f" Total Votes: {total_votes}")
print("-" * 30)
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f" {candidate}: {percentage: .3f}% ({votes})")
print("-" * 30)
print(f"Winner: {winner_name}")
print("-" * 30)

with open ('Election_results.txt', 'w') as file:
    file.write("Election Results/n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_name}\n")
    file.write("-------------------------\n")