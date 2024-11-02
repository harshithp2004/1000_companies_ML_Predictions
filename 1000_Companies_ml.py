import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('C:/Users/Harshith/Documents/1000_Companies.csv')

# Define features and target
features = ['R&D Spend', 'Administration', 'Marketing Spend']
target = ['Profit']

X = df[features]
y = df[target]

# Create train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Train the model
lin = LinearRegression()
lin.fit(X_train, y_train)

# Predict values
y_pred = lin.predict(X_test)

# Calculate accuracy (R^2 score)
accuracy = r2_score(y_test, y_pred)

# Create an accuracy dataframe
accuracy_df = pd.DataFrame({"Accuracy (%)": [accuracy * 100]})

# Add predictions to the original df
df["Predictions"] = lin.predict(X)

# Optionally, add accuracy to the dataset for visualization
df["Model Accuracy"] = accuracy * 100

# Return both dataframes combined
combined_df = pd.concat([df, accuracy_df], axis=1)
