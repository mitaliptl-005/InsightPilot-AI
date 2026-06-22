import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ====================================
# Load Environment Variables
# ====================================
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

# ====================================
# Streamlit Configuration
# ====================================
st.set_page_config(
    page_title="InsightPilot AI",
    layout="wide"
)

st.title("🚀 InsightPilot AI")
st.markdown(
    "### AI-Powered Exploratory Data Analysis"
)

# ====================================
# Upload Dataset
# ====================================
uploaded_file = st.file_uploader(
    "📂 Upload Your Dataset",
    type=["csv"],
    help="Upload a CSV file for AI-powered analysis"
)
# ====================================
# Main Application
# ====================================
if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        # ==========================
        # Dataset Preview
        # ==========================
        st.subheader("📊 Dataset Preview")
        st.dataframe(df.head())

        # ==========================
        # Dataset Information
        # ==========================
        st.subheader("📋 Dataset Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        # ==========================
        # Data Types
        # ==========================
        st.subheader("🔍 Column Data Types")

        dtype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        st.dataframe(dtype_df)

        # ==========================
        # Summary Statistics
        # ==========================
        st.subheader("📈 Summary Statistics")

        numeric_df = df.select_dtypes(include="number")

        if len(numeric_df.columns) > 0:
            st.dataframe(numeric_df.describe())
        else:
            st.info("No numeric columns available.")

        # ==========================
        # Missing Values
        # ==========================
        st.subheader("❗ Missing Value Analysis")

        missing_df = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum()
        })

        st.dataframe(missing_df)

        total_missing = int(df.isnull().sum().sum())

        # ==========================
        # Correlation Matrix
        # ==========================
        if len(numeric_df.columns) > 1:

            st.subheader("🔗 Correlation Matrix")

            corr_matrix = numeric_df.corr()

            st.dataframe(corr_matrix)

        # ==========================
        # Correlation Heatmap
        # ==========================

        if len(numeric_df.columns) > 1:

            st.subheader("🔥 Correlation Heatmap")

            fig = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto"
            )

            st.plotly_chart(fig)


        # ==========================
        # Advanced Visualizations
        # ==========================

        st.subheader("📊 Advanced Visualizations")

        if len(numeric_df.columns) > 0:

            chart_type = st.selectbox(
                "Visualization Type",
                [
                    "Histogram",
                    "Box Plot",
                    "Scatter Plot",
                    "Line Chart",
                    "Bar Chart"
                ]
            )

            if chart_type == "Histogram":

                col = st.selectbox(
                    "Column",
                    numeric_df.columns,
                    key="hist"
                )

                fig = px.histogram(df, x=col)

            elif chart_type == "Box Plot":

                col = st.selectbox(
                    "Column",
                    numeric_df.columns,
                    key="box"
                )

                fig = px.box(df, y=col)

            elif chart_type == "Scatter Plot":

                x_col = st.selectbox(
                    "X Axis",
                    numeric_df.columns,
                    key="x"
                )

                y_col = st.selectbox(
                    "Y Axis",
                    numeric_df.columns,
                    key="y"
                )

                fig = px.scatter(
                    df,
                    x=x_col,
                    y=y_col
                )

            elif chart_type == "Line Chart":

                col = st.selectbox(
                    "Column",
                    numeric_df.columns,
                    key="line"
                )

                fig = px.line(
                    df,
                    y=col
                )

            elif chart_type == "Bar Chart":

                col = st.selectbox(
                    "Column",
                    numeric_df.columns,
                    key="bar"
                )

                fig = px.bar(
                    df,
                    y=col
                )

            st.plotly_chart(fig)

        # ==========================
        # AI Insights
        # ==========================
        st.subheader("🤖 AI Insights")

        try:

            summary_stats = ""

            if len(numeric_df.columns) > 0:
                summary_stats = numeric_df.describe().to_string()

            prompt = f"""
            Analyze the following dataset.

            Dataset Shape:
            {df.shape}

            Columns:
            {list(df.columns)}

            Summary Statistics:
            {summary_stats}

            Provide:

            1. Dataset Overview
            2. Key Trends
            3. Potential Anomalies
            4. Business Insights
            5. Recommended Next Analysis
            """

            model = genai.GenerativeModel(
                "gemini-2.5-flash"
            )

            response = model.generate_content(
                prompt
            )

            st.success("AI Insights Generated")
            st.write(response.text)

        except Exception:

            st.warning(
                "Gemini quota reached. Showing local insights."
            )

            st.subheader("📌 Automated Dataset Insights")

            st.write(f"""
            **Dataset Overview**

            - Total Rows: {df.shape[0]}
            - Total Columns: {df.shape[1]}
            - Missing Values: {total_missing}
            - Numeric Columns: {len(numeric_df.columns)}

            """)

            if len(numeric_df.columns) > 0:

                st.subheader("📈 Numeric Feature Summary")

                st.dataframe(
                    numeric_df.describe()
                )

                highest_variance = (
                    numeric_df.var()
                    .sort_values(ascending=False)
                    .head(1)
                )

                # ==========================
                # Smart Questions
                # ==========================

                st.subheader("❓ Smart Questions")

                questions = [
                    "What is the most important feature in this dataset?",
                    "Which column would be most useful for business decisions?",
                    "What data quality issues exist in this dataset?",
                    "Which feature appears to have the strongest influence on other variables?",
                    "What trends can be identified from the numeric data?",
                    "Which column contains the most diverse information?",
                    "What insights would an executive want to know first?",
                    "Which feature should be investigated further?",
                    "Is this dataset suitable for predictive analytics?",
                    "What are the top 3 findings from this dataset?"
                ]

                selected_question = st.selectbox(
                    "Select a question",
                    questions
                )

                numeric_df = df.select_dtypes(include="number")

                st.subheader("💡 Answer")

                if selected_question == questions[0]:

                    if len(numeric_df.columns) > 0:
                        important_feature = numeric_df.var().idxmax()
                        st.success(
                            f"The most important feature appears to be '{important_feature}' because it shows the highest variability."
                        )

                elif selected_question == questions[1]:

                    if len(numeric_df.columns) > 0:
                        business_feature = numeric_df.var().idxmax()
                        st.success(
                            f"'{business_feature}' may be the most useful column for business decision-making."
                        )

                elif selected_question == questions[2]:

                    total_missing = int(df.isnull().sum().sum())
                    duplicate_rows = int(df.duplicated().sum())

                    st.success(
                        f"Data Quality Report:\n\nMissing Values: {total_missing}\nDuplicate Rows: {duplicate_rows}"
                    )

                elif selected_question == questions[3]:

                    if len(numeric_df.columns) > 1:

                        corr = numeric_df.corr().abs()

                        corr_values = corr.unstack()
                        corr_values = corr_values[corr_values < 1]

                        strongest_pair = corr_values.idxmax()

                        st.success(
                            f"The strongest relationship is between '{strongest_pair[0]}' and '{strongest_pair[1]}'."
                        )

                elif selected_question == questions[4]:

                    st.success(
                        f"The dataset contains {len(numeric_df.columns)} numeric features that can be used for trend analysis."
                    )

                elif selected_question == questions[5]:

                    unique_counts = df.nunique()

                    st.success(
                        f"The most diverse column is '{unique_counts.idxmax()}' with {unique_counts.max()} unique values."
                    )

                elif selected_question == questions[6]:

                    st.success(
                        f"An executive would first want to know: Total Records = {df.shape[0]}, Total Features = {df.shape[1]}, Missing Values = {df.isnull().sum().sum()}."
                    )

                elif selected_question == questions[7]:

                    if len(numeric_df.columns) > 0:

                        feature = numeric_df.var().idxmax()

                        st.success(
                            f"'{feature}' should be investigated further because it has the highest variation."
                        )

                elif selected_question == questions[8]:

                    if len(numeric_df.columns) >= 2 and total_missing == 0:

                        st.success(
                            "Yes. This dataset appears suitable for predictive analytics because it contains multiple numeric features and no missing values."
                        )

                    else:

                        st.warning(
                            "The dataset may require cleaning before predictive modeling."
                        )

                elif selected_question == questions[9]:

                    st.success(
                        f"""
                Top 3 Findings:

                1. Dataset contains {df.shape[0]} records and {df.shape[1]} columns.

                2. Missing values detected: {df.isnull().sum().sum()}.

                3. Numeric features available: {len(numeric_df.columns)}.
                """
                    )


    except Exception as e:

        st.error(
            f"Error processing dataset: {e}"
        )

else:

    st.info(
        "Upload a CSV file to begin analysis."
    )