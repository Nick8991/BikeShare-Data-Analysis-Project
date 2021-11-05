import time
import pandas as pd
import numpy as np


# dictionary for acessing file name
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city' : 'new_york_city.csv',
             'washington': 'washington.csv'}
# month and week dictionaries hold month and week keys for accesing dictionary values
month_index = {'january':1, 'february':2, 'march':3,  'april':4, 'may': 5,
                'june':6, 'None':None, 'all':'all'}
week_index = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3,
                'friday':4, 'saturday':5, 'sunday':6, 'None':None, 'all':'all'}

list_city = ['chicago', 'washington', 'new york city']

def get_filters():


    """Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) both  - name of the day of week and month to filter by,
    (str) none - no filters applied
    Returns:
    city as city as str
    month and day as ints corresponding to keys in month_index and week_index dictionaries"""
    city=""
    month =""
    day =""
    print("Hello Let\'s  explore some US bikeshare data!\n\n")
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    explore_by = ['month', 'day', 'both', 'none']
    try:
        while city not in list_city:
            city = input('Enter city you wish to explore (chicago, new york city, washington)\n\n >').lower()
        print('\n Welcome to the {} bikeshare database.\n'.format(city))
        select_by = input('Would you like to explore the data by month, both(month and day), or none\n >').lower()

        while select_by not in explore_by:
            select_by = input("Enter  'month', both(month and day), 'none'").lower()

        if select_by == 'month':
            month = input('Enter a month name from january,february, march,... june or all\n' + '>').lower()
            while month not in months:
                month = input('Enter a valid month name january,...,june or all\n ' + '>').loer()
            day = 'None'
        elif select_by == 'day':
            day = input('Enter a weekday name like monday,...,sunday, or all\n' +'>').lower()
            while day not in days:
                day = input('Enter a valid weekday\n' + '>').lower()
            city = 'None'
        elif select_by == 'both':
            while month not in months:
                month = input('Enter a month name from january,february, march,... june\n' + '>').lower()
            while day not in days:
                day = input('Enter a weekday name like monday,...,sunday\n' +  '>').lower()
        elif select_by == 'none':
            month = 'None'
            day = 'None'
    except KeyboardInterrupt:
        print('You stopped the code execution')
    except EOFError:
        print('The program was stopped and an unexpexted EOFError was generated')

    print('-'*40)
    return city, month_index.get(month), week_index[day]


def get_ValueKey(months, days):
    """
    Takes as args month and days integers
    creates four temporal list from month_index and week_index dictionaries
    gets values and keys from week_index and month_index dictionaries
    Returns:
            str keys corresponding to dictionaries values
    """
    month_keys = list(month_index.keys())
    month_values = list(month_index.values())
    week_keys = list(week_index.keys())
    week_values = list(week_index.values())
    postion_month = month_values.index(months)
    position_week = week_values.index(days)

    return month_keys[postion_month], week_keys[position_week]


def load_data(city, month, day):
    """
    Loads dataframe base on city, month and day filters
    loads filename base on the corresponding city key value in CITY_DATA dictionary
    Returns:
            df - Pandas DataFrame containing city data filtered by month and day
    """
    if city in list_city:
        filename = CITY_DATA[city]
        df = pd.read_csv(filename)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        if month == None and day == None:
            df['Start Time'] = pd.to_datetime(df['Start Time'])
        elif month ==None and day != None:
            df['DayOfWeek'] = df['Start Time'].dt.dayofweek
        elif month != None and day == None:
            df['Month'] = df['Start Time'].dt.month
        elif month != None and day != None:
            df['DayOfWeek'] = df['Start Time'].dt.dayofweek
            df['Month'] = df['Start Time'].dt.month
    return df



