'''
Submitted 20.5.2021 on freeCodeCamp.org
'''

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.DataFrame(pd.read_csv('adult.data.csv'))

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df['age'][df['sex'] == 'Male'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'].value_counts()['Bachelors'])/(df.count()[0]) * 100,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.education.value_counts()['Bachelors']+df.education.value_counts()['Masters']+df.education.value_counts()['Doctorate']
    lower_education = df.count()[0]-higher_education


    # percentage with salary >50K
    rich = df.loc[df['salary']== '>50K', ['education']]
    rich_educated_total = rich['education'].value_counts()['Bachelors']+rich['education'].value_counts()['Masters']+rich['education'].value_counts()['Doctorate']
    higher_education_rich = round(rich_educated_total/higher_education *100,1)
    lower_education_rich = round((rich.count()[0] - rich_educated_total) / lower_education *100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'].value_counts()[min_work_hours]

    rich_percentage = df.loc[df['salary']== '>50K', ['hours-per-week']]['hours-per-week'].value_counts()[min_work_hours]/num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    rich_in_country = df.loc[df['salary']== '>50K', ['native-country']]['native-country'].value_counts()
    people_in_country = df['native-country'].value_counts()
    countries = pd.DataFrame({'rich-total': rich_in_country, 'people-total': people_in_country})
    countries['percentage'] = rich_in_country/people_in_country*100
    
    highest_earning_country = countries.loc[countries['percentage'] == countries['percentage'].max()].index[0]
    
    highest_earning_country_percentage = round(countries['percentage'].max(),1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[df['native-country']=='India', ['salary', 'occupation']].loc[df['salary']== '>50K']['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE - provided by freeCodeCamp.org

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
