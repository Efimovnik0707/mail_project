from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#td-app-aol-module-2  span.text-label.test")
    LOGOUT_LINK = (By.CSS_SELECTOR, ".ico-logout")
    


class MainPageLocators():
    NEWSLETTER_FORM = (By.CSS_SELECTOR, "#newsletter-email")
    NEWSLETTER_SUB_BUT = (By.CSS_SELECTOR, "#newsletter-subscribe-button")
    NEWSLETTER_RESULT = (By.CSS_SELECTOR, "#newsletter-result-block")
    LOGIN_LINK = (By.CSS_SELECTOR, '#block-block-3 a.zgh-login')
    ACCEPT_BUTTON = (By.CSS_SELECTOR, 'button.btn.primary')
    MAIL_BUTTON = (By.CSS_SELECTOR, '#td-app-aol-module-3 > ul > li.mail-link > a > span.text-label ')
    
    


class LoginPageLocators():
    EMAIL = (By.CSS_SELECTOR, "#login-username")
    PASSWORD = (By.CSS_SELECTOR, "#login-passwd")
    REMEMBER_RADIO_BUTTON = (By.CSS_SELECTOR, "#RememberMe")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-signin")
    MAIL_BUTTON = (By.CSS_SELECTOR, '#td-app-aol-module-3 > ul > li.mail-link > a > span.text-label ')


class InboxPageLocators():
    NEW_MAIL = (By.CSS_SELECTOR, "#zm_lftree  button:nth-child(1)")
    BASKET_BUT = (By.CSS_SELECTOR, "#add-to-cart-button-31")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#bar-notification")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-price > span")
    SUCCESS_BASKET_BUT = (By.CSS_SELECTOR, ".content a")

class MailPageLocators():
    NEW_MAIL = (By.CSS_SELECTOR, ".unselectable.btn.composeBtn")
    EMAIL_RECEIVER = ( By.CSS_SELECTOR, '#toInputField')
    SUBJECT = (By.CSS_SELECTOR, "input.subject")
    BODY = (By.CSS_SELECTOR, ".contentEditDiv")
    SEND_BTN = (By.CSS_SELECTOR, ".unselectable.btn.invertBtn.orientH.sendButton.wsIconButton")
    INBOX_MAIL = (By.CSS_SELECTOR, "#page-0 > div:nth-child(1)")
    INBOX_BTN = (By.CSS_SELECTOR, "#inboxNode")
    INBOX_SUBJECT = (By.CSS_SELECTOR, ".subject")
    # INBOX_BODY = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1][text()]")
    INBOX_BODY = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[3]/div/div/div[3]/div/div[2]/div/div/div[1]")
    SELECT_ALL_MSG = (By.XPATH, '/html/body/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[5]/div/div[1]/div/div/div/table/tbody/tr/th[1]')
    SELECT_FIRST_MSG = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]")
    DELETE_BTN = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[9]/div[1]")
    OK_BTN = (By.XPATH, "//div[contains(text(),'OK')]")
    # DELETE_BTN_IN_MAIL = (By.XPATH, "//body/div[@id='ws_application']/div[@id='ws_appScroll']/div[@id='appContent']/div[@id='ws_view']/div[3]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]")
    DELETE_BTN_IN_MAIL = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[3]/div/div/div[1]/div[1]/div[7]/div[1]")
    # DELETE_BTN_IN_MAIL = (By.ID, "uniqName_4_22")
    # DELIVERED_SUBJECT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/span[1]")
    DELIVERED_SUBJECT = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[4]/span[1]")
    DELIVERED_SUBJECT2 = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[4]/span[1]")
    DELIVERED_SUBJECT3 = (By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div/div/div[3]/table/tbody/tr/td[4]/span[1]")

    #dojox_grid_Grid_0 > div.dojoxGrid-master-header > div > div > div > table > tbody > tr > th.dojoxGrid-cell.gridColSel
    #page-0 > div:nth-child(1) > table > tbody > tr > td.dojoxGrid-cell.gridColSel
    #page-0 > div:nth-child(3) > table > tbody > tr > td.dojoxGrid-cell.gridColSel
    ROW = (By.CSS_SELECTOR, ".dojoxGrid-row")
    ROW_SUBJECT = (By.CSS_SELECTOR, ".gridColSub")
    ROW_SUBJECT_SPAN = (By.TAG_NAME, "span")
