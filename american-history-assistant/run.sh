#!/bin/bash

# AI-Powered FAQ Helpdesk - Quick Start Script

echo "=========================================="
echo "AI-Powered FAQ Helpdesk"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher from https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Check if requirements are installed
if ! python3 -c "import flask, pandas, sklearn" 2>/dev/null; then
    echo "Installing required packages..."
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
    echo ""
else
    echo "✓ Dependencies already installed"
    echo ""
fi

# Check if data file exists
if [ ! -f "data/faq_data.csv" ]; then
    echo "❌ Error: FAQ data file not found at data/faq_data.csv"
    exit 1
fi

echo "✓ FAQ data file found"
echo ""

# Start the Flask application
echo "=========================================="
echo "Starting Flask server..."
echo "=========================================="
echo ""
echo "🌐 Open your browser and go to:"
echo "   http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py

