
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Load preloaded data
df = pd.read_csv("data.csv")

st.sidebar.title("🌱 EcoVerge Analytics")
st.sidebar.write("Data-Driven Decisions for Sustainable Packaging")

menu = st.sidebar.radio("Navigate", [
    "EDA & Overview",
    "Customer Segmentation",
    "Purchase Intent",
    "Association Rules",
    "Spending Prediction",
    "Prescriptive Strategy",
    "New Customer Predictor"
])

st.title("🌱 EcoVerge AI Dashboard")

if menu == "EDA & Overview":
    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Total Customers", len(df))
    col2.metric("Avg Spend", df["monthly_spend"].mode()[0])
    col3.metric("Switch %", round((df["switch_likelihood"]=="Very Likely").mean()*100,2))
    col4.metric("Top Segment", df["business_type"].mode()[0])

    tab1, tab2 = st.tabs(["Demographics","Behavior"])

    with tab1:
        st.plotly_chart(px.histogram(df, x="business_type"))
        st.plotly_chart(px.histogram(df, x="city_tier"))

    with tab2:
        st.plotly_chart(px.histogram(df, x="monthly_volume"))
        st.plotly_chart(px.histogram(df, x="monthly_spend"))

elif menu == "Customer Segmentation":
    st.write("Segmentation Coming Soon")

elif menu == "Purchase Intent":
    st.write("Classification Coming Soon")

elif menu == "Association Rules":
    st.write("Association Rules Coming Soon")

elif menu == "Spending Prediction":
    st.write("Regression Coming Soon")

elif menu == "Prescriptive Strategy":
    st.write("Strategy Engine Coming Soon")

elif menu == "New Customer Predictor":
    st.write("Prediction UI Coming Soon")
