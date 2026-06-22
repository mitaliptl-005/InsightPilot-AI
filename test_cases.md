# InsightPilot-AI Test Cases

## TC-01: Upload Valid Dataset

**Input:** Ecommerce Dataset CSV

**Expected Result:**

* Dataset uploads successfully
* Dataset preview displayed
* Dataset information generated

**Status:** Pass

---

## TC-02: Automatic Domain Detection

**Input:** Ecommerce Dataset

**Expected Result:**

* System identifies dataset as Ecommerce
* Relevant business questions generated automatically

**Status:** Pass

---

## TC-03: Smart Question Generation

**Input:** Dataset with Product, Revenue, Customer columns

**Expected Result:**

* Domain-specific questions displayed
* Questions differ from Real Estate or Employee datasets

**Status:** Pass

---

## TC-04: Smart Question Answering

**Input:** Select a generated business question

**Expected Result:**

* Appropriate answer generated
* Answer displayed below question

**Status:** Pass

---

## TC-05: Dataset Preview

**Input:** Any valid CSV

**Expected Result:**

* First five rows displayed
* Data rendered correctly

**Status:** Pass

---

## TC-06: Data Type Detection

**Input:** Mixed-type dataset

**Expected Result:**

* Numeric columns identified
* Categorical columns identified

**Status:** Pass

---

## TC-07: Missing Value Analysis

**Input:** Dataset containing null values

**Expected Result:**

* Missing value counts displayed correctly

**Status:** Pass

---

## TC-08: Summary Statistics Generation

**Input:** Dataset with numeric columns

**Expected Result:**

* Mean, Min, Max, Std Dev generated

**Status:** Pass

---

## TC-09: Correlation Matrix

**Input:** Dataset with multiple numeric columns

**Expected Result:**

* Correlation matrix displayed

**Status:** Pass

---

## TC-10: Correlation Heatmap

**Input:** Dataset with multiple numeric columns

**Expected Result:**

* Interactive heatmap generated

**Status:** Pass

---

## TC-11: Histogram Visualization

**Input:** Numeric dataset

**Expected Result:**

* Histogram generated successfully

**Status:** Pass

---

## TC-12: Scatter Plot Visualization

**Input:** Dataset with at least two numeric columns

**Expected Result:**

* Scatter plot generated

**Status:** Pass

---

## TC-13: Box Plot Visualization

**Input:** Dataset with numeric columns

**Expected Result:**

* Outlier visualization displayed

**Status:** Pass

---

## TC-14: Line Chart Visualization

**Input:** Time-series or numeric dataset

**Expected Result:**

* Trend visualization displayed

**Status:** Pass

---

## TC-15: Bar Chart Visualization

**Input:** Dataset with categorical/numeric values

**Expected Result:**

* Comparison chart displayed

**Status:** Pass

---

## TC-16: AI Insight Generation

**Input:** Valid dataset with Gemini API available

**Expected Result:**

* AI-generated business insights displayed

**Status:** Pass / Quota Dependent

---

## TC-17: AI Fallback Mode

**Input:** Gemini quota exceeded

**Expected Result:**

* Local automated insights generated
* Application remains functional

**Status:** Pass

---

## TC-18: Predictive Analytics Readiness Check

**Input:** Clean dataset with multiple numeric features

**Expected Result:**

* Dataset suitability assessment displayed

**Status:** Pass

---

## TC-19: Invalid File Upload

**Input:** TXT, XLSX, or unsupported format

**Expected Result:**

* Upload rejected gracefully

**Status:** Pass

---

## TC-20: End-to-End Workflow

**Workflow:**

Upload Dataset
→ Domain Detection
→ Smart Questions
→ Dataset Preview
→ EDA
→ Visualizations
→ AI Insights

**Expected Result:**

* Complete workflow executes successfully without crashes

**Status:** Pass
