import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"]=="Male"]["age"].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df["education"].value_counts().loc["Bachelors"] / df["education"].count() ) *100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = 0
    for i in range(len(df)):
        if df.loc[i,"education"] in {"Bachelors","Masters","Doctorate"} :
            higher_education=higher_education+1
    
    lower_education = 0
    for i in range(len(df)):
        if not df.loc[i,"education"] in {"Bachelors","Masters","Doctorate"} :
            lower_education=lower_education+1

    # percentage with salary >50K
    c=0
    t=0
    for i in range(len(df)):
        if df.loc[i,"education"] in {"Bachelors","Masters","Doctorate"} :
            t=t+1
            if df.loc[i,"salary"] == ">50K":
                c=c+1

    higher_education_rich = (c/t)*100


    c1=0
    t1=0
    for i in range(len(df)):
        if not df.loc[i,"education"] in {"Bachelors","Masters","Doctorate"} :
            t1=t1+1
            if df.loc[i,"salary"] == ">50K":
                c1=c1+1
    
    lower_education_rich = (c1/t1)*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df["hours-per-week"] == df["hours-per-week"].min()) & (df["salary"] == ">50K")])

    rich_percentage = (num_min_workers / len(df.loc[df["hours-per-week"]==df["hours-per-week"].min()])) *100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = ((df[df['salary'] == '>50K'].groupby(["native-country"])["native-country"].count())/(df[df['salary'] == '>50K'].groupby(["native-country"])["native-country"].count()+df[df['salary'] == '<=50K'].groupby(["native-country"])["native-country"].count())).idxmax()
    highest_earning_country_percentage = ((df[df['salary'] == '>50K'].groupby(["native-country"])["native-country"].count())/(df[df['salary'] == '>50K'].groupby(["native-country"])["native-country"].count()+df[df['salary'] == '<=50K'].groupby(["native-country"])["native-country"].count())).max() *100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["salary"]==">50K") & (df["native-country"]=="India")]["occupation"].value_counts().idxmax()

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
        'average_age_men': average_age_men.round(1),
        'percentage_bachelors': percentage_bachelors.round(1),
        'higher_education_rich': round(higher_education_rich,1),
        'lower_education_rich': round(lower_education_rich,1),
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage.round(1),
        'top_IN_occupation': top_IN_occupation
    }
