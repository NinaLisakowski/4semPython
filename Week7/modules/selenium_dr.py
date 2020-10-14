import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_the_first_latest_article():
    base_url = 'https://wwww.dr.dk/'
    
    # headless is needed here because we do not have a GUI version of firefox
    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
    browser = webdriver.Chrome()

    browser.get(base_url)
    browser.implicitly_wait(3)


    # an overlay element was obscuring the Persons button
    try:
        # Cookies popup select
        WebDriverWait(browser, 20).until(lambda browser: browser.execute_script(
            "return document.readyState;") == "complete")
        # Wait for the popup to open
        sleep(5)
        element = browser.find_element_by_xpath(
            '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowSelection"]')
        browser.execute_script('arguments[0].click();', element)
        print('Cookie Button', element)

        # Wait for next page to load
        sleep(5)
        # First article selector
        cookie_button2 = browser.find_element_by_css_selector(
            'body > div:nth-child(3) > div > div.dre-site-wrapper > div > main > div:nth-child(3) > div > div > div.hydra-front-page-latest-news > div.hydra-front-page-latest-news__track > div > div > div > ul > li.dre-slide-band-track__item.dre-slide-band-track__item--first.dre-slide-band-track__item--snap')
        print('Cookie Button2', cookie_button2)
        cookie_button2.click()
    except Exception as e:
        print('BUTTON EXCEPTION', e)

    try:
        # Wait for next page to load
        WebDriverWait(browser, 20).until(lambda browser: browser.execute_script(
            "return document.readyState;") == "complete")

        # Get website information
        page_source = browser.page_source

        # Soup it
        soup = bs4.BeautifulSoup(page_source, 'html.parser')
        return soup
    except Exception as e:
        print('SOUP EXCEPTION', e)