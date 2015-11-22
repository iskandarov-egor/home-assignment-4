from selenium.webdriver.common.by import By


class MainPageLocators(object):
    USERNAME_FIELD = (By.ID, 'ph_login')
    PASSWORD_FIELD = (By.ID, 'ph_password')
    LOGIN_BUTTON = (By.ID, 'PH_authLink')
    USER_EMAIL_HREF = (By.ID, "PH_user-email")
    LOGOUT_BUTTON = (By.ID, "PH_logoutLink")