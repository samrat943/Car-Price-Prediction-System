# 🚗 Car Price Prediction System

An end-to-end machine learning system built to accurately estimate used car market valuations based on vehicle specifications, historical depreciation, and market trends.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

---

## 📌 Project Overview

Used car pricing is highly non-linear, influenced by factors such as vehicle age, mileage, brand prestige, fuel type, and transmission. This project provides an automated, reproducible machine learning pipeline that:
* Ingests, cleans, and encodes multi-attribute vehicle sales records.
* Mitigates skewness and handles outliers across continuous variables (e.g., odometer reading, engine capacity).
* Trains and benchmarks multiple regression architectures to determine the optimal pricing model.
* Exposes a reusable inference pipeline for instant price estimates.

---

## 🚀 Key Features

* **Data Cleaning & Wrangling:** Automated processing for missing values, structural anomalies, and categorical encoding (One-Hot / Target Encoding).
* **Feature Engineering:** Derivation of high-signal variables such as vehicle age, power-to-weight ratios, and mileage depreciation bands.
* **Model Benchmarking:** Comparison of multiple regression algorithms, including Linear Regression, Decision Trees, Random Forest, and Gradient Boosting (XGBoost/LightGBM).
* **Hyperparameter Optimization:** Automated tuning via Grid / Random Search with cross-validation to prevent overfitting.
* **Model Explainability:** Evaluation of feature importance to quantify which vehicle attributes impact depreciation the most.

---

## 📁 Repository Structure

```text
Car-Price-Prediction-System/
├── data/
│   ├── raw/               # Original vehicle sales dataset
│   └── processed/         # Cleaned, encoded, and scaled features
├── models/                # Serialized trained models (.pkl / .joblib)
├── notebooks/             # EDA, distribution plots, and prototype experiments
├── src/
│   ├── preprocess.py      # Cleaning routines, categorical encoders, and scalers
│   ├── feature_eng.py     # Feature extraction and engineering pipeline
│   ├── train.py           # Training loops, hyperparameter tuning, and logging
│   └── predict.py         # Inference pipeline for new vehicle inputs
├── requirements.txt       # Project dependencies
└── README.md
