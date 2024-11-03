#!/bin/bash

# Step 1: Create a virtual environment if it doesn’t e
# Step 3: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Create directories for Allure if not existing
mkdir -p allure-results allure-reports

# Step 5: Run pytest with Allure
echo "Running tests..."
pytest --alluredir=allure-results

# Step 6: Generate Allure report
echo "Generating Allure report..."
allure generate allure-results -o allure-reports --clean

# Step 7: Deactivate the virtual environment
deactivate


