import nasdaqdatalink
import pandas as pd
import pygal
import cairosvg  # Import cairosvg for converting SVG to PNG

# Set pandas options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

# Set your Nasdaq Data Link API key
nasdaqdatalink.ApiConfig.api_key = 'D1v7-vW5vYrXhH3SgxeL'

# Fetch Bitcoin Trade Volume vs Transaction Volume Ratio (TVTVR) data
TVTVR_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='TVTVR')

# Create an empty list to store the fetched data
TVTVR_list = []

for index, row in TVTVR_data.iterrows():
    date = row.iloc[1].strftime('%Y-%m-%d')  # Format the date
    TVTVR_list.append((date, row.iloc[2]))  # Append date and value

# Extract dates and values
dates, value = zip(*TVTVR_list)

# Create a line chart
chart = pygal.Line(x_label_rotation=45)
chart.title = "Bitcoin Trade Volume vs Transaction Volume Ratio"
chart.x_labels = dates
chart.add("Values", value)

# Render to SVG
chart.render_to_file('Bitcoin_Trade_Volume_vs_Transaction_Volume_Ratio.svg')

# Convert the SVG to PNG using cairosvg
cairosvg.svg2png(url='Bitcoin_Trade_Volume_vs_Transaction_Volume_Ratio.svg', write_to='Bitcoin_Trade_Volume_vs_Transaction_Volume_Ratio.png')
