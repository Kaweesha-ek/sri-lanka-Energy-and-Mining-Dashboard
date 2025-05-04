import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#  Page config must be the first Streamlit command
st.set_page_config(page_title="Sri Lanka Energy & Mining Dashboard", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_energy_and_mining_lka.csv')
    return df

df = load_data()

# Dashboard title
st.title("Sri Lanka Energy & Mining Dashboard")
st.markdown(
    "Welcome to the interactive dashboard that provides insights into "
    "**Sri Lanka's energy and mining sectors** based on World Bank indicators. "
    "Use the sidebar to explore trends, compare years, and dive into distributions."
)
st.markdown("---")

# Sidebar navigation
analysis_option = st.sidebar.selectbox(
    'Select Analysis',
    (
        'Distribution by Indicator Name',
        'Yearly Comparison by Category',
        'Trend by Indicator'
    )
)

# Distribution by Indicator Name
if analysis_option == 'Distribution by Indicator Name':
    st.subheader(" Distribution of Indicator Values")

    selected_category = st.selectbox(" Select Category", sorted(df['indicator_category'].unique()))
    filtered_df = df[df['indicator_category'] == selected_category]

    selected_indicators = st.multiselect(" Select Indicator(s)", sorted(filtered_df['indicator_name'].unique()))

    if selected_indicators:
        filtered_df = filtered_df[filtered_df['indicator_name'].isin(selected_indicators)]

        plt.figure(figsize=(12, 6))
        sns.boxplot(
            x='indicator_name', 
            y='value', 
            data=filtered_df, 
            palette='pastel'
        )
        plt.xticks(rotation=45, ha='right')
        plt.title(f" Value Distribution in {selected_category}", fontsize=14)
        plt.xlabel("")
        plt.ylabel("Value")
        plt.tight_layout()
        st.pyplot(plt.gcf())
    else:
        st.info("Please select at least one indicator to display the chart.")

# Yearly Comparison
elif analysis_option == 'Yearly Comparison by Category':
    st.subheader("Compare Years for Selected Indicators")

    selected_years = st.multiselect(
        "Select Year(s)", sorted(df['year'].unique()), default=[df['year'].max()]
    )

    selected_category = st.selectbox("Choose Category", sorted(df['indicator_category'].unique()))
    category_df = df[(df['year'].isin(selected_years)) & (df['indicator_category'] == selected_category)]

    selected_indicators = st.multiselect(
        "Select Indicator(s)", sorted(category_df['indicator_name'].unique())
    )

    if selected_indicators:
        filtered_df = category_df[category_df['indicator_name'].isin(selected_indicators)]
    else:
        filtered_df = category_df

    if not filtered_df.empty:
        unique_years = sorted(filtered_df['year'].unique())
        colors = sns.color_palette("Set2", len(unique_years))
        year_color_map = dict(zip(unique_years, colors))

        if filtered_df['indicator_name'].str.contains("investment", case=False).any():
            y_label = "Value (in million USD)"
        elif filtered_df['indicator_name'].str.contains("access to electricity|renewable energy consumption|firms using banks|value lost due to electrical outages", case=False).any():
            y_label = "Proportion (0–1 scale)"
        else:
            y_label = "Value"

        plt.figure(figsize=(14, 6))
        sns.barplot(data=filtered_df, x='indicator_name', y='value', hue='year', palette=year_color_map)
        plt.title(f"{selected_category} Indicators Across Year(s)", fontsize=14)
        plt.ylabel(y_label)
        plt.xlabel("")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(plt.gcf())
    else:
        st.warning("No data available for the selected filters.")

# Trend by Indicator
elif analysis_option == 'Trend by Indicator':
    st.subheader("Indicator Trend Over Time")

    selected_indicator = st.selectbox("Select Indicator", sorted(df['indicator_name'].unique()))
    ind_df = df[df['indicator_name'] == selected_indicator]

    plt.figure(figsize=(12, 5))
    sns.lineplot(x='year', y='value', data=ind_df, marker='o', color='teal', linewidth=2.5)
    plt.title(f"Trend Over Time: {selected_indicator}", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())