def time_stats(df, month_value, day_value):
    """Displays statistics on the most frequent times of travel.
    filters dataframe base on month and date
    displays most common month, day and hour
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    month, day = get_ValueKey(month_value, day_value)
    if month_value == None and day_value == None:
        print('Sorted by None')
        print('The following information is base on (Start Time) column')
        print('Most common Start Time for unsorted data:    ', df['Start Time'].mode()[0])
        print('Most common hour:    ', df['Start Time'].dt.hour.mode()[0])

    elif month_value != None and  day_value == None:
        print('Most common month:    ', df['Month'].mode()[0])
        print('Most common hour:    ', df['Start Time'].dt.hour.mode()[0])

    elif month_value == None and day_value != None:
        print('Most common day:    ', df[DayOfWeek].mode()[0])
        print('Most common hour:    ', df['Start Time'].dt.hour.mode()[0])

    else:
        print('Most common month:    ', df['Month'].mode()[0])
        print('Most common day:    ', df['DayOfWeek'].mode()[0])
        print('Most common hour:    ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def  station_stats(df, month_value, day_value):
    """Displays statistics on the most popular stations and trip.
    filters dataframe base on month and date
    display most start station for particular month and day or are None
    displays the most end station for a particular month and day or are None
    displays most used start station and end station
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip
    Start_time = time.time()
    month, day = get_ValueKey(month_value, day_value)
    if ((month_value == 'all' and day_value == None) or
        (month_value == None and day_value == 'all')
    or (month_value == None and day_value == None)):
        print('Sorted by all or None')
        print('Most used start station:    ', df['Start Station'].mode()[0])
        print('Most used end station:    ', df['End Station'].mode()[0])
        print('Most used start and end station:  \n',
        df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1))

    elif month_value in range(1, len(month_index)-1) and day_value not in range(0, len(day)-2):
        df1 = df[df['Month']==month_value]
        print('Sorting by month only\n')
        print('Most used stations for month number {}'.format(month))
        print('Most used start station :     ', df1['Start Station'].mode()[0])
        print('Most used end station : ', df1['Start Station'].mode()[0])
        #print('Most used start and end station:    \n',
        #        df1.groupby(df1['Start Station','End Station']).size().sort_values(ascending=False).head(1))

    elif month_value not in range(1, len(month_index)-1)  and day_value in range(0, len(week_index)-2):
        df1 = df[df['DayOfWeek'] == day_value]
        print('Sorting by day only\n')
        print('Most used stations {}'.format(day))
        print('Most used start station:    ', df1['Start Station'].mode()[0])
        print('Most used end station:     ', df1['End Station'].mode()[0])
        print('Most used start and end station:   \n',
                df1.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1))

    elif month_value in range(1, len(month_index)-1)  and day_value in range(0, len(week_index)-2):
        df1 = df[df['Month'] == month_value]
        df2 = df1[df1['DayOfWeek'] ==  day_value]
        print('Most used stations for all {} in  {} '.format(day, month))
        print('Most used start station:    ', df2['Start Station'].mode()[0])
        print('Most used end station:    ', df2['End Station'].mode()[0])
        print('Most used start and end station:    \n',
                df2.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - Start_time))
    print('-'*40)


