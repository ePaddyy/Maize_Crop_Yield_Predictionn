import streamlit as st
import pandas as pd
import joblib
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ghana Maize Predictor", page_icon="🌽")

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    model_path = "../models/maize_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error("Model not found! Please run the training notebook first.")
        return None

model = load_model()

# --- UI HEADER ---
st.title("🌽 Ghana Maize Yield Predictor")
st.markdown("""
This AI tool predicts maize yield (tons/hectare) for Ghanaian farmers.
It uses **Climate Data**, **Soil Type**, and **Historical Performance**.
""")

# --- SIDEBAR INPUTS ---
st.sidebar.header("1. Farm Details")

# Climate Inputs (Defaults set to Ghana averages)
rain = st.sidebar.number_input("Total Rainfall (mm) - Major Season", 0, 2000, 600)
temp = st.sidebar.number_input("Avg Temperature (°C)", 20.0, 40.0, 28.0)
humidity = st.sidebar.slider("Relative Humidity (%)", 0, 100, 75)
sun = st.sidebar.number_input("Solar Radiation (MJ/m²)", 0.0, 30.0, 18.0)
soil_moist = st.sidebar.slider("Soil Moisture Index (0-1)", 0.0, 1.0, 0.5)

# Soil & Location
soil_type = st.sidebar.selectbox("Soil Type", 
    ['Forest Ochrosol', 'Savanna Ochrosol', 'Coastal Savannah', 'Tropical Black Earth'])

# The "Secret Sauce" Input (Lag Feature)
st.sidebar.header("2. History")
lag_yield = st.sidebar.number_input("Yield from Previous Year (tons/ha)", 0.0, 10.0, 2.0, 
    help="How much maize did this farm produce last year? This is crucial for accuracy.")

# Year & Policy
year = st.sidebar.number_input("Prediction Year", 2024, 2030, 2025)
pest = st.sidebar.checkbox("Is there a Pest Outbreak (e.g. Armyworm)?", False)
policy = st.sidebar.checkbox("Is 'Planting for Food & Jobs' Active?", True)

# --- PREDICTION LOGIC ---
if st.button("Predict Yield 🚀"):
    if model:
        # Create Dataframe matching the training columns EXACTLY
        input_data = pd.DataFrame({
            'Rainfall': [rain],
            'Temperature': [temp],
            'Humidity': [humidity],
            'Sunlight': [sun],
            'Soil_Moisture': [soil_moist],
            'Soil_Type': [soil_type],
            'Pest_Risk': [1 if pest else 0],
            'PFJ_Policy': [1 if policy else 0],
            'Year': [year],
            'Yield_Lag1': [lag_yield]  # This is the new key feature
        })
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        # Display
        st.success(f"🌱 Estimated Yield: **{prediction:.2f} tons/hectare**")
        
        # Interpretation
        bags = int(prediction * 10) # Approx 100kg bags
        st.info(f"This is approximately **{bags} bags** (100kg) per hectare.")
        
        if prediction < 1.5:
            st.warning("⚠️ Low Yield Alert: Consider checking soil fertility or irrigation.")
        elif prediction > 2.5:
            st.balloons()
            st.markdown("🌟 **Excellent!** Conditions are favorable for a bumper harvest.")