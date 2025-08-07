from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class EmployeePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_toast_message(self):
        try:
            toast = self.wait.until(
                EC.visibility_of_element_located((By.ID, "oxd-toaster_1"))
            )
            return toast.text
        except TimeoutException:
            return None

    def add_employee(self, first, last, emp_id):
        try:
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))).click()
            self.wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first)
            self.driver.find_element(By.NAME, "lastName").send_keys(last)

            emp_id_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='Employee Id']/following::input[1]"))
            )
            emp_id_input.clear()
            emp_id_input.send_keys(emp_id)

            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            return self.get_toast_message()
        except Exception as e:
            print(f"[ERROR] Failed to add employee: {e}")
            return None

    def search_employee(self, name):
        try:
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List"))).click()
            search_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='Employee Name']/following::input[1]"))
            )
            search_box.clear()
            search_box.send_keys(name)

            self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

            # Wait for the result row to appear
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='row' and .//div[contains(text(), '{}')]]".format(name))))
            return True
        except TimeoutException:
            print(f"[WARNING] Employee '{name}' not found in search.")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to search employee: {e}")
            return False

    def edit_employee(self, new_last):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']"))).click()

            last_name = self.wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name.clear()
            last_name.send_keys(new_last)

            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            return self.get_toast_message()
        except Exception as e:
            print(f"[ERROR] Failed to edit employee: {e}")
            return None

    def delete_employee(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List"))).click()

            delete_icon = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']"))
            )
            delete_icon.click()

            confirm_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']"))
            )
            confirm_button.click()

            return self.get_toast_message()
        except Exception as e:
            print(f"[ERROR] Failed to delete employee: {e}")
            return None
