# InsightPilot-AI

## Project Overview

InsightPilot-AI is an AI-powered data analysis assistant that allows users to upload CSV datasets and receive automated insights using Google's Gemini AI model.

## Features

* CSV Dataset Upload
* Dataset Preview
* Dataset Schema Analysis
* AI-Generated Dataset Summary
* Streamlit-Based User Interface

## Tech Stack

* Python
* Streamlit
* Pandas
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

## Project Structure

```text
InsightPilot-AI/
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── data/
└── utils/
```
