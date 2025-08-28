# 🏠 Bangalore House Price Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bangalore-house-predictor.streamlit.app/)

A machine learning web application that predicts house prices in Bangalore using Linear Regression. Built with Streamlit for an interactive user experience.

## 🌐 Live Demo

**🚀 [Try the App Live](https://bangalore-house-predictor.streamlit.app/)**

## ✨ Features

- **🎯 Real-time Predictions**: Instant house price estimates based on your inputs
- **📍 Location Intelligence**: Covers 25+ prime Bangalore localities
- **💡 Smart Interface**: Clean, intuitive Streamlit UI with responsive design
- **📊 Price Analytics**: Shows price per sq ft and detailed breakdowns
- **⚡ Fast Performance**: Optimized model loading with caching

## 🧠 Model Performance

- **Algorithm**: Linear Regression (Scikit-learn)
- **Dataset**: 13,320 → 10,100 records (after cleaning)
- **Accuracy**: 85%+ R² score
- **Features**: Location, Total Area (sq ft), Bedrooms (BHK), Bathrooms
- **Training**: Rigorous data preprocessing with outlier removal

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vansh462/Bangluru-House-Price-Prediction.git
   cd Bangluru-House-Price-Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**: http://localhost:8501

### Cloud Deployment

The app is deployed on **Streamlit Cloud** for free hosting:
- **URL**: https://bangalore-house-predictor.streamlit.app/
- **Auto-deployment**: Connected to GitHub for continuous deployment

## 📁 Project Structure

```
Bangluru-House-Price-Prediction/
├── 📱 app.py                       # Main Streamlit application
├── 📋 requirements.txt             # Python dependencies
├── 🐍 runtime.txt                  # Python version specification
├── 🚀 deploy.py                    # Deployment utilities
├── 📊 artifacts/
│   ├── bengaluru_House_Data.pkl    # Trained ML model
│   └── columns.json                # Feature columns mapping
├── 📁 _not_needed/                 # Original dataset & notebook
│   ├── Bengaluru_House_Data.csv    # Raw dataset
│   └── bengaluru_house_price.ipynb # Data analysis notebook
├── 📄 LICENSE                      # MIT License
└── 📖 README.md                    # Project documentation
```

## 🎯 How to Use

1. **🏘️ Select Location**: Choose from Bangalore localities (Whitefield, Koramangala, etc.)
2. **📐 Enter Area**: Specify total area in square feet (500-10000+ sq ft)
3. **🛏️ Choose BHK**: Select bedrooms (1-5 BHK)
4. **🚿 Select Bathrooms**: Choose number of bathrooms (1-5)
5. **💰 Get Prediction**: Click "Predict Price" for instant results

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.11 |
| **ML Framework** | Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Model** | Linear Regression |
| **Deployment** | Streamlit Cloud |
| **Version Control** | Git, GitHub |

## 📊 Data Pipeline

1. **Data Collection**: 13,320 Bangalore house records
2. **Data Cleaning**: Removed duplicates, handled missing values
3. **Feature Engineering**: Location encoding, outlier detection
4. **Model Training**: Linear Regression with cross-validation
5. **Model Evaluation**: R² score, MAE, RMSE metrics
6. **Deployment**: Pickle serialization for production

## 🔮 Future Roadmap

- [ ] **🤖 Advanced Models**: Random Forest, XGBoost, Neural Networks
- [ ] **🏗️ More Features**: Property age, amenities, floor level
- [ ] **📈 Analytics**: Price trends, market analysis
- [ ] **🗺️ Visualization**: Interactive maps with Folium
- [ ] **🔍 Comparison**: Similar properties recommendation
- [ ] **📱 Mobile App**: React Native version

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset sourced from Kaggle's Bangalore House Price dataset
- Built with Streamlit's amazing framework
- Deployed on Streamlit Cloud's free tier

---

<div align="center">

**🏠 Built with ❤️ for Bangalore Real Estate | ML Project 2024**

[![GitHub stars](https://img.shields.io/github/stars/Vansh462/Bangluru-House-Price-Prediction?style=social)](https://github.com/Vansh462/Bangluru-House-Price-Prediction)
[![GitHub forks](https://img.shields.io/github/forks/Vansh462/Bangluru-House-Price-Prediction?style=social)](https://github.com/Vansh462/Bangluru-House-Price-Prediction)

</div>
