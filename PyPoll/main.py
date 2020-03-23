#PyBank Homework Assignment - Mitesh Parekh

#Import Budget Data File
import os
import csv

#Data File Name and Path to Open: C:\Users\mites\OneDrive\Documents\RU Data Science Bootcamp\python-challenge\PyBank\budget_data.csv
#Read CSV File, identify comma delimiter, and print csvreader

csvpath = "budget_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)

#Read Header Row and check print headers for confirmation
    csv_header = next(csvreader)
    

# Create initial empty sets
    month = []
    monthly_revenue_chg = []
    avg_monthly_revenue_chg = []
    total_revenue = 0
    total_revenue_change = 0
    prev_month_rev = 0

#Calculate Number of Months, and Sum Up total Profit or Loss in Budget Datafile
    for row in csvreader:
        month.append(row[0])
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1]) - prev_month_rev
        prev_month_rev = int(row[1])
        monthly_revenue_chg.append(revenue_change)
 


# Calculate average monthly change in budget datafile: Total Revenue Change / # Months 
    average_monthly_chg = round((sum(monthly_revenue_chg) - monthly_revenue_chg[0]) / (len(month) -1 ),2)
    
    
# Determine the greatest monthly profit increase amount, and identify month
    largest_increase = max(monthly_revenue_chg)
    
    lg_inc_mnth = monthly_revenue_chg.index(largest_increase)
    largest_increase_month = month[lg_inc_mnth]
    

# Determine the greatest monthly decrease change amount, and identify month
    largest_decrease = min(monthly_revenue_chg)
    
    lg_dec_mnth = monthly_revenue_chg.index(largest_decrease)
    largest_decrease_month = month[lg_dec_mnth]
   
  
# Print Results on Terminal

print("Budget Data Financial Analysis - Mitesh Parekh")
print("----------------------------------------------")
print("Total Months: " + str(len(month)))
print("Total Profit: $" + str(total_revenue))
print("Average Change: $" + str(average_monthly_chg))
print("Greatest Increase in Profits: " + largest_increase_month + " ($" + str(largest_increase) +")")
print("Greatest Decrease in Profits: " + largest_decrease_month + " ($" + str(largest_decrease) +")")

#Write to a Text File
#Path to Write and File Name: C:\Users\mites\OneDrive\Documents\RU Data Science Bootcamp\python-challenge\PyBank\Pybank_Results.txt
txtpath = os.path.join ('OneDrive', 'Documents','RU Data Science Bootcamp', 'python-challenge', 'Pybank','Pybank_Results.txt')
with open(txtpath, "w") as file:
        file.write ("Budget Data Financial Analysis - Mitesh Parekh"+'\n')
        file.write ("----------------------------------------------"+'\n')
        file.write ("Total Months: " + str(len(month))+'\n')
        file.write ("Total Profit: $" + str(total_revenue)+'\n')
        file.write ("Average Change: $" + str(average_monthly_chg)+'\n')
        file.write ("Greatest Increase in Profits: " + largest_increase_month + " ($" + str(largest_increase) +")"+'\n')
        file.write ("Greatest Decrease in Profits: " + largest_decrease_month + " ($" + str(largest_decrease) +")"+'\n')
