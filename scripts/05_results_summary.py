import pandas as pd

def summarize_results(exploratory_file, forecast_file, output_file):
    with open(exploratory_file, "r") as f:
        exploratory_results = f.read()
    
    forecast = pd.read_csv(forecast_file)
    summary = f"Exploratory Analysis:\n{exploratory_results}\n\nForecast Data:\n{forecast.to_string()}"
    
    with open(output_file, "w") as f:
        f.write(summary)
    
    print(f"Summary report saved to {output_file}")

if __name__ == "__main__":
    summarize_results("outputs/exploratory_results.txt", "outputs/birth_forecast.csv", "outputs/final_summary.txt")
