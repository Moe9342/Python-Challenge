#!/usr/bin/env python
# coding: utf-8

# In[38]:


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

khan_percentage = khan_vote / row_count           
format_khan_percentage = "{0:.3%}".format(khan_percentage)

Correy_percentage = Correy_vote / row_count           
format_Correy_percentage = "{0:.3%}".format(Correy_percentage)

Li_percentage = Li_vote / row_count           
format_Li_percentage = "{0:.3%}".format(Li_percentage)

OTooley_percentage = OTooley_vote / row_count           
format_OTooley_percentage = "{0:.3%}".format(OTooley_percentage)

print("Election Results")
print("-----------------------------------------")    
print("Total Votes: ",row_count )        
print("-----------------------------------------")
print("List of candidates: ", candidate_list)
print("-----------------------------------------")
print("Khan: ",format_khan_percentage,"(",khan_vote,")")
print("Correy: ",format_Correy_percentage,"(",Correy_vote,")" )
print("Li: ",format_Li_percentage,"(",Li_vote,")")
print("OTooley: ",format_OTooley_percentage,"(",OTooley_vote,")")
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


# In[ ]:




