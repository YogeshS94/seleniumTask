import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='class')
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path=r"C:\Users\60028440\PycharmProjects\SeleniiumTask\Driver\chromedriver.exe", chrome_options=options)
    f = open("conf.json")
    data = json.load(f)
    driver.get(data['url'])
    request.cls.driver = driver
    yield
    # driver.close()

