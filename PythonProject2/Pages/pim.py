from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        wait = WebDriverWait(self.driver, 10)

        # 1. Click on "PIM"
        pim_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM")))
        pim_menu.click()

        # 2. Hover over or click "Configuration"
        config_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Configuration']")))

        # Hover over the Configuration menu to reveal sub-items
        ActionChains(self.driver).move_to_element(config_menu).perform()
        time.sleep(1)  # Optional small wait in case submenu is animated

        # 3. Click on "Data Import"
        data_import_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Data Import']")))
        data_import_option.click()
