# Agridata Explorer


## Project Overview

Agridata Explorer is an end-to-end data analytics project focused on analyzing Indian agricultural crop production data. The project uses Python for data cleaning and exploratory data analysis (EDA), SQL for structured analysis, and Power BI for interactive dashboard visualization. The goal is to identify production trends, top-performing states, and crop-wise insights over multiple years.



## Tools & Technologies

* Python (Pandas, Matplotlib)
* SQL
* Power BI Desktop
* VS Code
* CSV Dataset (ICRISAT – District Level Agricultural Data)



## Dataset Source

* ICRISAT – District Level Agricultural Data (India)
* The dataset contains crop production, area, and yield information across different Indian states and districts over multiple years.



## Project Structure

AGRIDATA_EXPLORER/
│
├── data/
│   ├── Cleaned_data.csv
│   └── ICRISAT-District Level Data.csv
│
├── Plots/
│   ├── area_vs_production_heatmap.png
│   ├── rice_vs_wheat_50years.png
│   ├── sugarcane_50years.png
│   ├── top_rice_states.png
│   ├── top_wheat_states.png
│   ├── yield_comparison_states.png
│   └── other crop analysis plots
│
├── Power BI/
│   ├── 1_overview.png
│   ├── crop_insights.png
│   ├── state_analysis.png
│   └── trend_analysis.png
│
├── Scripts/
│   ├── cleaning_eda.py
│   └── eda_analysis.py
│
├── Sql/
│   └── agricultural_queries.sql
│
├── agridata_dashboard.pbix
└── README.md



## Data Cleaning & Exploratory Data Analysis (Python)

* Removed missing and duplicate values from the dataset
* Filtered and standardized crop, state, and year data
* Performed exploratory data analysis to understand trends and distributions
* Created multiple visualizations for:

  * Crop production trends over years
  * Top producing states by crop
  * Yield comparisons across states
* Saved all generated plots inside the Plots folder



## SQL Analysis

* Wrote SQL queries to analyze agricultural data efficiently
* Analysis includes:

  * Year-wise crop production trends
  * Top producing states for major crops
  * Yield and production comparisons across states
* All SQL queries are stored in `agricultural_queries.sql`



## Power BI Dashboard

* Built an interactive Power BI dashboard using the cleaned dataset
* Created multiple report pages including:

  * Overall production overview
  * Crop-wise insights
  * State-wise analysis
  * Year-wise trend analysis
* Dashboard file is saved as `agridata_dashboard.pbix`
* Dashboard screenshots are available in the Power BI folder for quick preview



## Key Insights

* Rice and wheat are the most dominant crops across multiple Indian states
* Certain states consistently lead in oilseed and sugarcane production
* Crop yield trends show significant variation over time and region
* Power BI visuals enable easy comparison of crops, states, and years



## How to Run the Project

1. Open the project folder in VS Code
2. Run `cleaning_eda.py` to clean and prepare the dataset
3. Run `eda_analysis.py` to generate EDA plots
4. Open `agridata_dashboard.pbix` using Power BI Desktop to view the dashboard



## Conclusion

This project demonstrates end-to-end data analytics skills, including data cleaning, exploratory analysis, SQL querying, and interactive dashboard creation using industry-standard tools.

## Author

   Revathy Ajith
 Aspiring Data Scientist / Data Analysist



## Future Improvements
============================

* Add predictive analysis using machine learning models
* Deploy the dashboard using Power BI Service
* Include more recent or real-time agricultural datasets
