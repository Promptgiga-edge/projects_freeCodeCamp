from main import calculate_race_distribution
from main import average_age_of_men
from main import percentage_bachelors
from main import percentage_high_earners
from main import percentage_low_earners
from main import min_work_hours
from main import percentage_min_hours_high_earners
from main import highest_earning_country
from main import top_IN_occupation

csv_url = csv_url = "https://raw.githubusercontent.com/Promptgiga-edge/projects_freeCodeCamp/main/Project_2/Census_database_1994.csv"

df = pd.read_csv(csv_url)

print(df)