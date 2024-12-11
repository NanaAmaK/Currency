import nasdaqdatalink
import pandas as pd
import pygal
import cairosvg

# Set pandas options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

# Set your Nasdaq Data Link API key
nasdaqdatalink.ApiConfig.api_key = 'D1v7-vW5vYrXhH3SgxeL'

# Fetch Bitcoin Total Number of Transactions (NTRAT) data
NTRAT_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='NTRAT')

# Create an empty list to store the fetched data
NTRAT_list = []

for index, row in NTRAT_data.iterrows():
    date = row.iloc[1].strftime('%Y-%m-%d')  # Format the date
    NTRAT_list.append((date, row.iloc[2]))  # Append date and value

# Extract dates and values
dates, value = zip(*NTRAT_list)

# Create a line chart
chart = pygal.Line(x_label_rotation=45)
chart.title = "Bitcoin Total Number of Transactions over Time"
chart.x_labels = dates
chart.add("Values", value)

# Render to SVG
chart.render_to_file('Bitcoin_Total_Number_of_Transaction.svg')

# Convert the SVG to PNG using cairosvg
cairosvg.svg2png(url='Bitcoin_Total_Number_of_Transaction.svg', write_to='Bitcoin_Total_Number_of_Transaction.png')
