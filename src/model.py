from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

def train_linear_regression(X_train, X_test, y_train, y_test):
    # Feature names (since X_train is scaled and loses column names)
    feature_names = ["RM", "LSTAT", "PTRATIO", "INDUS"]

    # Initialize the model
    model = LinearRegression()
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")

    # Feature Importance (coefficients)
    feature_importance = pd.DataFrame({'Feature': feature_names, 'Coefficient': model.coef_})
    feature_importance['Abs_Coefficient'] = feature_importance['Coefficient'].abs()  
    feature_importance = feature_importance.sort_values(by='Abs_Coefficient', ascending=False)

    print("\nFeature Importance:")
    print(feature_importance[['Feature', 'Coefficient']])

    return model
