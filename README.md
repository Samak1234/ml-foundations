# Used Car Price Prediction

Machine learning project for predicting used-car selling prices and comparing regression models.

## Overview

The project covers the complete regression workflow from data preprocessing to model evaluation and error analysis.

### Models
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Workflow
- Data cleaning and duplicate removal
- Categorical feature encoding
- Feature engineering with `Car_Age`
- Train/test splitting
- Model training and comparison
- Hyperparameter experimentation with Random Forest
- Prediction error and residual analysis

## Evaluation

Models are compared using:

- MAE
- RMSE
- R² Score

The project also analyzes the largest prediction errors and Linear Regression coefficients to better understand model behavior.

## Tech Stack

Python · Pandas · Scikit-learn · Matplotlib

## Run

```bash
git clone https://github.com/Samak1234/used-car-price-prediction.git
cd used-car-price-prediction
pip install pandas scikit-learn matplotlib
python car_price_model.py
```

## Project Structure

```text
used-car-price-prediction/
├── car_price_model.py
├── car_prediction_data.csv
├── metrics.py
├── plots/
└── README.md
```

## Status

Currently improving model selection and preparing the model for deployment.
