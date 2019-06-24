from pages.Webgeneric import Webgeneric

class Login(Webgeneric):
    def __init__(self,driver):
        Webgeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="username"
        self.pwd_name="pwd"
        self.login_btn_xpath="//a[@id='loginButton']"


    def logintime(self,un,pwd):
        wg=Webgeneric(self.driver)
        wg.enter(self.un_id,un)
        wg.enter(self.pwd_name,pwd)
        wg.submit(self.login_btn_xpath)

        #
        # self.driver.find_element_by_id(self.un_id).send_keys(un)
        # self.driver.find_element_by_name(self.pwd_name).send_keys(pwd)
        # self.driver.find_element_by_xpath(self.login_btn_xpath).click()