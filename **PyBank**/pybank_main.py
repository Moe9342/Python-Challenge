#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import csv

csvpath = "Resources/budget_data.csv"

with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    pydata = csv.reader(csvfile, delimiter=',')
    print(pydata)
    
    # Read the header row first
    csv_header = next(pydata)
    
    # Summary Analysis
    
    countrow = 0
    total = 0
    numcount = 0
    current_row=0
    last_row=0
    dlist = []
    min_value = 0
    max_value = 0
    max_row_date = 0
    min_row_date = 0
       
    for row in pydata: 
        
        # The total number of months included in the dataset
        countrow = countrow + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        total += int(row[1])
        format_total ='${:.0f}'.format(total)
        
        # The average of the changes in "Profit/Losses" over the entire period    
        
        current_row = int(row[1])  
        difference = current_row - last_row
        last_row = current_row   
        dlist.append(difference)
        
        # The greatest increase/decrease in profits (date and amount) over the entire period 
        
        if difference > max_value:
            max_value = difference
            format_max = '${:.0f}'.format(max_value)
            max_row_date = row[0]
            
        if difference < min_value: 
            min_value = difference
            format_min = '${:.0f}'.format(min_value)
            min_row_date = row[0]

                
    total_df = dlist[1:]
    average = sum(total_df) / len(total_df)
    format_average = '${:.2f}'.format(average)
      
    
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: ", str(countrow))
    
    print("Total: ", str(format_total)) 
    
    print('Average  Change: ',format_average)
    
    print(f"Greatest Increase in Profits: {max_row_date} ({format_max})")
    
    print(f"Greatest decrease in Profits: {min_row_date} ({format_min})") 


# In[6]:


#save the print result as text

file = open("PyBank_print.txt","w")

file.write("Financial Analysis \n")
file.write("--------------------------------------------- \n")
file.write(f"Total Months: {str(countrow)} \n")

file.write(f"Total: {str(format_total)}\n")

file.write(f"Average  Change: {format_average}\n")

file.write(f"Greatest Increase in Profits: {max_row_date} ({format_max})\n")

file.write(f"Greatest decrease in Profits: {min_row_date} ({format_min})")

file.close()

