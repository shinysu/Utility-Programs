from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
CHROME_PATH = '/Users/shinysuresh/Documents/chromedriver'
options = Options()
options.headless = True
driver = webdriver.Chrome(CHROME_PATH, options=options)


def write_csv_file(row):
    with open('description.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)


def read_input_file():
    with open('terms.txt', 'r') as fread:
        words = fread.readlines()
    return [word.strip() for word in words]


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
        row = [word, snippet.text, link.get_attribute('href')]
        write_csv_file(row)

    except Exception as e:
        print("No snippet found")


def search_term(word):
    search_query = "define+'" + word + "'"
    driver.get('https://google.com/search?q=' + search_query)
    get_link_description()


words = read_input_file()
fields = ['term', 'description', 'link']
write_csv_file(fields)
for word in words:
    search_term(word)
driver.quit()