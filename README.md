# 1000_companies_ML_Predictions
## Machine Learning Performance: Profit Analysis Dashboard

## Overview
This project leverages a machine learning model to predict profit values for a dataset of 1000 companies and visualizes the model’s performance using a Power BI dashboard. The dashboard enables users to compare actual profits with model predictions, assess the accuracy of the model, and gain insights into how variables like R&D spend, administrative costs, and marketing spend contribute to profit.

## Key Features
Machine Learning Model Accuracy: Displays the accuracy of the machine learning model (Linear Regression) as a percentage, using the R² score to indicate how well the model's predictions match actual profit values.
KPI Over Index: Shows a KPI visualization tracking the model's predicted profit against actual profit values across an index.
Profit vs Prediction Scatter Plot: Provides a scatter plot to compare the actual profits and predicted profits across different states (California, Florida, New York).
Profit vs Prediction Over Index: Line chart showing the trends of actual and predicted profit values over an index range.
Profit vs Prediction by Bar Chart: A bar chart comparing sums of actual profit and predictions for each index, allowing for straightforward visual comparison.
Detailed Data Table: A table view that includes values such as administrative spend, marketing spend, R&D spend, and both actual and predicted profit for each data point.

## Machine Learning Model Details
The project uses a Linear Regression model to predict profit based on the following features:

R&D Spend
Administration
Marketing Spend

## The model was trained and evaluated as follows:

Data Preprocessing: The dataset was split into training and testing sets.
Model Training: A LinearRegression model from scikit-learn was fitted to the training data.
Evaluation: Model accuracy was measured using the R² score, which quantifies the percentage of variance explained by the model's predictions.
Predictions: The model's predictions on test data were visualized alongside actual profits, and the predictions were added to the dataset for use in the Power BI dashboard.

## The code for ML:
<a href="https://github.com/harshithp2004/LokSabha_ElectionResult2024_Dashboard/blob/main/ml_integrated_LokSabha2024.py">ml_integrated_LokSabha2024</a>

