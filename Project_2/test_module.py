import pandas as pd
from main import calculate_race_distribution
from main import calculate_race_distribution
from main import average_age_of_men
from main import percentage_bachelors
from main import percentage_high_earners
from main import percentage_low_earners
from main import min_work_hours
from main import percentage_min_hours_high_earners
from main import highest_earning_country
from main import top_IN_occupation

# Read the CSV file from the provided URL
url = "https://raw.githubusercontent.com/Promptgiga-edge/projects_freeCodeCamp/main/Project_2/Census_database_1994.csv"
df = pd.read_csv(url)

# Calculate the distribution of people by race
race_distribution = calculate_race_distribution(df)
print("Race distribution:")
print(race_distribution)

# Calculate the average age of men
avg_age_men = average_age_of_men(df)
print(f"Average age of men: {avg_age_men} years")

# Calculate the percentage of people with a Bachelor's degree
percentage_bachelors_degree = percentage_bachelors(df)
print(f"Percentage with Bachelor's degree: {percentage_bachelors_degree}%")

# Calculate the percentage of high earners with advanced education
percentage_high_earners_advanced_edu = percentage_high_earners(df)
print(f"Percentage of high earners with advanced education: {percentage_high_earners_advanced_edu}%")

# Calculate the percentage of high earners without advanced education
percentage_high_earners_non_advanced_edu = percentage_low_earners(df)
print(f"Percentage of high earners without advanced education: {percentage_high_earners_non_advanced_edu}%")

# Find the minimum number of hours worked per week
min_hours_worked = min_work_hours(df)
print(f"Minimum hours worked per week: {min_hours_worked}")

# Calculate the percentage of high earners among those working the minimum hours
percentage_high_earners_min_hours = percentage_min_hours_high_earners(df)
print(f"Percentage of high earners among those working minimum hours: {percentage_high_earners_min_hours}%")

# Find the country with the highest percentage of high earners
highest_earning_country, highest_earning_percentage = highest_earning_country(df)
print(f"Highest earning country: {highest_earning_country} ({highest_earning_percentage}%)")

# Identify the most popular occupation for high earners in India
top_occupation_india = top_IN_occupation(df)
print(f"Most popular occupation for high earners in India: {top_occupation_india}")
