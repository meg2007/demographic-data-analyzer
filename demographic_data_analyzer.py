import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv", header=None, names=[
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()[["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"]]

    # What is the average age of men?
    male_ages = pd.to_numeric(df[df["sex"] == "Male"]["age"], errors="coerce")

    average_age_men = round(male_ages.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_degree = df[df["education"] == "Bachelors"]

    percentage_bachelors = round((len(bachelors_degree) / total_people) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education[higher_education["salary"] == ">50K"]) / len(higher_education)) * 100, 1)

    lower_education_rich = round((len(lower_education[lower_education["salary"] == ">50K"]) / len(lower_education)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = int(df["hours-per-week"].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df["hours-per-week"] == min_work_hours]

    num_min_workers = len(min_workers)

    num_rich_min_workers = len(min_workers[min_workers["salary"] == ">50K"])

    if num_min_workers > 0:
        rich_percentage = round((num_rich_min_workers / num_min_workers) * 100, 1)
    else:
        rich_percentage = 10
    

    # What country has the highest percentage of people that earn >50K?
    country_earnings = df.groupby("native-country").apply(lambda x: (x[x["salary"] == ">50K"].shape[0] / x.shape[0]) * 100)

    highest_earning_country = country_earnings.idxmax()

    highest_earning_country_percentage = round(country_earnings.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[df["native-country"] == "India"]

    top_IN_occupation = india[india["salary"] == ">50K"]["occupation"].mode()[0]

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
