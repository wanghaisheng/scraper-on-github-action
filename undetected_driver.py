#template for scrape
from selenium import webdriver
import undetected_chromedriver as uc
import seleniumwire.undetected_chromedriver as seleniumwireundetectedchromedriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
print('demo scrape using playwright')

#https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/347


# from webdriver_manager.utils import get_browser_version_from_os

# version = get_browser_version_from_os("google-chrome")

# print(version)



# # undetected_chromedriver==3.1.3
# from undetected_chromedriver import Chrome

# if __name__ == "__main__":
#     ctx = Chrome(headless=True)
#     try:
#         ctx.get("https://www.baidu.com")
#     finally:
#         ctx.quit()


def get_undetected_webdriver(proxy):

    seleniumwire_options = {
        'proxy': {
            'http': 'socks5://127.0.0.1:1080',  # user:pass@ip:port
            'https': 'socks5://127.0.0.1:1080',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    options = seleniumwireundetectedchromedriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    if os.environ.get("GOOGLE_CHROME_BIN"):
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # ChromeDriverManager().install()
    # Use with Chromium
    # Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    # Use with Chrome
    
    driver = ''
    if os.environ.get("CHROMEDRIVER_PATH"):
        executable_path = os.environ.get("CHROMEDRIVER_PATH")
    # driver = webdriver.Chrome(options = options, seleniumwire_options = seleniumwire_options, version_main = my_version)
        if proxy==False:
              driver = seleniumwireundetectedchromedriver.Chrome(
            options=options, executable_path=executable_path)
        else:
            driver = seleniumwireundetectedchromedriver.Chrome(
            options=options, executable_path=executable_path, seleniumwire_options=seleniumwire_options)
    else:
        if proxy==False:
            print('start uc no proxy')
            driver = seleniumwireundetectedchromedriver.Chrome(
            options=options)
        else:
            print('start uc with proxy')
            service=Service(ChromeDriverManager().install())
            driver = seleniumwireundetectedchromedriver.Chrome(service=service,
            options=options, seleniumwire_options=seleniumwire_options)
    return driver


# def get_a_driver(browser: BrowsersEnum, is_headless=True, seleniumwire_options=None):
#     if browser is BrowsersEnum.FIREFOX:
#         options = webdriver.FirefoxOptions()
#         options.headless = is_headless
#         from selenium.webdriver.firefox.service import Service
#         from webdriver_manager.firefox import GeckoDriverManager
#         service = Service(GeckoDriverManager().install())
#         return webdriver.Firefox(service=service, options=options, seleniumwire_options=seleniumwire_options)
#     if browser is BrowsersEnum.CHROME:
#         options = webdriver.ChromeOptions()
#         options.headless = is_headless
#         from selenium.webdriver.chrome.service import Service
#         from webdriver_manager.chrome import DriverManager
#         service = Service(DriverManager().install())
#         return webdriver.Chrome(service=service, options=options)
#     if browser is BrowsersEnum.CHROMIUM:
#         from selenium.webdriver.chromium.options import ChromiumOptions
#         from selenium.webdriver.chromium.webdriver import ChromiumDriver
#         from selenium.webdriver.chromium.webdriver import ChromiumDriver
#         options = ChromiumOptions()
#         options.headless = is_headless
#         from selenium.webdriver.chromium.service import ChromiumService
#         from webdriver_manager.chrome import ChromeDriverManager
#         from webdriver_manager.utils import ChromeType
#         service = ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),
#                                   start_error_message='Couldnt start')
#         return ChromiumDriver(service=service, options=options, browser_name="chromium", vendor_prefix="webkit",
#                               seleniumwire_options=seleniumwire_options)