import pandas as pd

# Step 1: Load the CSV file
file_path = 'receiving_yards.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Step 2: Clean and filter data for relevant columns and remove duplicates based on player_name and start_date
# Assuming the CSV contains columns: player_name, outcome (Over/Under), and start_date
data = data[['player_name', 'outcome', 'start_date']].drop_duplicates()

# Step 3: Count the total number of distinct games and "Over" and "Under" outcomes for each player
player_summary = data.groupby('player_name').agg(
    total_games=('start_date', 'nunique'),  # Count unique game dates
    over_count=('outcome', lambda x: (x == 'Over').sum()),
    under_count=('outcome', lambda x: (x == 'Under').sum())
).reset_index()

# Step 4: Calculate percentages for "Over" and "Under"
player_summary['over_percentage'] = (player_summary['over_count'] / player_summary['total_games']) * 100
player_summary['under_percentage'] = (player_summary['under_count'] / player_summary['total_games']) * 100

# Step 5: Filter for players who consistently go "Over" or "Under" (e.g., over 60% of the time)
consistent_over = player_summary[player_summary['over_percentage'] > 60]
consistent_under = player_summary[player_summary['under_percentage'] > 60]

# Step 6: Display the results
print("Players who consistently go Over (>60%):")
print(consistent_over)

print("\nPlayers who consistently go Under (>60%):")
print(consistent_under)

# Optionally, save the results to a CSV for further analysis
consistent_over.to_csv('consistent_over_players.csv', index=False)
consistent_under.to_csv('consistent_under_players.csv', index=False)
