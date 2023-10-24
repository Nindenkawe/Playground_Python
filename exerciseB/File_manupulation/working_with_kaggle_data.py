import pandas as pd
from datetime import datetime

# Function to calculate the time difference in minutes between two time strings
def minutes_between_times(start_time, end_time):
    start_datetime = datetime.strptime(start_time, "%I:%M:%S %p")
    end_datetime = datetime.strptime(end_time, "%I:%M:%S %p")

    # Calculate the time difference in minutes
    time_difference = (end_datetime - start_datetime).total_seconds() / 60

    # Ensure the result is non-negative
    return max(0, int(time_difference))

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('')

# Apply the minutes_between_times function to each row and add the result as a new column
df['duration_minutes'] = df.apply(lambda row: minutes_between_times(row['start_time'], row['end_time']), axis=1)

# Calculate the total time worked in minutes
total_minutes_worked = df['duration_minutes'].sum()

# Define the rates
normal_rate = 80  # RWF per minute
promotion_rate = 100  # RWF per minute during promotion

# Calculate earnings at normal rate and promotion rate
earnings_normal_rate = total_minutes_worked * normal_rate
earnings_promotion_rate = total_minutes_worked * promotion_rate

# Create a bar chart to represent earnings
rates = ['Normal Rate', 'Promotion Rate']
earnings = [earnings_normal_rate, earnings_promotion_rate]

# Plot the bar chart
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.bar(rates, earnings, color=['blue', 'green'])
plt.ylabel('Earnings (RWF)')
plt.title('Earnings at Different Rates')
plt.show()

# Print the total time worked and earnings per rate
print(f"Total time worked: {total_minutes_worked} minutes")
print(f"Earnings at normal rate ({normal_rate} RWF/minute): {earnings_normal_rate} RWF")
print(f"Earnings at promotion rate ({promotion_rate} RWF/minute): {earnings_promotion_rate} RWF")
df.iloc[130]