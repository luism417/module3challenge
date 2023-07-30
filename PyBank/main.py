#import dependencies 
import os
import csv
#create variable 
total_months = 0
total_net_profit_losses= 0
previous_profit_losses=0
profit_losses_changes = []
greatest_increase = {"date": "", "profit": 0}
greatest_decrease = {"date": "", "profit": 0}
# create file path
csvpath = os.path.join('Resources','budget_data.csv')

#read in file 
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    print(csvreader)

# read in first row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


#loop through each row in the csv
    for row in csvreader:
       #total number of months
       total_months +=1

       # calculate net total amount of profit/losses over entire period
       current_profit_losses = int(row[1])
       total_net_profit_losses += current_profit_losses
       
       #csalculate changes in profit/losses over the entire period
       if total_months > 1: 
          change = current_profit_losses - previous_profit_losses
          profit_losses_changes.append(change)

         # calculate greatest increase and decrease in profits
          if change > greatest_increase["profit"]:
             greatest_increase = {"date": row[0], "profit": change}
          if change < greatest_decrease[ "profit"]:
                greatest_decrease = {"date": row[0], "profit": change}
    previous_profit_losses = current_profit_losses
# average of the changes in profit/losses
average_change = sum(profit_losses_changes) / len(profit_losses_changes)             

# print analysis
print(" Finacial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${total_net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['profit']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['profit']})")


# export text file
output_path = "finacial_anlysis.txt"
with open(output_path, 'w') as file:
    file.write("Financial_analysis/n")
    file.write("-" * 30)
    file.write(f"\nTotal Months: {total_months}")
    file.write(f"\nTotal: ${total_net_profit_losses}")
    file.write(f"\nAverage Change: ${average_change:.2f}")
    file.write(f"\nGreatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['profit']})")
    file.write(f"\nGreatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['profit']})")