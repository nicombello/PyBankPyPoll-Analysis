import os
import csv
import collections

from collections import Counter

#Storage for computed data

candidate_list=[]
candidate_votes=[]

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Finding the list of candidates

    for row in csvreader:
        candidate_votes.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

#Find the total number of votes cast
Total_votes=(len(candidate_votes))

#Find the votes per candidate
Votes_tally = Counter(candidate_votes)

#Find the candidate with most votes
Votes_tally.most_common()
votes_winner=Votes_tally.most_common(1)[0][0]

#Define variables for each candidate tally
Kahn_votes = Votes_tally['Kahn']
Correy_votes = Votes_tally['Correy']
Li_votes = Votes_tally['Li']
OTooley_votes = Votes_tally["O'Tooley"]

print("-----------------------------------------------")
print("Election Results")
print("Candidates:", candidate_list)
print("-----------------------------------------------")
print('Total Votes =','{:,}'.format(Total_votes))
print("-----------------------------------------------")
print("   Votes for Kahn =",'{:,}'.format(Votes_tally['Kahn']),"Percent of Votes:",'{:.2f}'.format(Kahn_votes/Total_votes*100),"%")
print(" Votes for Correy =",'{:,}'.format(Votes_tally['Correy']),"Percent of Votes:",'{:.2f}'.format(Correy_votes/Total_votes*100),"%")
print("     Votes for Li =",'{:,}'.format(Votes_tally['Li']),"Percent of Votes:",'{:.2f}'.format(Li_votes/Total_votes*100),"%")
print("Votes for O'Tooley =",'{:,}'.format(Votes_tally["O'Tooley"]),"Percent of Votes:",'{:.2f}'.format(OTooley_votes/Total_votes*100),"%")
print("")
print("-----------------------------------------------")
print("Election Winner: ", votes_winner)
print("-----------------------------------------------")
print("")

#Writing Results to a text file
with open('election_results.txt','w') as f:
    f.write("Election Results" + "\n" + "------------------------------"+"\n" +"Total Votes = "+ str(Total_votes)+"\n"
    +"------------------------------"+ "\n"
    +"   Votes for Kahn =" + str(Kahn_votes) +"Percent of Votes=" + str(Kahn_votes/Total_votes*100) + "%" + "\n"
    +" Votes for Correy =" + str(Correy_votes) +"Percent of Votes=" + str(Correy_votes/Total_votes*100) + "%" + "\n"
    +"     Votes for Li =" + str(Li_votes) +"Percent of Votes=" + str(Li_votes/Total_votes*100) + "%" + "\n"
    +"Votes for O'Tooley =" + str(Otooley_votes) +"Percent of Votes=" + str(Otooley_votes/Total_votes*100) + "%" + "\n"
    +"------------------------------"+ "\n"
    +"Election winner = " + str(votes_winner + "\n"
    +"------------------------------"+ "\n"
    )
    f.close()