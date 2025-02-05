# Import the necessary functions
from load_data import load_data
from handle_missing_values import handle_missing_values
import matplotlib.pyplot as plt
import seaborn as sns
from preprocess import preprocess_data
from model import train_linear_regression
from tuning import tune_hyperparameters
import pickle

# Step 1: Load the dataset
file_path = 'data/HousingData.csv'  # Adjust the path if necessary
df = load_data(file_path)

# Step 2: Handle missing values
data = handle_missing_values(df)

# Step 3: Check if there are still missing values
print("Missing Values After Handling:")
print(data.isnull().sum())

# step 4: Save the cleaned dataset
data.to_csv('data/HousingData.csv', index=False)

# 1. Dataset Overview
print("Dataset Summary:")
print(data.describe())  # Summary of the data
print("\nCorrelation with MEDV:")
print(data.corr()['MEDV'].sort_values(ascending=False))  # Correlation with target

# 2. Correlation Heatmap (Top Relationships)
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# 3. Distribution of MEDV (Target Variable)
plt.figure(figsize=(6, 4))
sns.histplot(data['MEDV'], kde=True, bins=30)
plt.title('Distribution of MEDV')
plt.xlabel('MEDV')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plots (Top Features vs MEDV)
top_features = ['LSTAT', 'RM', 'PTRATIO']  # Key features most likely to affect MEDV
for feature in top_features:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=data[feature], y=data['MEDV'], alpha=0.7)
    plt.title(f'{feature} vs MEDV')
    plt.xlabel(feature)
    plt.ylabel('MEDV')
    plt.show()



# Apply preprocessing
X_train, X_test, y_train, y_test = preprocess_data(df)
print("Data preprocessing completed successfully!")


# Train and evaluate the Linear Regression model
model = train_linear_regression(X_train, X_test, y_train, y_test)

# Tune hyperparameters
best_ridge, best_lasso = tune_hyperparameters(X_train, y_train, X_test, y_test)


# Save the trained Ridge model
with open("src/best_model.pkl", "wb") as f:
    pickle.dump(best_ridge, f)


