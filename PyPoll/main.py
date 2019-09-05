import os
import csv

election_data_CSV = os.path.join('election_data.csv')

with open(election_data_CSV, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    Votes = []
    Candidates = []
    Vote_Count = 0
    Candidate_Votes = {}

    # Loop through the data
    for row in csvreader:
        Votes.append(row[0])
        Candidate_Name = row[2]
        
        if Candidate_Name not in Candidates:
            Candidates.append(Candidate_Name)
            Candidate_Votes[Candidate_Name] = 0
        Candidate_Votes[Candidate_Name] = Candidate_Votes[Candidate_Name] + 1

    
    
    print('Election Results')
    print('-------------------------')  
    print(f'Total Votes: {len(Votes)}')
    print('-------------------------')
    for Candidate in Candidates:
        Percent_Of_Votes = "{:.3%}".format((Candidate_Votes[Candidate]/len(Votes)))
        print(f'{Candidate}: {Percent_Of_Votes} ({Candidate_Votes[Candidate]})')
       
    Max_Votes = max(Candidate_Votes.values())
    
    for Candidate_Name in Candidate_Votes:
        if Candidate_Votes[Candidate_Name] == Max_Votes:
            Max_Votes = Candidate_Votes[Candidate_Name]
            Winner = Candidate_Name
            print('-------------------------')
            print(f'Winner: {Winner}')
            print('-------------------------')

    f = open('Election_Results.txt', 'w')
    print('Election Results', file=f)
    print('-------------------------', file=f)  
    print(f'Total Votes: {len(Votes)}', file=f)
    print('-------------------------', file=f)
    for Candidate in Candidates:
        Percent_Of_Votes = "{:.3%}".format((Candidate_Votes[Candidate]/len(Votes)))
        print(f'{Candidate}: {Percent_Of_Votes} ({Candidate_Votes[Candidate]})', file=f)
    
    for Candidate_Name in Candidate_Votes:
        if Candidate_Votes[Candidate_Name] == Max_Votes:
            Max_Votes = Candidate_Votes[Candidate_Name]
            Winner = Candidate_Name
            print('-------------------------', file=f)
            print(f'Winner: {Winner}', file=f)
            print('-------------------------', file=f)
    f.close()