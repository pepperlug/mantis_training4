from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper

class Application:
    def __init__(self,browser,base_url):
        if browser == "firefox":
            #запуск FireFox
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.wd = webdriver.Firefox(
                executable_path=r'C:\Windows\SysWOW64\geckodriver.exe',
                options=options
            )
            #self.wd = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            #запуск Chrome
            self.wd = webdriver.Chrome()
        elif browser == "opera":
            #запуск Оперы
            self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognized browser %s" + browser)
        self.wd.implicitly_wait(5)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
