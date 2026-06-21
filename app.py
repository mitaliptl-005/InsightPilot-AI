import streamlit as st
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("InsightPilot AI")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    schema = str(df.dtypes)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        f"""
        Analyze this dataset schema:

        {schema}

        Provide a short dataset summary.
        """
    )

    st.subheader("AI Dataset Summary")
    st.write(response.text)