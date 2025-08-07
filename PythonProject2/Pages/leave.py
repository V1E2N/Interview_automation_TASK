import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def apply_leave(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Apply']"))
        ).click()

        # Wait for From Date field
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='From Date']/following::input[1]"))
        ).click()

        # Select From Date
        self.driver.find_element(By.XPATH, "//label[text()='From Date']/following::input[1]").send_keys("2024-12-20")

        # Select To Date
        self.driver.find_element(By.XPATH, "//label[text()='To Date']/following::input[1]").send_keys("2024-12-21")

        # Select Leave Type
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')]"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='CAN - Bereavement']"))
        ).click()

        # Enter Comment
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Funeral")

        # Click Apply
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()

    def view_leave_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Leave List']"))
        ).click()

    def check_my_leave(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='My Leave']"))
        ).click()

    def assign_leave(self, name, date, reason):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Assign Leave']"))
        ).click()

        # Enter employee name
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        ).send_keys(name)

        # Select leave type
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')]"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='CAN - Personal']"))
        ).click()

        # Enter date
        self.driver.find_element(By.XPATH, "//label[text()='From Date']/following::input[1]").send_keys(date)

        # Enter reason
        self.driver.find_element(By.XPATH, "//textarea").send_keys(reason)

        # Click Assign
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
