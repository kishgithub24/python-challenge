import os
import csv

csvpath = os.path.join("resources", "election_data.csv")
my_report = open(os.path.join('analysis','election_data.txt'), 'w')

votes = 0
cands_list= {}
winner = [0,""]

with open(csvpath) as file:
   csv_reader = csv.reader(file, delimiter=",")

   header = next(csv_reader)

   for row in csv_reader:
      
        # total_votes = votes +1
        votes += 1

        cand = row[2]

        if cand not in cands_list.keys():
            cands_list[cand] = 0

        cands_list[cand]+=1                                                          


output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''

for candidate in cands_list.keys():
    
    candidate_votes = cands_list[candidate]

    output+=f'{candidate}: {candidate_votes/votes*100:.3f}% ({candidate_votes:,})\n'

    if candidate_votes > winner[0]:
      winner[0]=candidate_votes
      winner[1]=candidate


output += f'-------------------------\n Winner: {winner[1]} \n-------------------------'

print(output)
my_report.write(output)
