## Configure Project
1. If you do not have Python installed, [download and install Python](https://www.python.org/downloads/)
2. Clone ACBot locally.
3. In terminal, navigate to ACBot directory.
4. Install dependencies: `pip install -r requirements.txt`
5. Install ChromeDriver (make sure you also have chrome installed)  
    For macos, run `brew cask install chromedriver`  
    **If you have issues lauching ChromeDriver refer [here](https://stackoverflow.com/a/60374958)**  
    For Windows, refer to [here](https://www.kenst.com/2019/02/installing-chromedriver-on-windows/)
6. Configure Username and Password
    - Rename the '.env.sample' file as '.env'
    - Open the file and insert your LaurierAthletics username and passwords as
        ```{python}
        USERNAME='your_username'
        PASSWORD='your_password'
        ```

## Using ACBot to Schedule Fitness
To schedule fitness you need to configure date/time constants and run the fitness.py file more than 1 minute before you want to schedule a fitness slot (usually when the spot or a set of spots open). The program will login to LaurierAthletics.com 1 minute before the time you want it to schedule your fitness slot. Then at the time you specify it should schedule your slot, it will refresh, find the slot, reserve it, and sign the waivers. To configure and run ACBot to schedule fitness,
1. Open the 'constants.py' file and update the date constants
2. Update the fitness time. This is the date and time that you want to be at the gym.
    ```{python}
    # Change this to be the date/time you want to work out
    FITNESS_DATE_TIME = dt.datetime(year = 2020, month= 12, day = 1, hour = 9)
    ```
3. Update the schedule time. This is the time that a booking you want to pick will come out.
    ```{python}
    # Change this to be the date/time you want AC Bot to book at
    SCHEDULE_DATE_TIME = dt.datetime(year = 2020, month = 11, day = 27, hour = 12)
    ```
4. Update the any time parameter. If you don't care what time you're in the gym, and want to maximize the likelihood you reserve a spot, you set it as TRUE.
    ```{python}
    # Make this True if you don't care what time slot you get on the date
    ANY_TIME = True
    ```

5. Open a terminal window and navigate to the project directory
6. Enter the command `python fitness.py`

