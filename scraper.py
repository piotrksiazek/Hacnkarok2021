from selenium import webdriver
import os


class Scraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
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

    def parse_num(self, num):
        result = ''
        for char in num:
            if char != ',':
                result += char
        return int(result)

    def daily(self, num):
        return str(int(self.parse_num(num)/365))


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

    def food(self, driver):
        died_of_hunger = driver.find_elements_by_xpath('//*[@id="c32"]/div[1]/span[1]/span')[0].text
        money_spent_on_obesity = driver.find_elements_by_xpath('//*[@id="c33"]/div[1]/span[1]/span')[0].text
        money_spent_on_weight_loss = driver.find_elements_by_xpath('//*[@id="c34"]/div[1]/span[1]/span')[0].text
        food = {
            'died_of_hunger': died_of_hunger,
            'money_spent_on_obesity': money_spent_on_obesity,
            'money_spent_on_weight_loss': money_spent_on_weight_loss
        }
        return food

    def health(self, driver):
        accidents = driver.find_elements_by_xpath('//*[@id="c62"]/div[1]/span[1]/span')[0].text
        abortions = driver.find_elements_by_xpath('//*[@id="c51"]/div[1]/span[1]/span')[0].text
        cancer_deaths = driver.find_elements_by_xpath('//*[@id="c55"]/div[1]/span[1]/span')[0].text
        suicides = driver.find_elements_by_xpath('//*[@id="c60"]/div[1]/span[1]/span')[0].text
        health = {
            'accidents': self.daily(accidents),
            'abortions': self.daily(abortions),
            'cancer_deaths': self.daily(cancer_deaths),
            'suicides': self.daily(suicides)
        }
        return health

    def energy(self, driver):
        oil_barrels = driver.find_elements_by_xpath('//*[@id="c42"]/div[1]/span[1]/span')[0].text
        energy = {
            'oil_barrels': oil_barrels,
        }
        return energy
    def get_worldometers(self):
        self.driver.get('https://www.worldometers.info/')
        driver = self.driver

        gae = self.government_and_economics(driver)
        food = self.food(driver)
        health = self.health(driver)
        energy = self.energy(driver)

        return {
            'government_and_economics': gae,
            'food': food,
            'health': health,
            'energy': energy
        }