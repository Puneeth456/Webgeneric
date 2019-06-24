from pages.LoginPage import Login
from data.Testdata import *
import pytest

# launch the browser and login
@pytest.mark.usefixtures("test_setup")
class Testlogin:
    def test_login(self):
        driver=self.driver
        time=Login(driver)
        time.logintime(USERNAME,PASSWORD)




# go to the home page
# def test_logoutact():
#     driver.implicitly_wait(20)
#     driver.find_element_by_id("logoutLink").click()




