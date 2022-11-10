# Import library
import os
import csv

# Change directory
os.chdir(os.path.dirname(__file__))

# Create path
budget_data_csv_path = os.path.join(
    "C:\\Users\\M.Sam\\Documents\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv")

# Define variables
count_months = 0
total_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

months = []
profit_loss_changes = []



# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row 
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        count_months += 1
        # Total amount of Profit/Losses
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Change in profit loss
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            # Append each month
            months.append(row[0])
            # Append each profit_loss_change
            profit_loss_changes.append(profit_loss_change)
            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    # Sum and Average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss / (count_months - 1), 2)

    # Max and min changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of max and min changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print results to Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${total_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# -->>  Export text file with results
budget_file = os.path.join("C:\\Users\\M.Sam\\Documents\\GitHub\\python-challenge\\PyBank\\analysis\\budget_data.txt")
with open(budget_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${total_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")
    outfile.close()
    