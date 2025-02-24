import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def visualize_birth_trends(input_file, output_folder):
    df = pd.read_csv(input_file, parse_dates=['date'])
    
    # Line plot of birth trends
    plt.figure(figsize=(12, 6))
    df.groupby('date')["births"].sum().plot()
    plt.title("Daily Birth Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Births")
    plt.savefig(os.path.join(output_folder, "birth_trends.png"))
    
    # Heatmap of birth distribution by month and weekday
    pivot_table = df.pivot_table(index='month', columns='day_of_week', values='births', aggfunc='sum')
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, cmap="coolwarm", annot=True, fmt=".0f")
    plt.title("Births by Month and Day of Week")
    plt.savefig(os.path.join(output_folder, "heatmap.png"))
    
    print(f"Visualizations saved to {output_folder}")

if __name__ == "__main__":
    visualize_birth_trends("data/cleaned_birthdays.csv", "outputs/")