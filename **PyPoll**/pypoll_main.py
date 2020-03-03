#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

csvpath = "Resources/election_data.csv"

with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    polldata = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(polldata)
    
    row_count = 0
    candidate_list = []
    khan_vote = 0 
    Correy_vote = 0
    Li_vote = 0
    OTooley_vote = 0
    largest_vote = 0
    
    # The total number of votes cast
    for row in polldata:
        row_count = row_count + 1
        
    # A complete list of candidates who received votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    # The total number of votes each candidate won
        if row[2] == "Khan":
            khan_vote = khan_vote + 1
        elif row[2] == "Correy":
            Correy_vote = Correy_vote + 1
        elif row[2] == "Li":
            Li_vote = Li_vote + 1
        else:
            OTooley_vote = OTooley_vote + 1
    
      
# The percentage of votes each candidate won

khan_percentage = 100*(khan_vote / row_count)           

Correy_percentage = 100*(Correy_vote / row_count)           

Li_percentage = 100*(Li_vote / row_count)

OTooley_percentage = 100*(OTooley_vote / row_count)
          

print("Election Results")
print("-----------------------------------------")    
print("Total Votes: ",row_count )        
print("-----------------------------------------")
print("List of candidates: ", candidate_list)
print("-----------------------------------------")
print(f"Khan: {khan_percentage:.3f}% ({khan_vote})")
print(f"Correy: {Correy_percentage:.3f}% ({Correy_vote})")
print(f"Li: {Li_percentage:.3f}% ({Li_vote})")
print(f"OTooley: {OTooley_percentage:.3f}% ({OTooley_vote})")
print("-----------------------------------------")

# The winner of the election based on popular vote.
vote_dic = {"Khan": khan_vote,
            "Correy": Correy_vote,
            "Li": Li_vote,
            "OTooley":OTooley_vote}

for value in vote_dic.values():
    if value > largest_vote: 
        largest_vote = value
        print("Winner: ",(list(vote_dic.keys())[list(vote_dic.values()).index(largest_vote)]))


# In[3]:


#save the print result as text

file = open("PyPoll_print.txt","w")

file.write("Election Results\n")
file.write("-----------------------------------------\n")    
file.write(f"Total Votes: {row_count}\n")      
file.write("-----------------------------------------\n")
file.write(f"List of candidates:{candidate_list}\n")
file.write("-----------------------------------------\n")
file.write(f"Khan: {khan_percentage:.3f}% ({khan_vote})\n")
file.write(f"Correy: {Correy_percentage:.3f}% ({Correy_vote})\n")
file.write(f"Li: {Li_percentage:.3f}% ({Li_vote})\n")
file.write(f"OTooley: {OTooley_percentage:.3f}% ({OTooley_vote})\n")
file.write("-----------------------------------------")

file.close()

