# 🏠 Bangalore House Price Predictor

A machine learning web application built with Streamlit that predicts house prices in Bangalore based on location, area, and property features.

## 🚀 Features

- **Interactive UI**: Clean and intuitive Streamlit interface
- **Real-time Predictions**: Instant price predictions based on input parameters
- **Location-based Analysis**: Covers multiple areas across Bangalore
- **Price Insights**: Shows price per sq ft and expected price range
- **Responsive Design**: Works on desktop and mobile devices

## 📊 Model Details

- **Algorithm**: Linear Regression
- **Features**: Location, Total Area (sq ft), Bedrooms (BHK), Bathrooms
- **Dataset**: Bangalore house price data with 13,000+ records
- **Accuracy**: ~90% R² score

## 🛠️ Installation & Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd BHP
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - Local: http://localhost:8501

## 🌐 Deployment Options

### Option 1: Streamlit Community Cloud (FREE - Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Streamlit app"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

### Option 2: Hugging Face Spaces (FREE)

1. **Create a new Space** at [huggingface.co/spaces](https://huggingface.co/spaces)
2. **Choose Streamlit** as the SDK
3. **Upload your files** or connect GitHub repository
4. **Your app will be live** at `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

### Option 3: Railway/Render (Paid)

1. **Connect GitHub repository**
2. **Set build command**: `pip install -r requirements.txt`
3. **Set start command**: `streamlit run app.py --server.port $PORT`

## 📁 Project Structure

```
BHP/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── server/
│   └── artifacts/
│       ├── bengaluru_House_Data.pkl   # Trained ML model
│       └── columns.json               # Feature columns data
└── README.md                       # This file
```

## 🎯 Usage

1. **Select Location**: Choose from 200+ Bangalore localities
2. **Enter Area**: Specify total area in square feet
3. **Choose BHK**: Select number of bedrooms (1-5)
4. **Select Bathrooms**: Choose number of bathrooms (1-5)
5. **Get Prediction**: Click "Predict Price" for instant results

## 🔧 Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Library**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Model**: Linear Regression

## 📈 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Include property age and amenities
- [ ] Add price trend analysis
- [ ] Implement map visualization
- [ ] Add comparison with similar properties

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit | Data Science Project**
