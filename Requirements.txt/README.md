# Industrial-Energy-Consumption-Optimizer
An AI-powered system to analyze and forecast industrial energy usage. Developed using Python and Machine Learning (Random Forest, Decision Tree) to identify consumption patterns, optimize load distribution, and reduce operational costs based on environmental factors
The Industrial Energy Consumption Optimizer is a data-driven solution designed to analyze historical energy usage and predict future demand for industrial facilities. By leveraging Advanced Excel for data engineering and Machine Learning (XGBoost) for forecasting, this project helps industries optimize their energy procurement and reduce operational costs.
  
**🛤️ Development Roadmap**

Step 1: Data Engineering (Advanced Excel)
Action: Processed and sanitized a dataset containing over 50,000 rows of raw industrial energy records.
Techniques: Leveraged Power Query for automated data cleaning, utilized DAX to create calculated columns (like custom time-frames), and performed trend analysis using Pivot Tables.
Outcome: Transformed messy raw data into a structured, high-quality dataset optimized for Machine Learning.

Step 2: Machine Learning Pipeline (Python)
Action: Developed a high-performance predictive engine using the XGBoost Regressor algorithm.
Feature Engineering: Integrated key variables including Temperature, Production Work Levels (Low/Medium/High), and Time-series components (Hour, Day, Month).
Performance: Achieved superior accuracy by fine-tuning hyperparameters and validating results with R2 Score and Mean Absolute Error (MAE).

Step 3: Web Deployment (Streamlit)
Action: Engineered an interactive web dashboard using the Streamlit framework.
Key Features: * Dynamic CSV Upload: Users can upload their specific industrial datasets for instant analysis.
Real-time Predictor: A manual input interface that predicts energy demand based on current temperature and scheduled production loads.

3. Repository Description & Tags

**Excel → Python → Machine Learning → XGBoost → Streamlit → Data Analytics → Energy Forecasting**

**Project Overview**
Energy management is critical for large-scale industries. This project provides an end-to-end pipeline:
Data Engineering: Cleaning and structuring raw industrial data using Excel.
Predictive Modeling: Training a robust ML model to forecast energy needs (MW).
Deployment: An interactive Streamlit dashboard for real-time analysis and custom predictions.

**Tech Stack**
Data Processing: Advanced Excel (Power Query, DAX, Pivot Tables)
Programming: Python 3.x
Machine Learning: XGBoost Regressor, Scikit-learn
Data Visualization: Matplotlib, Seaborn
Web Framework: Streamlit (UI/UX)

**Project Workflow**
1. Advanced Excel Processing
Before feeding data into the model, the raw dataset was refined in Excel:
Data Sanitization: Removed null values and handled outliers.
Feature Extraction: Used DAX to create time-based features and Pivot Tables to identify seasonal trends.
Constraint Mapping: Filtered core variables like Temperature, Production Work Levels, and Time-series data.

2. Machine Learning Development
The core logic resides in the Energy_consumption_optimizer.ipynb notebook:
Feature Selection: The model uses Hour, Day of Week, Month, Temperature, and Production Level (1-3) as primary drivers.
Algorithm: Implemented XGBoost, an optimized gradient boosting library, to capture non-linear relationships in energy demand.
Validation: Evaluated using R2 Score and MAE to ensure high prediction accuracy.

3. Streamlit Web Application (app.py)
The application allows users to interact with the data without writing code:
Dynamic Upload: Users can upload their own company CSV files to run the analysis.
Visual Insights: Displays "Which factors drive consumption most?" and "Consumption vs. Temperature" trends.
Real-time Predictor: A dedicated calculator where users input variables (e.g., 35°C at Production Level 3) to get an immediate energy estimate in MW.
