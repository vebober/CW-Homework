import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

#find total votes
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_votes = len(csvfile.readlines())
    

#total votes for each candidate
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Tooley_count = 0
    for row in csvreader:
        x = int(row[0])
        y = str(row[1])
        z = str(row[2])

        if  z == "Khan":
            Khan_count = Khan_count + 1
        elif row[2] == "Correy":
            Correy_count = Correy_count + 1
        elif row[2] == "Li":
            Li_count = Li_count + 1
        else:
            Tooley_count = Tooley_count + 1 

Khan_percent = round((Khan_count/total_votes)*100)
Correy_percent = round((Correy_count/total_votes)*100)
Li_percent = round((Li_count/total_votes)*100)
Tooley_percent = round((Tooley_count/total_votes)*100)




print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------")
print("Khan: " + str(Khan_percent) + "% " + "(" + str(Khan_count) + ")")
print("Correy: " + str(Correy_percent) + "% " + "(" + str(Correy_count) + ")")
print("Li: " + str(Li_percent) + "% " + "(" + str(Li_count) + ")")
print("O'Tooley: " + str(Tooley_percent) + "% " + "(" + str(Tooley_count) + ")")
print("------------------------")
if max(Khan_percent,Correy_percent,Li_percent,Tooley_percent) == Khan_percent:
    print("Winner: Khan")
elif max(Khan_percent,Correy_percent,Li_percent,Tooley_percent) == Correy_percent:
    print("Winner: Correy")
elif max(Khan_percent,Correy_percent,Li_percent,Tooley_percent) == Li_percent:
    print("Winner: Li")
elif max(Khan_percent,Correy_percent,Li_percent,Tooley_percent) == Tooley_percent:
    print("Winner: O'Tooley")
print("------------------------")