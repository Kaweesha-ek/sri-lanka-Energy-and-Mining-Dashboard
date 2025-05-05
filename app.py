import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page config
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
    "*Sri Lanka's energy and mining sectors* based on World Bank indicators. "
    "Use the sidebar to explore trends, compare years, and dive into distributions."
)
st.markdown("---")

# KPIs (Your original KPI board)
latest_year = df['year'].max()
total_indicators = df['indicator_name'].nunique()
average_value = df['value'].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Latest Year", value=int(latest_year))
with col2:
    st.metric(label="Total Indicators", value=total_indicators)
with col3:
    st.metric(label="Average Value", value=f"{average_value:.2f}")

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
    st.subheader("Distribution of Indicator Values")

    selected_category = st.selectbox("Select Category", sorted(df['indicator_category'].unique()))
    filtered_df = df[df['indicator_category'] == selected_category]

    selected_indicators = st.multiselect("Select Indicator(s)", sorted(filtered_df['indicator_name'].unique()))

    if selected_indicators:
        filtered_df = filtered_df[filtered_df['indicator_name'].isin(selected_indicators)]
        fig = px.box(
            filtered_df,
            x='indicator_name',
            y='value',
            color='indicator_name',
            title=f"Value Distribution in {selected_category}",
            labels={'value': 'Value', 'indicator_name': 'Indicator'},
            template='plotly_white'
        )
        fig.update_layout(xaxis_tickangle=-45, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Please select at least one indicator to display the chart.")

# Yearly Comparison by Category 
elif analysis_option == 'Yearly Comparison by Category':
    st.subheader("Compare Years for Selected Indicators")

    selected_years = st.multiselect("Select Year(s)", sorted(df['year'].unique()), default=[df['year'].max()])
    selected_category = st.selectbox("Choose Category", sorted(df['indicator_category'].unique()))
    category_df = df[(df['year'].isin(selected_years)) & (df['indicator_category'] == selected_category)]

    selected_indicators = st.multiselect("Select Indicator(s)", sorted(category_df['indicator_name'].unique()))

    if selected_indicators:
        filtered_df = category_df[category_df['indicator_name'].isin(selected_indicators)]
    else:
        filtered_df = category_df

    if not filtered_df.empty:
        fig = px.bar(
            filtered_df,
            x='indicator_name',
            y='value',
            color=filtered_df['year'].astype(str),  #Force year to categorical
            barmode='group',
            title=f"{selected_category} Indicators Across Year(s)",
            labels={'value': 'Value', 'indicator_name': 'Indicator', 'color': 'Year'},
            template='plotly_white'
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")


# Trend by Indicator
elif analysis_option == 'Trend by Indicator':
    st.subheader("Indicator Trend Over Time")

    selected_indicator = st.selectbox("Select Indicator", sorted(df['indicator_name'].unique()))
    ind_df = df[df['indicator_name'] == selected_indicator]

    fig = px.line(
        ind_df,
        x='year',
        y='value',
        markers=True,
        title=f"Trend Over Time: {selected_indicator}",
        labels={'value': 'Value', 'year': 'Year'},
        template='plotly_white'
    )
    fig.update_traces(line=dict(color='teal', width=3))
    fig.update_layout(xaxis=dict(dtick=1))
    st.plotly_chart(fig, use_container_width=True)

