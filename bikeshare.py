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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle     invalid inputs
    city = ''
    while city not in ('chicago', 'new york city', 'washington'):
    
        city = input("which city would you like to explore?").lower()
    print(city)


    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
    
        month= input("which month would you like to check?").lower()
    print(month)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ('all', 'monday', 'tuesady', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
    
        day= input("which day would you like to check?").lower()
    print(day)


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
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')
        
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df = df.loc[df['Start Time'].dt.month == month,:]
    
    if day != 'all':
    
        df['Start Time'] = pd.to_datetime(df['Start Time'])  
        df = df.loc[df['Start Time'].dt.weekday_name.str.lower() == day,:] 
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_num = (df['Start Time'].dt.month).mode()
    print(months[(month_num[0] - 1)])


    # TO DO: display the most common day of week
    print((df['Start Time'].dt.weekday_name).mode())

    # TO DO: display the most common start hour
    print((df['Start Time'].dt.hour).mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print((df['Start Station']).mode())

    # TO DO: display most commonly used end station
    print((df['End Station']).mode())

    # TO DO: display most frequent combination of start station and end station trip
    print((df['Start Station'] + ' - ' + df['End Station']).mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print((df['End Time'] - df['Start Time']).sum())


    # TO DO: display mean travel time
    print((df['End Time'] - df['Start Time']).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print('no Gender data')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print(df['Birth Date'].min())
    except KeyError:
        print('no Birth Date data')
        
    try:
        print(df['Birth Date'].max())
    except KeyError:
        print('no Birth Data data')
        
    try:
        print(df['Birth Date'].mode())
    except KeyError:
        print('no Birth Date data')
  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

# Ask the users if they would like to see 5 lines of raw data
    
    response = ''
    while response != 'no':
        
            row_num = 5
            while row_num < df.shape[0]:
                response = input("would you like to see 5 lines of raw data? (type 'yes' or 'no')").lower()
                if response == 'yes':
                    print(df.iloc[min(row_num, df.shape[0])-5:min(row_num, df.shape[0]),:]);     # Used min() function to make sure display index never exceeds number of rows
                    row_num += 5
                else:
                    break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

