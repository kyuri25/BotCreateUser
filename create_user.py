from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class Criaruser:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    def Iniciar(self):
        name = input('name: ')
        user = input('user: ')
        email = input('Email: ')
        company = input('company:')
        groups = input('groups: ')

        self.driver.get('https://site.empresa.org/AccessControl/User')

        time.sleep(10)

        link_email = self.driver.find_element_by_id('username')
        link_email.click()
        link_email.send_keys('your.username')

        time.sleep(5)

        link_password = self.driver.find_element_by_id('password')
        link_password.click()
        link_password.send_keys('password')

        time.sleep(5)

        login = self.driver.find_element_by_tag_name('button')
        login.click()

        time.sleep(10)

        select_company = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/a')
        select_company.click()

        time.sleep(5)

        click_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button/span[2]')
        click_new.click()

        time.sleep(5)

        type_name = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div[1]/div[2]/input')
        type_name.click()
        type_name.send_keys(name)

        type_user = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div[2]/div[2]/input')
        type_user.click()
        type_user.send_keys(user)

        type_email = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div[3]/div[2]/input')
        type_email.click()
        type_email.send_keys(email)

        clicar_save = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div/div[2]/button[2]/span[2]')
        clicar_save.click()

        time.sleep(5)

        member_group = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div[3]/button/span[2]')
        member_group.click()

        time.sleep(5)

        list_groups = self.driver.find_elements_by_class_name(
            'form-control.ng-pristine.ng-valid.ng-empty.ng-touched')
        time.sleep(1)
        list_groups.send_keys(groups)
        time.sleep(1)
        list_groups.send_keys(Keys.ENTER)
        time.sleep(1)
        list_groups.send_keys(Keys.DOWN)
        time.sleep(1)
        list_groups.send_keys(Keys.ENTER)
        time.sleep(1)

        add_group = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div/div[3]/button')
        add_group.click()

        time.sleep(2)

        click_return_group = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button/span[2]')
        click_return_group.click()

        time.sleep(5)

        member_company = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div[7]/div[3]/button/span[2]')
        member_company.click()

        time.sleep(5)

        list_company = self.driver.find_elements_by_css_selector(
            '#\\32 45f4b7d-b3d5-4188-a403-65c15c2c11ff')
        list_company.click()
        list_company.send_keys(company)
        time.sleep(1)
        list_company.send_keys(Keys.ENTER)
        time.sleep(1)
        list_company.send_keys(Keys.DOWN)
        time.sleep(1)
        list_company.send_keys(Keys.ENTER)
        time.sleep(1)

        add_company = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/form/div/div[3]/button')
        add_company.click()

        click_return_company = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button/span[2]')
        click_return_company.click()

        time.sleep(5)

        click_return_all = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div/div/button/span[2]')
        click_return_all.click()


criar = Criaruser()
criar.Iniciar()
