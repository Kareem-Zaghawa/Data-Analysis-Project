import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    global day
    global month
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for Chicago , Washington, or New York?')
    while True:
        global city
        city = input('Please specify a city: \n').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('The city you specified is not in the list. Choose from Chicago, New York, Washington')  
        
        
    # get user input for month (all, january, february, ... , june)
    def month():
        while True:
            global month
            month = input('Which month? January, February, March, April, May, June \n').title()
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            if month not in months:
                print('The month you specified is not avalilable.')
                print('Please choose from January to June')
            else:
                break
        
        
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    def day():
        while True:
            global day
            day = input('Which day? Monday, Tuseday, Wednesday, Thursday, Friday, Saturday, Sunday \n').title()
            days = ['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday']
            if day not in days:
                print('The day you specified may have a typo, please enter it again')
            else:
                break 
    while True:
        choice_filter = input('Would you like to filter data by month, day, both or no filter? type "none" for no time filter \n')
        if choice_filter not in ['month','day','none','both']:
            print('Oops! looks like you typed the filter incorrectly, please type it again \n')
        else:
            break
        
    
    if choice_filter == 'month':
        month()
        day = None
    elif choice_filter == 'day':
        day()
        month = None
    elif choice_filter == 'both':
        month()
        day()
    else:
        month = None
        day = None

    

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #adding new column for months
    df['month'] = df['Start Time'].dt.month_name()
    
    #adding new column for days 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #fitlering data using the user's choice of month and/or day
    if month != None :
        df = df.loc[df['month']== month.title()]
    
    if day != None:
            df = df.loc[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    global month
    if month == None:
        common_month = df['month'].mode()[0]
        countmonth = df.groupby(['month'])['month'].count()[common_month]
        print('The most common month is {}, count:{}'.format(common_month,countmonth))



    # display the most common day of week
    global day
    if day == None:
        common_day = df['day_of_week'].mode()[0]
        daycount = df.groupby(['day_of_week'])['day_of_week'].count()[common_day]
        print('The most common day is {}, count:{}'.format(common_day,daycount))


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    hourcount = df.groupby(['hour'])['hour'].count()[common_hour]
    print('The most common hour is {}, count:{}'.format(common_hour,hourcount))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    count_start = df.groupby(['Start Station'])['Start Station'].count()[common_sstation]
    print('The most common Start Station is {}, count:{}'.format(common_sstation,count_start))


    # display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    count_end = df.groupby(['End Station'])['End Station'].count()[common_estation]
    print('The most common End Station is {}, count:{}'.format(common_estation,count_end))


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] +' to '+ df['End Station']
    frequent_trip = df['Trip'].mode()[0]
    count_trip = df.groupby(['Trip'])['Trip'].count()[frequent_trip]
    print('The most Frequent Trip is {}, count:{}'.format(frequent_trip,count_trip))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = sum(df['Trip Duration'])
    print('Total Travel Time is {}'.format(total_time))
   

    # display mean travel time
    Mean = df['Trip Duration'].mean()
    print('Mean travel time is {}'.format(Mean))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users = df['User Type'].value_counts()
    print(users,'\n')
    

    # Display counts of gender and earliest, most recent, and most common year of birth
    if city!= 'washington':
        gender = df['Gender'].value_counts()
        print(gender,'\n')
        print('Earliest year is {}'.format(df['Birth Year'].min()))
        print('Most recent year is {}'.format(df['Birth Year'].max()))
        print('Most common year is {}'.format(df['Birth Year'].mode()[0]))
 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_date(df):
    start = 0
    stop = 5
    while True:
        disp = input('Would you like to display individual data? type "yes" or "no" \n')
        if disp not in ['yes','no']:
            print('enter your answer again')
            disp = input('Would you like to display individual data? type "yes" or "no" \n')     
        if disp == 'yes':
            for num in range(start,stop):
                start += 1
                stop += 1
                print(df.iloc[num],'\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        global df
        df = load_data(city, month, day)
        if len(df) == 0:
            print('There is no data under this filter')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_date(df)
        

        restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
