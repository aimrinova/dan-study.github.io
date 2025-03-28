#!/bin/bash

# Define the base directory
PROJECT_DIR="MRI_Injury_Detection"

# Create main project folder
mkdir -p $PROJECT_DIR
cd $PROJECT_DIR

# Create necessary subdirectories
mkdir -p data/raw_mri_scans
mkdir -p data/processed_mri_scans
mkdir -p data/segmentation_masks
mkdir -p data/predictions

mkdir -p models

mkdir -p notebooks

mkdir -p scripts

mkdir -p deployment/configs

mkdir -p logs

# Create necessary files
touch README.md

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing required dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete! Your MRI project structure is ready."
