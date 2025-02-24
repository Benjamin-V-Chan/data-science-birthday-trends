import pandas as pd

def exploratory_analysis(input_file, output_file):
    df = pd.read_csv(input_file, parse_dates=['date'])
    
    summary = df.describe()
    most_common_day = df.groupby('day_of_week')["births"].sum().idxmax()
    least_common_day = df.groupby('day_of_week')["births"].sum().idxmin()
    
    results = {
        "summary_statistics": summary.to_dict(),
        "most_common_birth_day": most_common_day,
        "least_common_birth_day": least_common_day
    }
    
    with open(output_file, "w") as f:
        f.write(str(results))
    
    print(f"Exploratory analysis results saved to {output_file}")

if __name__ == "__main__":
    exploratory_analysis("data/cleaned_birthdays.csv", "outputs/exploratory_results.txt")