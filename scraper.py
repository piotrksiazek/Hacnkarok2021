from selenium import webdriver
import os


class Scraper:
    def __init__(self):
        # options.add_argument(f'user-agent={user_agent}')
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-dev-sh-usage')
        self.options.add_argument('--no-sandbox')

        # for deployment
        self.options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=self.options)

        # for testing
        # self.driver = webdriver.Chrome(executable_path="chromedriver.exe",
        #                                options=self.options)

        
    def get_world_population(self, driver):
        world_population = driver.find_element_by_css_selector('#c1 > div.counter-heading.inactive-header > span.counter-number > span').text
        births_today = driver.find_element_by_css_selector('#c3 > div.counter-heading.inactive-header > span.counter-number > span').text
        deaths_today = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[6]/span[1]/span')[0].text
        growth_today = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div[8]/span[1]/span')[0].text
        population = {
            'world_population': world_population,
            'births': births_today,
            'deaths': deaths_today,
            'growth': growth_today
        }
        return population

    def government_and_economics(self, driver):
        healthcare = driver.find_elements_by_xpath('//*[@id="c8"]/div[1]/span[1]/span')[0].text
        education = driver.find_elements_by_xpath('//*[@id="c9"]/div[1]/span[1]/span')[0].text
        military = driver.find_elements_by_xpath('//*[@id="c10"]/div[1]/span[1]/span')[0].text
        gae = {
            'healthcare': healthcare,
            'education': education,
            'military': military
        }
        return gae

    def get_worldometers(self):
        self.driver.get('https://www.worldometers.info/')
        driver = self.driver
        population = self.get_world_population(driver)
        gae = self.government_and_economics(driver)
        return {'population': population, 'government_and_economics': gae}