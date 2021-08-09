from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
CHROME_PATH = '/Users/shinysuresh/Documents/chromedriver'


def get_link_description():
    try:
        snippet = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]'))
        )
        print(snippet.text)
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="kp-wp-tab-overview"]/div/div/div/div/div/div/div/div/div/span[2]/a'))
        )

        print(link.get_attribute('href'))
        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


word = input("Enter the search term: ")
search_query = "define+" + word
options = Options()
options.headless = True
driver = webdriver.Chrome(CHROME_PATH, options=options)
driver.get('https://google.com/search?q='+search_query)
get_link_description()

