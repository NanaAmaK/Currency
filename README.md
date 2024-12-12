# Project Name: NanaAmaK

## Description
This project includes Python scripts for data analysis, visualizations, and a web dashboard. It provides insights into Bitcoin transactions and trade volume ratios, alongside other resources like static files, templates, and graphical outputs.

## Features
- **Bitcoin Visualizations**: Includes pre-generated charts:
  - `Bitcoin_Total_Number_of_Transaction.svg`
  - `Bitcoin_Trade_Volume_vs_Transaction_Volume_Ratio.svg`
- **Web Dashboard**: Built with Python (using `dashboard.py` and `app.py`).
- **Static and Template Files**: Organized for front-end integration.
- **Custom Line Chart Viewer**: Script for displaying line charts (`line_chart_viewer.py`).
- **Preconfigured DevContainer**: `.devcontainer` for VSCode remote development setup.

## Project Structure
```plaintext
NanaAmaK/
├── .devcontainer/            # Configuration files for DevContainer
├── __pycache__/              # Compiled Python files
├── static/                   # Static files (CSS, JS, images)
├── templates/                # HTML template files
├── Bitcoin_Total_Number_of_Transaction.svg  # Visualization of total Bitcoin transactions
├── Bitcoin_Trade_Volume_vs_Transaction_Volume_Ratio.svg  # Visualization of trade vs transaction volume ratio
├── Octocat.png               # Example image resource
├── README.md                 # Project documentation
├── app.py                    # Flask app for the dashboard
├── dashboard.py              # Script to manage and render dashboard components
├── gitignore.txt             # Files to be ignored by Git
├── line_chart_viewer.py      # Script to visualize line charts
├── main.py                   # Main script for the application
├── main1.py                  # Additional script for auxiliary functionality
├── requirements.txt          # Dependencies for the project

