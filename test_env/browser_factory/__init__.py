import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowseFactory:

    @staticmethod
    def get_driver():
        driver = None

        match os.getenv('BROWSER'):
            case 'chrome':
                service = Service(ChromeDriverManager().install())
                options = webdriver.ChromeOptions()
                options.add_argument(f'--window-size={os.getenv("SIZE")}')
                driver = webdriver.Chrome(service=service, options=options)
            case 'firefox':
                service = Service(GeckoDriverManager().install())
                options = FirefoxOptions()
                options.add_argument(f'--window-size={os.getenv("SIZE")}')
                driver = webdriver.Firefox(service=service, options=options)
            case _:
                print('Please check the browser name in the .env file. Possible browsers is "chrome" and "firefox".')

        return driver
