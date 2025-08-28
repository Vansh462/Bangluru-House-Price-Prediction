#!/usr/bin/env python3
"""
Deployment helper script for Bangalore House Price Predictor
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'server/artifacts/bengaluru_House_Data.pkl',
        'server/artifacts/columns.json'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found!")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def run_app():
    """Run the Streamlit application"""
    print("🚀 Starting Streamlit app...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
    except Exception as e:
        print(f"❌ Error running app: {e}")

def main():
    """Main deployment function"""
    print("🏠 Bangalore House Price Predictor - Deployment Script")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Deployment failed: Missing required files")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Deployment failed: Could not install dependencies")
        return
    
    print("\n🎉 Setup complete! Starting the application...")
    print("📱 The app will open in your browser at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the application")
    print("-" * 60)
    
    # Run the app
    run_app()

if __name__ == "__main__":
    main()
