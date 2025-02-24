# data-science-birthday-trends

# Project Overview
This project analyzes birth trends using historical data. It includes data preprocessing, exploratory analysis, visualization, and forecasting to gain insights into birth patterns.

# Folder Structure
```
project-root/
├── data/                 # Contains the dataset
│   ├── birthdays.csv     # Raw dataset
│   ├── cleaned_birthdays.csv # Processed dataset
├── scripts/              # Contains all analysis scripts
│   ├── 01_data_preprocessing.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_visualization.py
│   ├── 04_modeling.py
│   ├── 05_results_summary.py
├── outputs/              # Stores analysis results
│   ├── exploratory_results.txt
│   ├── birth_trends.png
│   ├── heatmap.png
│   ├── birth_forecast.csv
│   ├── final_summary.txt
├── requirements.txt      # Dependencies list
├── README.md             # Project documentation
```

# Usage
## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

## 2. Run Scripts
### Data Preprocessing
```bash
python scripts/01_data_preprocessing.py
```
Processes the raw dataset and saves a cleaned version in the `data/` folder.

### Exploratory Analysis
```bash
python scripts/02_exploratory_analysis.py
```
Computes statistics and key insights, saving results in `outputs/exploratory_results.txt`.

### Data Visualization
```bash
python scripts/03_visualization.py
```
Generates and saves visualizations (`birth_trends.png`, `heatmap.png`) in the `outputs/` folder.

### Forecasting Model
```bash
python scripts/04_modeling.py
```
Trains a time series forecasting model and saves predictions in `outputs/birth_forecast.csv`.

### Results Summary
```bash
python scripts/05_results_summary.py
```
Compiles findings and generates a summary report in `outputs/final_summary.txt`.

# Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn
- statsmodels

# Acknowledgments
- **Dataset Name**: Birthdays  
- **Dataset Author**: Ulrik Thyge Pedersen  
- **Dataset Source**: [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/birthdays/data)