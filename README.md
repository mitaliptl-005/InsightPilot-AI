# InsightPilot-AI

## Project Overview

InsightPilot-AI is an AI-powered data analytics assistant that allows users to upload CSV datasets and receive automated insights, visualizations, and business intelligence recommendations using Exploratory Data Analysis (EDA) and Google's Gemini AI model.

## Features

* CSV Dataset Upload
* Dataset Preview
* Dataset Information Summary
* Data Type Detection
* Missing Value Analysis
* Summary Statistics
* Correlation Matrix
* Smart Questions & Answers
* AI-Generated Insights
* Automated Fallback Insights
* Advanced Visualizations

  * Histogram
  * Box Plot
  * Scatter Plot
  * Line Chart
  * Bar Chart
* Streamlit-Based User Interface

## Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* Google Gemini API
* Python Dotenv

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Run the Application

```bash
python -m streamlit run app.py
```

## Application Workflow

```text
Upload CSV Dataset
→ Dataset Preview
→ Smart Questions
→ Summary Statistics
→ Missing Value Analysis
→ Correlation Analysis
→ Advanced Visualizations
→ AI Insights / Fallback Insights
```

## Baseline Results

* CSV Upload Working
* Smart Questions Working
* Missing Value Analysis Working
* Correlation Analysis Working
* Advanced Visualizations Working
* AI Insights Working (Quota Dependent)
* Fallback Insights Working

## Project Structure

```text
InsightPilot-AI/
├── app.py
├── requirements.txt
├── README.md
├── test_cases.md
├── .env
├── .gitignore
├── data/
└── screenshots/
```

## Future Improvements

* Automatic Dataset Domain Detection
* AI-Generated Dynamic Questions
* Predictive Analytics
* Automated Report Generation
* Downloadable Insight Reports

## Author

Developed as part of the DDS Building AI Applications Challenge 2026.
