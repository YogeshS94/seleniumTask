import json
import random
import string

import pytest
from selenium import webdriver

from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures('setup')
class HomePage(BaseClass):
    f = open(r'C:\Users\60028440\PycharmProjects\seleniumTask\pageObject\HomePage.json')
    data = json.load(f)
    def __init__(self,driver):
        self.driver = driver

    def home_page_details(self):


        return self.driver.find_element_by_xpath(self.data['flight-link'])
        # driver = webdriver.Chrome(executable_path=r"C:\Users\60028440\PycharmProjects\SeleniiumTask\Driver\chromedriver.exe")
        # driver.find_element_by_xpath()

    def flight_header_text(self):
        return self.driver.find_element_by_xpath('//h2[contains(text(),"Book Domestic")]')

    def one_way_button(self):
        return self.driver.find_element_by_xpath('//span[text()="One-way"]')
    import random
    def random_generator(self, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(8))

    def round_trip_button(self):
        return self.driver.find_element_by_xpath('//span[text()="Round-trip"]')

    def multi_city_button(self):
        return self.driver.find_element_by_xpath('//span[text()="Multi-city"]')

    def from_textbox(self):
        # return self.driver.find_element_by_xpath('//div[@class ="sc-bkkeKt gAqCbJ fswFld"]')
        return self.driver.find_element_by_xpath('//span[text() ="From"]')

    def enter_value_text(self):
        a = self.driver.find_element_by_xpath('//input[@type="text"]')
        return a

    def from_date(self):
        return self.driver.find_element_by_xpath('//div[@class="DayPicker-Day"][contains(@aria-label,"Apr 01")]')

    def from_date_done(self):
        return self.driver.find_element_by_xpath('//span[@class="fswTrvl__done"]')

    def adult_number_add(self):
        return self.driver.find_element_by_xpath('//div[@class="sc-ehCJOs kXqgMf"][1]//div[@class="sc-clIzBv gFdmFA"]//span[@class="sc-faUpoM jSgnBw"][2]')

    def children_number_add(self):
        return self.driver.find_element_by_xpath('//div[@class="sc-ehCJOs kXqgMf"][2]//div[@class="sc-clIzBv gFdmFA"]//span[@class="sc-faUpoM jSgnBw"][2]')

    def infant_number_add(self):
        return self.driver.find_element_by_xpath('//div[@class="sc-ehCJOs kXqgMf"][3]//div[@class="sc-clIzBv gFdmFA"]//span[@class="sc-faUpoM jSgnBw"][2]')

    def children_number_remove(self):
        return self.driver.find_element_by_xpath('//div[@class="sc-ehCJOs kXqgMf"][2]//div[@class="sc-clIzBv gFdmFA"]//span[@class="sc-faUpoM jSgnBw"][1]')

    def travel_class(self):
        return self.driver.find_element_by_xpath('//li[@class="sc-hiwPVj fFWmQL"][2]')

    def travellers_class_check(self):
        return self.driver.find_element_by_xpath('//p[@class="sc-jOxtWs cRUgor"]')

    def class_check(self):
        return self.driver.find_element_by_css_selector('p[class="sc-hmjpVf bKFxFL"]')

    def press_done(self):
        return self.driver.find_element_by_css_selector('a[class="sc-dtMgUX daltrV"]')

    def armed_force(self):
        return self.driver.find_element_by_css_selector('li[class="sc-eCImPb jasfVq"]')

    def hidden_text_armed_force(self):
        return self.driver.find_element_by_css_selector('span[class="fswTooltip__text"]')

    def press_search_flight(self):
        return self.driver.find_element_by_css_selector('span[class="sc-fHeRUh jHgPBA"]')






