# sprint7-vehicle-eda-dashboard

EDA dashboard for vehicle listings with interactive visualizations built with Streamlit.

---

# 🚗 Vehicle Data Analysis Dashboard

## 📌 Project Description

This project is an interactive web application developed with Streamlit for exploratory data analysis (EDA) of used vehicle listings.

The dashboard allows users to analyze vehicle market data through interactive visualizations and dynamic analytical tools. The application explores relationships between variables such as vehicle prices, mileage, vehicle types, and market behavior.

The project follows a multi-page structure that organizes the analysis into different sections:
- Market Overview
- Price Analysis
- Vehicle Segmentation
- Market Trends
- Interactive Analysis

---

## 🎯 Project Objective

The main objective of this project is to apply exploratory data analysis techniques and interactive visualization methods to analyze a dataset of used vehicle advertisements.

The dashboard helps users:
- explore the dataset,
- identify pricing patterns,
- analyze vehicle characteristics,
- detect market trends,
- and interact dynamically with visualizations.

---

## 🧰 Main Features

### ✔ Dataset Exploration
- Vehicle dataset loading and processing
- Dataset preview visualization
- Descriptive statistics analysis

### ✔ Interactive Visualizations
- Interactive histograms
- Interactive scatter plots
- Dynamic chart rendering

### ✔ Exploratory Data Analysis (EDA)
- Vehicle price distribution analysis
- Mileage analysis
- Price vs odometer relationship analysis
- Market trend exploration

### ✔ Interactive Components
- Checkboxes to display visualizations
- Buttons for interactive actions
- Random vehicle sample visualization

### ✔ Data Cleaning
- Missing values handling (`None` / `NaN`)
- Clean dataframe display for improved readability

---

## ✅ Project Requirements Fulfilled

This project fulfills all required evaluation criteria:

| Requirement | Status |
|---|---|
| At least one header with text | ✅ Completed |
| At least one histogram | ✅ Completed |
| At least one scatter plot | ✅ Completed |
| At least one button or checkbox | ✅ Completed |

---

## 📊 Interactive Analysis Section

The application includes a dedicated **Interactive Analysis** page containing the required interactive visualizations and components.

### Histogram
The dashboard includes a histogram visualization used to analyze the distribution of vehicle prices.

### Scatter Plot
The application includes a scatter plot showing the relationship between:
- vehicle mileage (`odometer`)
- and vehicle price.

### Interactive Components
Users can dynamically interact with the dashboard using:
- checkboxes,
- and buttons.

---

## 🧹 Missing Values Handling

To improve dashboard readability and presentation quality, missing values are removed from the random dataframe sample displayed in the application.

Example:

```python
clean_sample = df.dropna(
    subset=['price', 'odometer', 'model']
).sample(5)

