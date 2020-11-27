import os
import datetime as dt
from dotenv import load_dotenv

# Don't Change this
LOGIN_LINK = "https://www.laurierathletics.com/ecommerce/user/index.php"
load_dotenv()
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
# Don't Change this


# Change this to have the location of your ChromeDriver executable
CHROMEDRIVER_LOCATION = "/usr/local/bin/chromedriver"

# Change this to be the date/time you want to work out
FITNESS_DATE_TIME = dt.datetime(year = 2020, month= 12, day = 1, hour = 9)

# Change this to be the date/time you want AC Bot to book at
SCHEDULE_DATE_TIME = dt.datetime(year = 2020, month = 11, day = 27, hour = 13)
