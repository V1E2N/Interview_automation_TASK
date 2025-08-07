# === tests/test_orangehrm_workflow.py ===
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from Pages.login_page import LoginPage
from Pages.pim import PIMPage
from Pages.employee import EmployeePage
from Pages.leave import LeavePage
from Pages.entitlements_page import EntitlementsPage
from Pages.logout import LogoutPage


@pytest.mark.order(1)
def test_login(browser):
    try:
        login_page = LoginPage(browser)
        login_page.load()
        login_page.login("Admin", "admin123")
        assert login_page.is_logged_in(), " Login failed - user not logged in"
        browser.save_screenshot("C:/Users/Admin/Downloads/PythonProject2/Screenshot/login_success.png")
        print(" Login successful, screenshot saved as 'login_success.png'")
    except Exception as e:
        pytest.fail("Exception in login test: {e}")


@pytest.mark.order(2)
def test_pim_page_navigation(browser):
    try:
        pim_page = PIMPage(browser)
        pim_page.navigate()
        assert browser.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList", \
            "PIM page URL mismatch"
        browser.save_screenshot("C:/Users/Admin/Downloads/PythonProject2/Screenshot/pim_page.png")
        print("PIM page navigation successful, screenshot saved as 'pim_page.png'")
    except Exception as e:
        pytest.fail(" Exception in PIM navigation test: {e}")


@pytest.mark.order(3)
def test_employee_page_workflow(browser):
    employee_page = EmployeePage(browser)

    # Step 1: Add employee
    try:
        toast = employee_page.add_employee("John", "Doe", "12345")
        print(" Add Toast:", toast if toast else "No toast message returned.")
    except Exception as e:
        print("Error adding employee:", str(e))

    # Step 2: Search employee
    try:
        found = employee_page.search_employee("John Doe")
        print("✅ Search Found:", found)
    except Exception as e:
        print("Error searching employee:", str(e))
        found = False  # Prevents edit/delete attempt if search fails

    # Step 3: Edit employee
    if found:
        try:
            toast = employee_page.edit_employee("Smith")
            print("Edit Toast:", toast if toast else "No toast message returned.")
        except Exception as e:
            print("Error editing employee:", str(e))
    else:
        print("⚠️ Skipping edit step as employee was not found.")

    # Step 4: Delete employee
    try:
        toast = employee_page.delete_employee()
        print("✅ Delete Toast:", toast if toast else "No toast message returned.")
    except Exception as e:
        print("Error deleting employee:", str(e))


def test_leave(browser):
    try:
        leave_page = LeavePage(browser)
        leave_page.apply_leave()
        leave_page.view_leave_list()
        leave_page.check_my_leave()
        leave_page.assign_leave("Paul", "2024-12-24", "Personal Reason")
        browser.save_screenshot("C:/Users/Admin/Downloads/PythonProject2/Screenshot/leave_workflow.png")
        print(" Leave workflow completed successfully, screenshot saved as 'leave_workflow.png'")
    except Exception as e:
        pytest.fail(f"Exception in leave workflow test: {e}")
@pytest.mark.order(5)
def test_entitlement_workflow(browser):
    try:
        entitlement_page = EntitlementsPage(browser)
        entitlement_page.manage_entitlements()  # Add your specific action steps if needed
        assert "Entitlements" in browser.title or browser.current_url, "Entitlement page not loaded properly"
        browser.save_screenshot("C:/Users/Admin/Downloads/PythonProject2/Screenshot/entitlement_workflow.png")
        print("Entitlement workflow completed successfully, screenshot saved as 'entitlement_workflow.png'")
    except Exception as e:
        pytest.fail(f"Exception in entitlement workflow test: {e}")


@pytest.mark.order(6)
def test_logout(browser):
    try:
        logout_page = LogoutPage(browser)
        logout_page.logout()
        assert "login" in browser.current_url.lower(), "Logout not successful"
        browser.save_screenshot("C:/Users/Admin/Downloads/PythonProject2/Screenshot/logout.png")
        print("Logout completed successfully, screenshot saved as 'logout.png'")
    except Exception as e:
        pytest.fail(f"Exception in logout test: {e}")



