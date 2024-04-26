import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    return race_counts

    # What is the average age of men?
    men_df = df[df['sex'] == 'Male']
    average_age_men = men_df['age'].mean()
    return round(avg_age, 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = (bachelors_count / total_count) * 100
    return round(percentage, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return higher_education

    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    return higher_education

    # percentage with salary >50K
    
    high_ed_earn_df = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich = (high_ed_earn_df.shape[0] / higher_education.shape[0]) * 100
    return round(percentage, 1)

    low_ed_earn_df = lower_education[lower_education['salary'] == '>50K']
    lower_education_rich = (low_ed_earn_df.shape[0] / lower_education.shape[0]) * 100
    return round(percentage, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    return min_work_hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_workers.shape[0]

    high_earn_df = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = (high_earn_df.shape[0] / num_min_workers) * 100
    return round(percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').sum() / len(x)).country_stats.idxmax()
    highest_earning_country_percentage = highest_earning_country.max() * 100
    return highest_earning_country, round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners_df['occupation'].mode().iloc[0]
    return top_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
