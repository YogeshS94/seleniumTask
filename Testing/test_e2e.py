import json
from time import sleep

import pytest
# from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass



@pytest.mark.usefixtures('setup')
class TestE2E(BaseClass):
    def test_e2e(self):
        # l = open(r"C:\Users\60028440\PycharmProjects\seleniumTask\pageObject\HomePage.json")
        # data = json.load(l)
        log = self.getLogger()
        title = self.driver.title
        log.info(f'Title of the page is: {title}')
        # driver = webdriver.Chrome(executable_path=r"C:\Users\60028440\PycharmProjects\SeleniiumTask\Driver\chromedriver.exe")
        homepage = HomePage(self.driver)
        homepage.home_page_details().click()
        currentUrl = self.driver.current_url
        log.info(currentUrl)
        headerText = homepage.flight_header_text().text
        log.info(headerText)
        oneWayBtn = homepage.one_way_button().click()
        log.info(f'One way button is clicked: {oneWayBtn}')
        roundTripBtn = homepage.round_trip_button().click()
        log.info(f'Round Trip button is clicked: {roundTripBtn}')
        multiCityBtn = homepage.multi_city_button().click()
        log.info(f'Multi-City button is clicked: {multiCityBtn}')
        homepage.one_way_button().click()
        # Click the From Texbox Drop down
        homepage.from_textbox().click()
        self.driver.execute_script("arguments[0].value='Chennai ';", homepage.enter_value_text())
        sleep (2)
        homepage.enter_value_text().send_keys(Keys.TAB)
        homepage.enter_value_text().send_keys(Keys.BACKSPACE)
        sleep(3)
        ac = ActionChains(self.driver)
        ch = self.driver.find_element_by_xpath('//li[@class="sc-iUKqMP hlZHGM"][1]')
        ac.move_to_element(ch).perform()
        ac.click().perform()
        fr = self.driver.execute_script("return document.getElementsByClassName('sc-dJjYzT cjzxWN fswWidgetTitle')[0];")
        log.info(f'Value of from dropdown is : {fr.text}')

        # Click the To Texbox Drop down
        self.driver.execute_script("arguments[0].value='Mumbai ';", homepage.enter_value_text())
        sleep(2)
        homepage.enter_value_text().send_keys(Keys.TAB)
        homepage.enter_value_text().send_keys(Keys.BACKSPACE)
        sleep(3)
        ch = self.driver.find_element_by_xpath('//li[@class="sc-iUKqMP hlZHGM"][2]')
        ac.move_to_element(ch).perform()
        ac.click().perform()

        # Selection of from date
        sleep(3)
        date = self.driver.find_element_by_xpath('//div[@class="DayPicker-Day"][contains(@aria-label,"Apr 01")]')
        ac.move_to_element(date).perform()
        ac.click().perform()
        # HomePage.from_date.click()
        homepage.from_date_done().click()

        # Adding number of passengers
        homepage.adult_number_add().click()
        for i in range(0,2):
            homepage.children_number_add().click()
        homepage.children_number_remove().click()
        homepage.infant_number_add().click()
        homepage.travel_class().click()
        checkClassTraveler = []
        checkClassTraveler = homepage.travellers_class_check()
        log.info(checkClassTraveler.text)
        homepage.press_done().click()

        ac.move_to_element(homepage.armed_force()).perform()
        hiddentTxt1 = homepage.hidden_text_armed_force()
        log.info(hiddentTxt1.text)

        homepage.press_search_flight().click()




