from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_births(input_file, output_file):
    df = pd.read_csv(input_file, parse_dates=['date'])
    df = df.set_index("date").resample("M").sum()
    
    # Fit exponential smoothing model
    model = ExponentialSmoothing(df["births"], seasonal="add", seasonal_periods=12).fit()
    forecast = model.forecast(12)
    
    forecast.to_csv(output_file)
    print(f"Forecast saved to {output_file}")

if __name__ == "__main__":
    forecast_births("data/cleaned_birthdays.csv", "outputs/birth_forecast.csv")