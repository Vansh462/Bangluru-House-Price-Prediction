import streamlit as st
import json
import pickle
import numpy as np
import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Bangalore House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global variables for model and data
@st.cache_data
def load_artifacts():
    """Load the saved model and location data"""
    try:
        # Load columns data
        with open("artifacts/columns.json", 'r') as f:
            data_columns = json.load(f)['data_columns']
            locations = data_columns[3:]  # First 3 are sqft, bath, bhk

        # Load the trained model
        with open("artifacts/bengaluru_House_Data.pkl", 'rb') as f:
            model = pickle.load(f)
        
        return model, data_columns, locations
    except Exception as e:
        st.error(f"Error loading model artifacts: {e}")
        return None, None, None

def predict_price(location, total_sqft, bath, bhk, model, data_columns):
    """Predict house price based on input parameters"""
    try:
        # Find location index
        try:
            loc_index = data_columns.index(location.strip().lower())
        except:
            loc_index = -1
        
        # Create input array
        x = np.zeros(len(data_columns))
        x[0] = total_sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
        
        # Make prediction
        predicted_price = model.predict([x])[0]
        return round(predicted_price, 2)
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None

def main():
    # Load model and data
    model, data_columns, locations = load_artifacts()
    
    if model is None:
        st.error("Failed to load model. Please check if the artifacts exist.")
        return
    
    # App header
    st.title("🏠 Bangalore House Price Predictor")

    # Add GitHub link in header
    col_title, col_github = st.columns([3, 1])
    with col_github:
        st.markdown("""
        <div style='text-align: right; padding-top: 10px;'>
            <a href="https://github.com/Vansh462/Bangluru-House-Price-Prediction" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-View%20Code-black?style=for-the-badge&logo=github" alt="GitHub">
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Predict house prices in Bangalore based on location, size, and amenities")

    # Sidebar with additional info
    with st.sidebar:
        st.header("📋 About This App")
        st.markdown("""
        This ML model predicts house prices in Bangalore using:
        - **Linear Regression** algorithm
        - **13K+ property records** (cleaned dataset)
        - **85%+ accuracy** on test data
        """)

        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        [![GitHub](https://img.shields.io/badge/GitHub-View%20Code-black?style=flat-square&logo=github)](https://github.com/Vansh462/Bangluru-House-Price-Prediction)

        [![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blue?style=flat-square&logo=vercel)](https://portfolio-vob.vercel.app/)
        """)

        st.markdown("---")
        st.header("📊 Model Info")
        st.markdown("""
        - **Algorithm**: Linear Regression
        - **Features**: Location, Area, BHK, Bathrooms
        - **Dataset**: Bangalore Housing Data
        - **Preprocessing**: Outlier removal, feature engineering
        """)

    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter Property Details")
        
        # Location selection
        location = st.selectbox(
            "📍 Select Location",
            options=sorted(locations),
            help="Choose the area/locality in Bangalore"
        )
        
        # Area input
        total_sqft = st.number_input(
            "📐 Total Area (Square Feet)",
            min_value=300,
            max_value=10000,
            value=1000,
            step=50,
            help="Enter the total area of the property"
        )
        
        # BHK selection
        bhk = st.number_input(
            "🛏️ BHK (Bedrooms)",
            min_value=1,
            max_value=20,
            value=2,
            step=1,
            help="Number of bedrooms (1-20 based on actual data)"
        )

        # Bathrooms selection
        bath = st.number_input(
            "🚿 Bathrooms",
            min_value=1,
            max_value=15,
            value=2,
            step=1,
            help="Number of bathrooms (typically BHK + 2 or less)"
        )
        
        # Validation warning
        if bath > bhk + 2:
            st.warning("⚠️ Note: Having more than BHK+2 bathrooms is unusual and may affect prediction accuracy.")

        # Predict button
        if st.button("🔮 Predict Price", type="primary", use_container_width=True):
            if location and total_sqft and bhk and bath:
                with st.spinner("Calculating price..."):
                    predicted_price = predict_price(location, total_sqft, bath, bhk, model, data_columns)
                
                if predicted_price:
                    st.success(f"### 💰 Estimated Price: ₹{predicted_price:.2f} Lakhs")
                    
                    # Additional insights
                    price_per_sqft = (predicted_price * 100000) / total_sqft
                    st.info(f"**Price per sq ft:** ₹{price_per_sqft:.0f}")
                    
                    # Price range
                    lower_bound = predicted_price * 0.9
                    upper_bound = predicted_price * 1.1
                    st.info(f"**Expected Range:** ₹{lower_bound:.2f} - ₹{upper_bound:.2f} Lakhs")
            else:
                st.error("Please fill in all the details!")
    
    with col2:
        st.subheader("📊 Property Summary")
        
        # Display current selections
        if 'location' in locals():
            st.metric("Location", location)
        if 'total_sqft' in locals():
            st.metric("Area", f"{total_sqft:,} sq ft")
        if 'bhk' in locals():
            st.metric("Bedrooms", f"{bhk} BHK")
        if 'bath' in locals():
            st.metric("Bathrooms", bath)
        
        # Add some tips
        st.subheader("💡 Tips")
        st.markdown("""
        - **Location** greatly affects price
        - **Central areas** are typically more expensive
        - **Price per sq ft** varies by locality
        - Consider **future development** in the area
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit |
        <a href="https://github.com/Vansh462/Bangluru-House-Price-Prediction" target="_blank" style="text-decoration: none;">
            🔗 View Source Code
        </a>
        </p>
        <p style='font-size: 12px; color: #666;'>
            Machine Learning Project | Bangalore House Price Prediction
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