def trip_duration_stats(df, month, day):
    """Displays statistics on the total and average trip duration.
        """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if ((month == 'all' and day == None) or
        (month == None and day == 'all') or
        (month == None and day == None)):
        travel_time = df['Trip Duration'].sum()
        mean_time = df['Trip Duration'].mean()
        str_mean = str(mean_time)+'S'
        str_time = str(travel_time) + 'S'
        print('Sorted by all or None')
        print('Total travel time indays hrs mins and seconds: ', pd.to_timedelta(str_time))
        print('Average travel time: ', pd.to_timedelta(str_mean))

    elif month in range(1, len(month_index)-1) and day not in range(0, len(week_index)-2):
        df1 = df[df['Month'] == month]
        t_time = df1['Trip Duration'].sum()
        mean_time = df1['Trip Duration'].mean()
        str_mean = str(mean_time)+'S'
        str_time = str(t_time)+'S'
        print('Sorted by month')
        print('Total travel time indays hrs mins and seconds:', pd.to_timedelta(str_time))
        print('Average travel time: ',pd.to_timedelta(mean_time) )

    elif month not in range(1, len(month_index)-1)  and day in range(0, len(week_index)-2):
        df1 = df[df['DayOfWeek'] == month]
        t_time = df1['Trip Duration'].sum()
        mean_time = df1['Trip Duration'].mean()
        str_time = str(t_time)+'S'
        str_mean = str(mean_time)+'S'
        print('Sorted by day of a week')
        print('Total travel time:     ',pd.to_timedelta(str_time) )
        print('Average traveling time:    ', pd.to_timedelta(str_mean))

    elif month in range(1, len(month_index)-1)  and day in range(0, len(week_index)-2):
        df1 = df[df['Month'] == month]
        df2 = df1[df1['DayOfWeek']==day]
        t_time = df2['Trip Duration'].sum()
        mean_time = df2['Trip Duration'].mean()
        str_time = str(t_time)+'S'
        str_mean = str(mean_time)+'S'
        print('Sorted by month and day')
        print('Total travel time:     ',pd.to_timedelta(str_time) )
        print('Average traveling time:    ', pd.to_timedelta(str_mean))

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if ((month == 'all' and day == None) or
        (month == None and day == 'all') or
        (month == None and day == None)):
        if city == 'washington':
            print('For unsorted data')
            print('Birth year and Gender columns are absent for this database')
            print('User Type counts: ', df['User Type'].value_counts())
        else:
            print('For unsorted data')
            print('User Type counts: ', df['User Type'].value_counts())
            print('Gender counts: ', df['Gender'].value_counts())
            print('Earliest year of birth: ', df['Birth Year'].min())
            print('Most recent year of birth: ', df['Birth Year'].max())
            print('Most common birth Year:   ',df['Birth Year'].mode())

    elif month in range(1, len(month_index)-1) and day not in range(0, len(week_index)-2):
        df1 = df[df['Month']==month]
        if city == 'washington':
            print('For unsorted data')
            print('Birth year and Gender columns are absent for this database')
            print('User Type counts: ', df1['User Type'].value_counts())
        else:
            print('For unsorted data')
            print('User Type counts: ', df1['User Type'].value_counts())
            print('Gender counts: ', df1['Gender'].value_counts())
            print('Earliest year of birth: ', df1['Birth Year'].min())
            print('Most recent year of birth: ', df1['Birth Year'].max())
            print('Most common birth Year:   ',df1['Birth Year'].mode())

    elif month not in range(1, len(month_index)-1)  and day in range(0, len(week_index)-2):
        df1 = df1[df1['DayOfWeek']== day]
        if city == 'washington':
            print('For unsorted data')
            print('Birth year and Gender columns are absent for this database')
            print('User Type counts: ', df1['User Type'].value_counts())
        else:
            print('For unsorted data')
            print('User Type counts: ', df1['User Type'].value_counts())
            print('Gender counts: ', df1['Gender'].value_counts())
            print('Earliest year of birth: ', df1['Birth Year'].min())
            print('Most recent year of birth: ', df1['Birth Year'].max())
            print('Most common birth Year:   ',df1['Birth Year'].mode())

    elif month in range(1, len(month_index)-1)  and day in range(0, len(week_index)-2):
        df1 = df[df['Month']==month]
        df2 = df1[df1['DayOfWeek']==day]
        if city == 'washington':
            print('For unsorted data')
            print('Birth year and Gender columns are absent for this database')
            print('User Type counts: ', df2['User Type'].value_counts())
        else:
            print('For unsorted data')
            print('User Type counts: ', df2['User Type'].value_counts())
            print('Gender counts: ', df2['Gender'].value_counts())
            print('Earliest year of birth: ', df2['Birth Year'].min())
            print('Most recent year of birth: ', df2['Birth Year'].max())
            print('Most common birth Year:   ',df2['Birth Year'].mode())

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_rawData(city_name):
    """ Ask user to enter yes to no view raw data
    if user enters yes 5 lines of the .csv file is dipslayed
    user types yes to display the next 5 lines of the .csv file
    user types no or and enters an invalid option to abort the program
    """

    rows = []
    global counts
    counts = 5
    dataRaw = ['yes', 'no']
    verify = True
    while verify == True:
        input_verify = input('Would like to view the raw data ? Enter yes or no\n>').lower()
        while input_verify not in dataRaw:
            input_verify = input('Re-enter a value, please enter yes or no\n>')
        if input_verify == 'yes':
            while input_verify == 'yes':
                with open(CITY_DATA[city_name], 'r') as file:
                    filereader = file.readlines()
                    temp = filereader[0:counts]
                    rows.append(temp)
                    count = counts + 5
                print(rows)

                input_verify = input('Type yes to continue and no to stop\n>').lower()
                if input_verify == 'yes':
                    print('')
                elif input_verify == 'no':
                    print('Aborting.......')
                    break
                else:
                    print('invalid option aborting....')
                    break
        elif input_verify == 'no':
            verify = False
            print('Quiting...')

        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df, month, day)
        trip_duration_stats(df, month, day)
        user_stats(df, city, month, day)
        view_rawData(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
