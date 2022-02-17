import os
from selenium import webdriver
import random
class Bot:
    def __init__(self):

                  
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        # self.options.binary_location =  
        # os.environ.get('GOOGLE_CHROME_BIN')
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        # self.options.add_argument('--proxy-server=%s' %proxy_ip_port)
        self.options.add_argument('--disable-dev-shm-usage')
        # self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path= 'chromedriver.exe', options=self.options)
        
        