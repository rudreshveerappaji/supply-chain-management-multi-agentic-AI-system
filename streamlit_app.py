import streamlit as st
import pandas as pd
from main import main as run_crew

st.title("Construction Supply Chain Dashboard")

if st.button("Run SCM Workflow"):
    st.write("Running CrewAI agents...")
    result = run_crew()
    st.success("Workflow completed!")
    st.write(result)

st.header("Material Forecast")
if st.checkbox("Show Forecast"):
    df = pd.read_csv("data/material_forecast.csv")
    st.dataframe(df)

st.header("Purchase Orders")
if st.checkbox("Show Purchase Orders"):
    df = pd.read_csv("data/purchase_orders.csv")
    st.dataframe(df)

st.header("Delivery Schedule")
if st.checkbox("Show Delivery Schedule"):
    df = pd.read_csv("data/delivery_schedule.csv")
    st.dataframe(df)

st.header("Site Usage Log")
if st.checkbox("Show Site Usage"):
    df = pd.read_csv("data/site_usage_log.csv")
    st.dataframe(df)
