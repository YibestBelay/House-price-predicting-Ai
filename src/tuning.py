import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def tune_hyperparameters(X_train, y_train, X_test, y_test):
    # Ridge Regression (L2 Regularization)
    ridge_params = {'alpha': [0.01, 0.1, 1, 10, 100]}
    ridge = GridSearchCV(Ridge(), ridge_params, scoring='r2', cv=5)
    ridge.fit(X_train, y_train)
    best_ridge = ridge.best_estimator_

    # Lasso Regression (L1 Regularization)
    lasso_params = {'alpha': [0.01, 0.1, 1, 10, 100]}
    lasso = GridSearchCV(Lasso(), lasso_params, scoring='r2', cv=5)
    lasso.fit(X_train, y_train)
    best_lasso = lasso.best_estimator_

    # Evaluate Ridge Model
    ridge_preds = best_ridge.predict(X_test)
    ridge_mse = mean_squared_error(y_test, ridge_preds)
    ridge_r2 = r2_score(y_test, ridge_preds)

    # Evaluate Lasso Model
    lasso_preds = best_lasso.predict(X_test)
    lasso_mse = mean_squared_error(y_test, lasso_preds)
    lasso_r2 = r2_score(y_test, lasso_preds)

    print("Best Ridge Alpha:", ridge.best_params_['alpha'])
    print("Ridge MSE:", round(ridge_mse, 2), "| Ridge R²:", round(ridge_r2, 2))

    print("Best Lasso Alpha:", lasso.best_params_['alpha'])
    print("Lasso MSE:", round(lasso_mse, 2), "| Lasso R²:", round(lasso_r2, 2))

    return best_ridge, best_lasso
