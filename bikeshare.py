import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome to the beautiful world of Python! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
def get_filters():
    city_keywords = {'chicago', 'new york city', 'washington'}
    city = set([None])

    while not city.issubset(city_keywords):
        city = set(input('Which city are you interested in looking at? Chicago, New York City, or Washington?').lower().split(', '))        

    # TO DO: get user input for month (all, january, february, ... , june)
    month_keywords = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = None
    
    while month not in month_keywords:
            month = input('Which month are you interested in looking at?\nPS: you can use all as well to see everything \n').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_keywords = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = None
    
    while day not in day_keywords:
            day = input('Which day are you interested in looking at?\nPS: you can use all as well to see everything \n').lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    final_df = []
    for c in city:
        df = pd.read_csv(CITY_DATA[c])
    
        df['Start Time'] = pd.to_datetime(df['Start Time'])
    
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        df['city'] = c.title() 
        final_df.append(df)
    final_df = pd.concat(final_df).reset_index()
    
    month_name_to_index = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "mai": 5,
        "june": 6
    }

    if month == "all" and day == "all":
        final_df = final_df
    elif month == "all":
        final_df = final_df[final_df.day_of_week == day.title()]
    elif day == "all":
        final_df = final_df[final_df.month == (month_name_to_index[month])]
    else:
        final_df = final_df[(final_df.month == (month_name_to_index[month]) & (final_df.day_of_week == day.title()))]
       
    return final_df


def time_stats(final_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    final_df['month'] = final_df['Start Time'].dt.month
    most_common_month = final_df['month'].mode()[0]
    print("The most common month is {}.\n".format(most_common_month))

    # TO DO: display the most common day of week
    final_df['day_of_week'] = final_df['Start Time'].dt.day_name()
    most_common_day = final_df['day_of_week'].mode()[0]
    print("The most common day is {}.\n".format(most_common_day))


    # TO DO: display the most common start hour
    final_df['hour'] = final_df['Start Time'].dt.hour
    most_common_time = final_df['hour'].mode()[0]
    print("The most common time is {}.\n".format(most_common_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(final_df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    print("The most commonly used start station is {}.\n".format(final_df["Start Station"].mode().item()))

    # TO DO: display most commonly used end station
    
    print("The most commonly used end station is {}.\n".format(final_df["End Station"].mode().item()))

    # TO DO: display most frequent combination of start station and end station trip
    
    final_df['route'] = final_df['Start Station'] + "-" + final_df['End Station']
    print("The most frequent route is {}.\n".format(final_df['route'].mode().item()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(final_df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: {}.\n".format(final_df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("Average travel time: {}.\n".format(final_df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(final_df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of users are: {}. \n".format(final_df["User Type"].shape[0]))

    # TO DO: Display counts of gender
    if "Gender" in final_df:
        print("The counts of males are: {}. \n".format(final_df[final_df["Gender"] == "Male"].shape[0]))    
        print("The counts of females are: {}. \n".format(final_df[final_df["Gender"] == "Female"].shape[0]))
    else:
        print("There is no gender specification data in this dataframe")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in final_df:    
        print("The earliest birth year is: {}. \n".format(final_df["Birth Year"].min()))
        print("The latest birth year is: {}. \n".format(final_df["Birth Year"].max()))
        print("The most common birth year is: {}. \n".format(final_df["Birth Year"].mode().item()))
    else:
        print("There is no birth year data in this dataframe")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(final_df):
    accepted_answers = ["yes", "no"]
    user_reply = None
    i = 0
    while user_reply not in accepted_answers:
        user_reply = input("Do you want to see the first 5 rows of raw data? Reply yes or no.\n".lower())
        if user_reply == "yes":
            print(final_df.head())
        else:
            print("You typed something wrong, please check again")
    
    while user_reply == "yes":
        user_reply2 = None
        user_reply2 = input("Do you want to see more data? \nReply with yes or no.\n".lower())
        i += 5
        if user_reply2 == "yes":
            print(final_df[i:i+5])
        else:
            break
            
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
