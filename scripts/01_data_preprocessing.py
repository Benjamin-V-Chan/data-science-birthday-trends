import pandas as pd
import os

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Convert to datetime format
    df['date'] = pd.to_datetime(df[['year', 'month', 'date_of_month']])
    
    # Drop unnecessary columns
    df = df[['date', 'day_of_week', 'births']]
    
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data("data/birthdays.csv", "data/cleaned_birthdays.csv")