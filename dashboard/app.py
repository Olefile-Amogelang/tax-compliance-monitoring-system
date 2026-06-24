import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("../burs.db")
df = pd.read_sql("SELECT * FROM compliance", conn)

st.title("Tax Compliance Dashboard")

st.metric("High Risk Taxpayers", (df['risk_score'] > 40).sum())

st.dataframe(df)
