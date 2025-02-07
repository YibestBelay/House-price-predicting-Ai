# House Price Prediction Application

This project is a **House Price Prediction Application** built using **FastAPI** for the backend and a Streamlit-based frontend. The application predicts house prices based on various input features, utilizing a trained Ridge Regression model. The backend is deployed on **Render**, and the application provides a seamless user experience.

---

## Features

- **FastAPI Backend**:
  - API endpoints for predicting house prices.
  - CORS middleware to allow frontend-backend communication.

- **Streamlit Frontend**:
  - User-friendly interface to input features for prediction.
  - Instant prediction results displayed on the screen.

- **Machine Learning Model**:
  - Trained Ridge Regression model using Boston Housing Dataset.
  - Includes preprocessing, feature selection, and model evaluation.

---

## Tech Stack

### Backend:
- FastAPI
- Python (pandas, numpy, scikit-learn)
- Render (for deployment)

### Frontend:
- Streamlit

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd HousePricePrediction
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Backend:**
   ```bash
   uvicorn src.api:app --reload
   ```

4. **Run the Frontend:**
   ```bash
   streamlit run src/frontend.py
   ```

---

## Deployment

### Backend on Render:

1. **Create a new Web Service on Render:**
   - Use the repository URL.
   - Set the environment as Python.
   - Add `uvicorn src.api:app --host 0.0.0.0 --port 8000` as the start command.

2. **Configure Environment Variables:**
   - Add necessary variables like `PYTHONUNBUFFERED=1`.

3. **Deploy the Service.**

### Frontend Deployment:

1. Host the Streamlit app on **Streamlit Cloud** or another suitable platform.

2. Ensure the deployed frontend fetches the correct API endpoint from the deployed backend.

---

## Usage

1. Access the deployed Streamlit app.
2. Input the required features:
   - Average number of rooms (RM).
   - Percentage of lower status of the population (LSTAT).
   - Pupil-teacher ratio (PTRATIO).
   - Proportion of non-retail business acres per town (INDUS).
3. Click on **Predict Price**.
4. View the predicted house price.

---

## File Structure

```plaintext
HousePricePrediction/
├── src/
│   ├── api.py               # FastAPI backend code
│   ├── frontend.py          # Streamlit frontend code
│   └── best_model.pkl       # Trained Ridge Regression model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Acknowledgments

- **Dataset**: Boston Housing Dataset
- **Libraries**: FastAPI, Streamlit, pandas, numpy, scikit-learn

---

## License

This project is licensed under the MIT License.
