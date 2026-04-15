import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# --- Page Config ---
st.set_page_config(page_title="Industrial Energy Optimizer", layout="wide")

st.title("Industrial Energy Consumption Optimizer")
st.markdown("""
Please upload your company's historical data (CSV) to analyze energy patterns and generate future predictions."
""")

# --- Sidebar: File Upload ---
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your Industrial CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data Uploaded Successfully!")

    # Basic Data Cleaning
    if 'Datetime' in df.columns:
        df['Datetime'] = pd.to_datetime(df['Datetime'])
    
    # --- Tabs for Organization ---
    tab1, tab2, tab3 = st.tabs(["Data Analysis", " Model Training", "Real-time Prediction"])

    with tab1:
        st.header("Exploratory Data Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Data Preview")
            st.write(df.head())
        
        with col2:
            st.subheader("Correlation Heatmap")
            fig, ax = plt.subplots()
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)

        st.subheader("Energy Consumption Trend (First 500 hours)")
        fig2, ax2 = plt.subplots(figsize=(12, 4))
        ax2.plot(df['Energy_MW'][:500])
        ax2.set_ylabel("Energy (MW)")
        st.pyplot(fig2)

    with tab2:
        st.header("Model Performance & Training")
        
        # Features and Target
        X = df[['Hour', 'DayOfWeek', 'Month', 'Temperature', 'Production_Level']]
        y = df['Energy_MW']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train Model
        model = XGBRegressor(n_estimators=100, learning_rate=0.1)
        model.fit(X_train, y_train)
        
        # Predictions
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        # Metrics Display
        m1, m2 = st.columns(2)
        m1.metric("Model Accuracy (R2 Score)", f"{r2*100:.2f}%")
        m2.metric("Mean Absolute Error", f"{mae:.2f} MW")
        
        st.subheader("Actual vs Predicted Comparison")
        fig3, ax3 = plt.subplots(figsize=(10, 4))
        ax3.plot(y_test.values[:100], label="Actual", alpha=0.7)
        ax3.plot(y_pred[:100], label="Predicted", linestyle="--")
        ax3.legend()
        st.pyplot(fig3)

    with tab3:
        st.header("Predict Future Consumption")
        st.info("Adjust the values given below for prediction.:")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            in_hour = st.slider("Hour of Day", 0, 23, 12)
            in_temp = st.number_input("Temperature (°C)", value=30.0)
        with c2:
            in_day = st.selectbox("Day of Week", options=[0,1,2,3,4,5,6], format_func=lambda x: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][x])
            in_prod = st.selectbox("Production Level", options=[1, 2, 3], format_func=lambda x: f"Level {x}")
        with c3:
            in_month = st.slider("Month", 1, 12, 6)

        if st.button("Calculate Energy Demand"):
            input_df = pd.DataFrame([[in_hour, in_day, in_month, in_temp, in_prod]], 
                                    columns=['Hour', 'DayOfWeek', 'Month', 'Temperature', 'Production_Level'])
            res = model.predict(input_df)[0]
            st.success(f"Estimated Energy Requirement: **{res:.2f} MW**")
            
            # Advice logic
            if res > df['Energy_MW'].mean() + df['Energy_MW'].std():
                st.warning("⚠️ High Demand Detected! Consider rescheduling heavy loads.")
            else:
                st.info("✅ Demand is within normal industrial limits.")

else:
    st.info("Please upload your company's CSV file from the sidebar to activate the dashboard.")