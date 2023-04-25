import os
import csv
import statistics

maindata = 'election_data.csv'
totalVotes = 0
votesPerCandidate = {}
with open('election_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

csv_header = next(csvreader)

for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1 

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")


