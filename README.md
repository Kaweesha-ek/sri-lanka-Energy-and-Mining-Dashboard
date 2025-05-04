# sri-lanka-Energy-and-Mining-Dashboard
Streamlit dashboard analyzing Sri Lanka's energy and mining indicators using public datasets.

# Dataset
Source:[ World Bank - Sri Lanka Energy & Mining ](https://data.humdata.org/dataset/world-bank-energy-and-mining-indicators-for-sri-lanka )

# What the Project Does
Shows distribution of indicator values by category via box plots
Compares multiple years for selected indicators using grouped bar charts
Displays time-series trends for any selected indicator
All visuals are dynamic and update based on user selections

# Why the Project Is Useful
This dashboard helps:
Students, researchers, and policymakers quickly gain insights into Sri Lanka’s energy and mining sector
Enable data-driven understanding of development indicators
Convert complex raw data into accessible and interactive visuals

# Aims and Objectives
Analyze key energy and mining indicators relevant to Sri Lanka.
Present trends over time using interactive visual tools.
Support stakeholder decisions with intuitive data exploration.

# Development Methodology
We used a Data Science Lifecycle approach including:

Data Acquisition from the World Bank. 
Data Cleaning & Preprocessing using Pandas.
Feature Engineering to categorize and normalize indicators.
Visualization using Streamlit.
Testing using manual test cases and a test log.

#Files 
app.py
Streamlit dashboard application for visualizing Sri Lanka’s energy and mining data.

preprocessing.py
Python script for cleaning and preprocessing raw data before visualization.

energy-and-mining_lka.csv
Original raw dataset containing energy and mining statistics for Sri Lanka.

cleaned_energy_and_mining_lka.csv
Cleaned dataset used directly in visualizations after preprocessing.

requirements.txt
List of Python libraries required to run the Streamlit app (e.g., streamlit, pandas, plotly, etc.).


