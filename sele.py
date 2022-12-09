import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver


class Crawling:
    def __init__(self, url):
        options = webdriver.ChromeOptions()

        options.add_argument('headless')
        options.add_argument('no-sandbox')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options)
        url = urllib.parse.quote(url, safe="")

        lenUrl = "https://lens.google.com/uploadbyurl?url=" + url
        self.driver.get(lenUrl)

    def get_site_info(self):
        name = ''

        # get google lens info
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        grids = soup.find('div', class_='aah4tc')

        # loop child in grids
        for grid in grids.findChildren('div', class_='UAiK1e', limit=1):
            name = grid.text.split('|')[0].strip()

        self.driver.close()

        return name
