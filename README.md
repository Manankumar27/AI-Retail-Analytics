# AI Retail Analytics & Forecasting Platform

## Overview

AI Retail Analytics & Forecasting Platform is a Flask-based Data Science and Machine Learning application designed to analyze retail sales data, generate business insights, and forecast future sales trends using the Sample Superstore dataset.

The platform provides interactive dashboards, AI-driven business insights, and machine learning-based sales forecasting through a modern web interface.

---

## Features

### Dashboard

* Total Sales Analysis
* Total Profit Analysis
* Total Orders Tracking
* Average Discount Monitoring
* Sales by Category Visualization
* Profit by Region Analysis
* Monthly Sales Trend Analysis
* Top Products Performance Analysis

### AI Insights

* Best Performing Category
* Least Performing Category
* Most Profitable Region
* Highest Revenue Product
* Automated Business Recommendations

### Sales Forecasting

* Linear Regression Forecasting Model
* Next Month Sales Prediction
* Expected Growth Rate Calculation
* Actual vs Forecast Sales Visualization
* Interactive Forecast Charts

---

## Technology Stack

### Backend

* Python
* Flask

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Linear Regression

### Data Visualization

* Plotly

### Frontend

* HTML5
* CSS3
* Bootstrap 5

---

## Project Structure

```text
AI_Retail_Analytics/
│
├── app.py
│
├── dataset/
│   └── Sample - Superstore.csv
│
├── models/
│   ├── analytics.py
│   ├── forecast.py
│   └── gemini_helper.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   ├── insights.html
│   └── forecast.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Retail-Analytics-Flask.git
```

### Navigate to Project

```bash
cd AI-Retail-Analytics-Flask
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Machine Learning Model

The forecasting module uses a Linear Regression model to predict future sales based on historical monthly sales data.

### Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Sales Prediction
6. Forecast Visualization

---

## Dataset

Sample Superstore Dataset

Dataset contains information related to:

* Orders
* Sales
* Profit
* Discount
* Customers
* Products
* Regions
* Categories

---

## Future Enhancements

* Gemini AI Integration
* Customer Segmentation
* Advanced Forecasting Models
* PDF Report Generation
* Cloud Deployment
* User Authentication

---

## Developer

**Manan Kumar**

AI Retail Analytics & Forecasting Platform

---

## Screenshots

### Dashboard
* (screenshots/dashboard.png)

### AI Insights
* (screenshots/insights.png)

### Forecasting
* (screenshots/forecast.png)

---

## License

This project is developed for educational and academic purposes.
