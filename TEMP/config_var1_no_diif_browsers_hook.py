#import pytest
#from selenium import webdriver

#link = "https://rahulshettyacademy.com/angularpractice"

# до того, как фиксчу вынесли в бейз класс и начали добавлять код для запуска на разных
# браузерах через командную строчку, было так:

#@pytest.fixture(scope="class")
#def prepare_chrome_browser(request):  # request is an instance of the fixture
#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument("--disable-search-engine-choice-screen")
#    driver = webdriver.Chrome(options=chrome_options)
#    driver.maximize_window()
#    driver.implicitly_wait(5)
#    driver.get(link)
#    request.cls.driver = driver  # !!! a trick to return driver (used instead of return driver)
#    yield
#    driver.close()
