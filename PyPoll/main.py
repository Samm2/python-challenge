# Import library
import os
import csv

# Create path
election_data_path = os.path.join("C:\\Users\\M.Sam\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources"
                                  "\\election_data.csv")

# Define variables
total_votes = 0

candidates = []
vote_counts = []



# Open and read csv file
with open(election_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    line = next(csvreader, None)

    # read through each row of data after header
    for line in csvreader:

        # total number of votes
        total_votes = total_votes + 1

        # candidate
        candidate = line[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

# calculate percentage of vote for  candidates and for the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count] / total_votes * 100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

# Print results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Export text file with results
text_path = os.path.join("C:\\Users\\M.Sam\\Documents\\GitHub\\python-challenge\\PyPoll\\analysis\\election_data.txt")
with open(text_path, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("--------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    for count in range(len(candidates)):
        outfile.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("---------------------------\n")
    outfile.close()