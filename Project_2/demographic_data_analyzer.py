# %%
import pandas as pd


csv_url = "https://raw.githubusercontent.com/Promptgiga-edge/projects_freeCodeCamp/main/Project_2/Census_database_1994.csv"

df = pd.read_csv(csv_url)

# %%
df.head()

# %% [markdown]
# #How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

# %%
def calculate_race_distribution(df):
    """
    Calculates the distribution of people by race.
    Returns a Pandas Series with race names as index labels.
    """
    race_counts = df['race'].value_counts()
    return race_counts

# %% [markdown]
# #What is the average age of men?

# %%
def average_age_of_men(df):
    """
    Calculates the average age of men (gender 'Male').
    """
    men_df = df[df['sex'] == 'Male']
    avg_age = men_df['age'].mean()
    return round(avg_age, 1)

# %% [markdown]
# #What is the percentage of people who have a Bachelor's degree?

# %%
def percentage_bachelors(df):
    """
    Calculates the percentage of people with a Bachelor's degree.
    """
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage = (bachelors_count / total_count) * 100
    return round(percentage, 1)

# %% [markdown]
# #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

# %%
def percentage_high_earners(df):
    """
    Calculates the percentage of people with advanced education (Bachelors, Masters, or Doctorate)
    who make more than 50K.
    """
    advanced_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_earners_df = advanced_df[advanced_df['salary'] == '>50K']
    percentage = (high_earners_df.shape[0] / advanced_df.shape[0]) * 100
    return round(percentage, 1)

# %% [markdown]
# #What percentage of people without advanced education make more than 50K?

# %%
def percentage_low_earners(df):
    """
    Calculates the percentage of people without advanced education
    who make more than 50K.
    """
    non_advanced_df = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_earners_df = non_advanced_df[non_advanced_df['salary'] == '>50K']
    percentage = (high_earners_df.shape[0] / non_advanced_df.shape[0]) * 100
    return round(percentage, 1)


# %% [markdown]
# #What is the minimum number of hours a person works per week?

# %%
def min_work_hours(df):
    """
    Finds the minimum number of hours a person works per week.
    """
    min_hours = df['hours-per-week'].min()
    return min_hours

# %% [markdown]
# #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

# %%
def percentage_min_hours_high_earners(df):
    """
    Calculates the percentage of people who work the minimum number of hours per week
    and have a salary of more than 50K.
    """
    min_hours = min_work_hours(df)
    min_hours_df = df[df['hours-per-week'] == min_hours]
    high_earners_df = min_hours_df[min_hours_df['salary'] == '>50K']
    percentage = (high_earners_df.shape[0] / min_hours_df.shape[0]) * 100
    return round(percentage, 1)

# %% [markdown]
# #What country has the highest percentage of people that earn >50K and what is that percentage?

# %%
def highest_earning_country(df):
    """
    Finds the country with the highest percentage of people earning >50K
    and returns the country name and percentage.
    """
    country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').sum() / len(x))
    highest_earning_country = country_stats.idxmax()
    highest_percentage = country_stats.max() * 100
    return highest_earning_country, round(highest_percentage, 1)

# %% [markdown]
# #Identify the most popular occupation for those who earn >50K in India.

# %%
def top_IN_occupation(df):
    """
    Identifies the most popular occupation for high earners in India.
    """
    india_high_earners_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_occupation = india_high_earners_df['occupation'].mode().iloc[0]
    return top_occupation

# %%



