#PyPoll Homework Assignment Mitesh Parekh

#Import Election Data File
import os
import csv

#Data File Name and Path to Open: C:\Users\mites\OneDrive\Documents\RU Data Science Bootcamp\python-challenge\PyPoll\election_data.csv
#Read CSV File, identify comma delimiter, and print csvreader

csvpath = "election_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)

#Read Header Row 
    csv_header = next(csvreader)
   

#Determine Initial Variable Values
    Total_Votes = 0
    candidates = []
    candidate_Khan = []
    votes_Khan = 0
    candidate_Correy = []
    votes_Correy = 0
    candidate_Li = []
    votes_Li = 0
    candidate_OTooley = []
    votes_OTooley = 0

#Calculate Total Votes and check value

    for row in csvreader:
            Total_Votes = Total_Votes + 1
            candidates.append(row[2])          
    

#Counting Votes for each candidate in Candidates list )
    for candidate in candidates:
        if candidate == "Khan":
            candidate_Khan.append(candidates)
            votes_Khan = len(candidate_Khan)
        elif candidate == "Correy":
            candidate_Correy.append(candidates)
            votes_Correy = len(candidate_Correy)
        elif candidate == "Li":
            candidate_Li.append(candidates)
            votes_Li = len(candidate_Li)
        else :
            candidate_OTooley.append(candidates)
            votes_OTooley = len(candidate_OTooley)


# Determine the Winning Candiate and print winner (commented out)
    if votes_Khan > max(votes_Correy, votes_Li, votes_OTooley):
        election_winner = "Khan"
    elif votes_Correy > max(votes_Khan, votes_Li, votes_OTooley):
        election_winner = "Correy"
    elif votes_Li > max(votes_Khan, votes_Correy, votes_OTooley):
        election_winner = "Li"
    else:
        election_winner = "OTooley"
    

#Calculate percentage of votes for each candidate

    percentage_khan = round((votes_Khan / Total_Votes),3)*100
  
    percentage_correy = round((votes_Correy / Total_Votes),3)*100
   
    percentage_li = round((votes_Li / Total_Votes),3)*100
   
    percentage_otooley = round((votes_OTooley / Total_Votes),3)*100
    
    
# Print Results on Terminal

print("Election Data Analysis - Mitesh Parekh")
print("----------------------------------------------")
print("Total Votes: " + str(Total_Votes))
print("----------------------------------------------")
print("Election Results by Candidate")
print("----------------------------------------------")
print("Candidate Khan received " + str(votes_Khan) + " votes (" + str(percentage_khan) + "%)")
print("Candidate Correy received " + str(votes_Correy) + " votes (" + str(percentage_correy) + "%)")
print("Candidate Li received " + str(votes_Li) + " votes (" + str(percentage_li) + "%)")
print("Candidate OTooley received " + str(votes_OTooley) + " votes (" + str(percentage_otooley) + "%)")
print("----------------------------------------------")
print("The Winner of the election is...(drum roll).... " + election_winner +"! Congratulations!!")

#Write to a Text File
#Path to Write and File Name: C:\Users\mites\OneDrive\Documents\RU Data Science Bootcamp\python-challenge\PyPoll\PyPoll_Results.txt

txtpath = os.path.join ('OneDrive', 'Documents','RU Data Science Bootcamp', 'python-challenge', 'PyPoll','PyPoll_Results.txt')
with open(txtpath, "w") as file:
         file.write ("Election Data Analysis - Mitesh Parekh"+'\n')
         file.write ("----------------------------------------------"+'\n')
         file.write ("Total Votes: " + str(Total_Votes)+'\n')
         file.write ("----------------------------------------------"+'\n')
         file.write ("Candidate Khan received " + str(votes_Khan) + " votes (" + str(percentage_khan) + "%)"+'\n')
         file.write ("Candidate Correy received " + str(votes_Correy) + " votes (" + str(percentage_correy) + "%)"+'\n')
         file.write ("Candidate Li received " + str(votes_Li) + " votes (" + str(percentage_li) + "%)"+'\n')
         file.write ("Candidate OTooley received " + str(votes_OTooley) + " votes (" + str(percentage_otooley) + "%)"+'\n')
         file.write ("----------------------------------------------"+'\n')
         file.write ("The Winner of the election is...(drum roll).... " + election_winner +"! Congratulations!!"+'\n')
