# Player Receiving Yards Analysis Script

This Python script processes player receiving yards data from an exported CSV file, analyzes over/under outcomes, and identifies players who consistently go over or under projected receiving yards. It's designed to help spot trends for making smarter betting decisions.

## Features
- Cleans and filters data, removing duplicates.
- Aggregates game data to count the total number of games each player has participated in.
- Calculates the percentage of games in which a player goes "Over" or "Under" the projected receiving yards.
- Identifies players who consistently go over or under (e.g., more than 60% of the time).
- Outputs the results as a CSV for further analysis.

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone this repository or download the script.
2. Install the required Python package by running:

    ```bash
    pip install pandas
    ```

3. Replace the placeholder file path `'path_to_your_exported_csv.csv'` in the script with the path to your actual CSV file containing player data.

## Usage

1. **Load the Data**: The script reads the exported CSV containing the following columns:
   - `player_name`: The name of the player.
   - `outcome`: The result of the game (either "Over" or "Under").
   - `start_date`: The date of the game.

2. **Run the Script**:
    ```bash
    python player_receiving_yards_analysis.py
    ```

3. **Output**: The script will display two lists of players:
   - Players who consistently go "Over" more than 60% of the time.
   - Players who consistently go "Under" more than 60% of the time.

4. **CSV Export**: It also saves the results in two CSV files:
   - `consistent_over_players.csv`
   - `consistent_under_players.csv`

## Example Output

```bash
Players who consistently go Over (>60%):
   player_name  total_games  over_count  under_count  over_percentage  under_percentage
0   Player 1        5            4             1               80.0               20.0
1   Player 2        5            3             2               60.0               40.0

Players who consistently go Under (>60%):
   player_name  total_games  over_count  under_count  over_percentage  under_percentage
0   Player 3        5            1             4               20.0               80.0
