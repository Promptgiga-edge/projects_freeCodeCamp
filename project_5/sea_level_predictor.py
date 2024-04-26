import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_level_data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(sea_level_data["Year"], sea_level_data["CSIRO Adjusted Sea Level"], color='blue', label='Sea Level Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(sea_level_data["Year"], sea_level_data["CSIRO Adjusted Sea Level"])
    # Predict sea level rise in 2050 using all data
    plt.plot([1880, 2050], [intercept + slope * 1880, intercept + slope * 2050], color='red', linestyle='--', label='Line of Best Fit (1880-2050)')


    # Create second line of best fit
    # Step 4: Filter data from year 2000 onwards
    recent_data = sea_level_data[sea_level_data["Year"] >= 2000]
    # Calculate line of best fit for recent data
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
    # Predict sea level rise in 2050 using recent data
    plt.plot([2000, 2050], [intercept_recent + slope_recent * 2000, intercept_recent + slope_recent * 2050], color='green', linestyle='--', label='Line of Best Fit (2000-2050)')
    
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()