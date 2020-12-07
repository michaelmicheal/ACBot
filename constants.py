import os
import datetime as dt
from dotenv import load_dotenv

# Don't Change this
LOGIN_LINK = "https://www.laurierathletics.com/ecommerce/user/index.php"
load_dotenv()
USERNAME1 = os.environ["USERNAME1"]
PASSWORD1 = os.environ["PASSWORD1"]

USERNAME2 = os.environ["USERNAME2"]
PASSWORD2 = os.environ["PASSWORD2"]
# Don't Change this


# Change this to have the location of your ChromeDriver executable
CHROMEDRIVER_LOCATION = "/usr/local/bin/chromedriver"

# Change this to be the date/time you want to work out
FITNESS_DATE_TIME = dt.datetime(year = 2020, month= 12, day =11, hour = 9)

# Change this to be the date/time you want AC Bot to book at
SCHEDULE_DATE_TIME = dt.datetime(year = 2020, month = 12, day = 7 , hour = 9)

# Make this True if you don't care what time slot you get on the date
ANY_TIME = True

# Account Number
ACCOUNT_NUM = 1