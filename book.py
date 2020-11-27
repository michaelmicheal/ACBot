from ACBot import ACBot, ACBotException
import datetime as dt
from datetime import timedelta
import threading
import time
import constants

def book(event_name, fitness_date_time, schedule_date_time=None):
    
    if schedule_date_time is not None:
        login_date_time = schedule_date_time - timedelta(minutes=1)
        login_delay_seconds = (login_date_time - dt.datetime.now()).total_seconds()
        print('{0} Seconds Until Login'.format(login_delay_seconds))

        time.sleep(login_delay_seconds)

    print('Starting Bot at: {}'.format(dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))

    for i in range(3):
        try:
            bot = ACBot()
            bot.load_site()
            bot.login()
            bot.extend_table()
            break
        except:
            if i < 2:
                time.sleep(2)
                continue
            else:
                raise
    
    if schedule_date_time is not None:
        schedule_delay_seconds = (schedule_date_time - dt.datetime.now()).total_seconds()
        time.sleep(schedule_delay_seconds)

    for i in range(21):
        
        print(i)
        if i > 5:
            time.sleep(5)
        try:
            print('Refreshing and booking at: {}'.format(dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
            bot.refresh()
            bot.reserve(event_name, fitness_date_time)
            break
        except ACBotException as e:
            if i == 20:
                raise e
            else:
                continue
    bot.accept_waivers()
    print("Booking Complete!")
    
