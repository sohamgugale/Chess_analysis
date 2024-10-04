import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'games.csv'
chess_games_df = pd.read_csv(file_path)

# Data cleaning
chess_games_df.dropna(subset=['winner'], inplace=True)

# Function to analyze openings and their success rates
def analyze_openings():
    opening_stats = chess_games_df.groupby(['opening_name', 'winner']).size().unstack().fillna(0)
    opening_stats['total_games'] = opening_stats.sum(axis=1)
    opening_stats['white_win_rate'] = opening_stats['white'] / opening_stats['total_games'] * 100
    opening_stats['black_win_rate'] = opening_stats['black'] / opening_stats['total_games'] * 100
    return opening_stats.sort_values('total_games', ascending=False).head(10)

# Function to analyze rating differences and victory likelihood
def analyze_rating_impact():
    chess_games_df['rating_diff'] = chess_games_df['white_rating'] - chess_games_df['black_rating']
    rating_win_stats = chess_games_df.groupby(['rating_diff', 'winner']).size().unstack().fillna(0)
    return rating_win_stats

# Function to plot victory types based on rating differences
def plot_victory_types():
    victory_types = chess_games_df['victory_status'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=victory_types.index, y=victory_types.values)
    plt.title('Victory Types in Chess Games')
    plt.xlabel('Victory Type')
    plt.ylabel('Count')
    plt.savefig('victory_types.png')
    plt.show()

# Main analysis function
def main():
    print("Analyzing the most common openings...")
    opening_stats = analyze_openings()
    print(opening_stats)
    
    print("Analyzing rating differences and their impact on victories...")
    rating_win_stats = analyze_rating_impact()
    print(rating_win_stats.head())

    print("Plotting victory types...")
    plot_victory_types()

# Run the analysis
if __name__ == "__main__":
    main()
