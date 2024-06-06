import os
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pandasai import SmartDataframe, Agent
import streamlit as st

# Setting the API key:
os.environ["PANDASAI_API_KEY"] = ""

st.title("EduInsight: AI-Powered Student Performance📊 Analysis 📈 using PandasAI🐼 Model")

st.subheader("An AI-powered platform that generates detailed, Personalized Analysis and Reports on Student Performance, Offering Actionable Insights")

uploaded_file = st.file_uploader("Upload CSV or Excel File")

df = pd.read_csv(uploaded_file)

st.dataframe(df, selection_mode="multi-column")

# Creating an Agent object:
data = Agent(df)

prompt = st.text_input("Enter prompt for analysis")
if st.button('Generate Analysis'):
    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.success('Done!')

    st.subheader("Generated Analysis")

    output = data.chat(prompt)

    if isinstance(output, str):
        st.write(output)  # Display text output
    elif isinstance(output, plt.Figure):
        st.pyplot(output)  # Display image output
    elif isinstance(output, pd.DataFrame):
        st.dataframe(output)  # Display DataFrame output
    else:
        st.write("Unsupported output format")



