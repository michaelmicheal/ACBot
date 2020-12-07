from selenium import webdriver
from enum import Enum
import datetime
import constants

class State(Enum):
    SETUP = 1
    LOGIN = 2
    BOOKINGS = 3
    WAIVERS = 4

class ACBotException(Exception):
    pass

class IncorrectStateException(ACBotException):
    pass

class FullyBookedException(ACBotException):
    pass

class UnFoundEventException(ACBotException):
    pass

class WaiverException(ACBotException):
    pass

class AccountNumException(ACBotException):
    pass

class ACBot:

    def __init__(self):
        self.state = State.SETUP
        self.driver = webdriver.Chrome(constants.CHROMEDRIVER_LOCATION)
    
    ## Helper Methods

    def __fill_input(self, input_name, string_input):
        x_path = '//input[@name="{0}"]'.format(input_name)
        try:
            input_component = self.driver.find_element_by_xpath(x_path)
        except:
            print('Could not find "{0}" input'.format(input_name))
        input_component.send_keys(string_input)

    def __press_button(self, button_name):
        try:
            button = self.driver.find_element_by_xpath('//button[@name="{0}"]'.format(button_name))
        except:
            print('Could not find "{0}" button'.format(button_name))
        button.click()

    def __select_dropdown(self, select_name, option_text):
        try:
            option = self.driver.find_element_by_xpath('//select[@name="{0}"]/option[text()="{1}"]'.format(select_name, option_text))
        except:
            print('Could not find "{0}" select'.format(select_name))
        option.click()
    
    ## External Methods

    def load_site(self):
        if not self.state == State.SETUP:
            raise IncorrectStateException
        self.driver.get(constants.LOGIN_LINK)
        self.state = State.LOGIN
    
    def login(self):
        if not self.state == State.LOGIN:
            raise IncorrectStateException
        if constants.ACCOUNT_NUM == 1:
            username = constants.USERNAME1
            password = constants.PASSWORD1
        elif constants.ACCOUNT_NUM == 2:
            username = constants.USERNAME2
            password = constants.PASSWORD2
        else:
            raise AccountNumException
        self.__fill_input('UserLogin', username)
        self.__fill_input('Password', password)
        self.__press_button('submit_Login')
        self.state = State.BOOKINGS

    def extend_table(self):
        if not self.state == State.BOOKINGS:
            raise IncorrectStateException
        self.__select_dropdown('DataTables_Table_1_length', 'All')

    def refresh(self):
        self.driver.refresh()

    def reserve(self, event_title, event_date_time=None, any_time=False):
        
        if not self.state == State.BOOKINGS:
            raise IncorrectStateException

        # event name component criteria
        event_name_search_xpath = '//td[contains(text(),"{0}")]'.format(event_title)

        # event date and time component criteria
        if event_date_time is not None:
            date_string = event_date_time.strftime("%Y-%m-%d")
            event_date_search_xpath = '//td[contains(text(),"{0}")]'.format(date_string)

            time_string = event_date_time.strftime("%H:%M:%S")
            event_time_search_xpath = '//td[contains(text(),"{0}")]'.format(time_string)

            criteria_list = [event_name_search_xpath, event_date_search_xpath]
            if not any_time:
                criteria_list.append(event_time_search_xpath)
            event_col_xpath = '/..'.join(criteria_list)
        
        else:
            event_col_xpath = event_name_search_xpath


        # finding the event row
        try:
            self.driver.find_element_by_xpath(event_col_xpath)
        except:
            raise UnFoundEventException
        
        # finding the associated reserve button
        event_reg_xpath = '{0}/..//button[contains(text()," Reserve ")]'.format(event_col_xpath)
        try:
            reserve_button = self.driver.find_element_by_xpath(event_reg_xpath)
            self.state = State.WAIVERS
        except:
            raise FullyBookedException
        print('clicking reserve button')

        reserve_button.click()
    
    def accept_waivers(self):
        if not self.state == State.WAIVERS:
            raise IncorrectStateException

        try:
            self.__select_dropdown('waiver1', 'I Agree to the terms above')
        except:
            raise WaiverException
        try:
            self.__select_dropdown('waiver2', 'I Agree to the terms above')
        except:
            raise WaiverException

        self.__press_button('makereservation')
        self.state = State.BOOKINGS

    


