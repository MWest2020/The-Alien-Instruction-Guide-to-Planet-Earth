#!/bin/bash

# Exit on error
set -e

echo "Setting up The Alien Instruction Guide AI system..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p ai/trained_model
mkdir -p ai/training_data

# Set permissions
echo "Setting script permissions..."
chmod +x ai/train_model.py

echo "Installation complete! To activate the environment, run:"
echo "source venv/bin/activate"
echo ""
echo "To train the model, run:"
echo "python ai/train_model.py" 