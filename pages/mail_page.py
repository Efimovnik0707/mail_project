from homework_test.send_email import get_random_string
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MailPageLocators
import time



class MailPage(BasePage):

    def send_mail(self, n):
        self.count = 1

        for mail in range(n):
            self.subject = get_random_string(10)
            self.body = get_random_string(10)
            self.new_mail = self.browser.find_element(
                *MailPageLocators.NEW_MAIL)
            self.new_mail.click()
            self.email_receiver = "testhookah@aol.com"
            self.input_email_receiver = self.browser.find_element(
                *MailPageLocators.EMAIL_RECEIVER)
            self.input_email_receiver.send_keys(self.email_receiver)
            self.subject = (self.subject)
            self.input_subject = self.browser.find_element(
                *MailPageLocators.SUBJECT)
            self.input_subject.send_keys(self.subject)
            time.sleep(5)
            self.body = (self.body)
            self.input_body = self.browser.find_element(*MailPageLocators.BODY)
            self.input_body.send_keys(self.body)
            self.button = self.browser.find_element(*MailPageLocators.SEND_BTN)
            self.button.click()
            time.sleep(2)
            print(self.count, "mail(s) sended")
            self.count += 1
        print("All messages sended")
        print('Func send has already done')

    def get_random_string(self, length):
        self.random_string = self.string.ascii_lowercase + self.string.digits
        self.result_str = ''.join(self.random.choice(
            self.random_string) for i in range(length))

        return self.result_str

    def read_mail(self):
        self.new_mail = self.browser.find_element(*MailPageLocators.INBOX_BTN)
        self.new_mail.click()
        self.new_mail = self.browser.find_element(*MailPageLocators.INBOX_MAIL)
        self.new_mail.click()
        self.dict = {}
        time.sleep(1)
        self.find_subject = self.browser.find_element(
            *MailPageLocators.INBOX_SUBJECT)
        self.new_subject = self.find_subject.text
        self.find_body = self.browser.find_element(
            *MailPageLocators.INBOX_BODY)
        self.text = self.find_body.text
        self.dict[self.new_subject] = self.text
        print(self.dict)
        return self.dict

    def delete_mail(self):
        self.new_mail = self.browser.find_element(*MailPageLocators.INBOX_BTN)
        self.new_mail.click()
        self.select_all = self.browser.find_element(
            *MailPageLocators.SELECT_ALL_MSG)
        self.select_all.click()
        self.delete_mail = self.browser.find_element(
            *MailPageLocators.DELETE_BTN)
        self.delete_mail.click()
        # self.okey_btn = self.browser.find_element(*MailPageLocators.OK_BTN)
        # self.okey_btn.click()

    def run_mail(self, n):
        self.count = 1

        for mail in range(n):
            # send_mail
            time.sleep(3)
            self.random_subject = get_random_string(10)
            self.random_body = get_random_string(10)
            self.new_mail = self.browser.find_element(
                *MailPageLocators.NEW_MAIL)
            self.new_mail.click()
            time.sleep(1)
            self.email_receiver = "testhookah@aol.com"
            self.input_email_receiver = self.browser.find_element(
                *MailPageLocators.EMAIL_RECEIVER)
            self.input_email_receiver.send_keys(self.email_receiver)
            self.subject = (self.random_subject)
            self.input_subject = self.browser.find_element(
                *MailPageLocators.SUBJECT)
            self.input_subject.send_keys(self.subject)
            self.body = (self.random_body)
            self.input_body = self.browser.find_element(*MailPageLocators.BODY)
            self.input_body.send_keys(self.body)
            self.button = self.browser.find_element(*MailPageLocators.SEND_BTN)
            self.button.click()
            print("Mail number:", self.count, "- sended")
            time.sleep(3)

            # try to find deliverd message
            self.new_mail = self.browser.find_element(
                *MailPageLocators.INBOX_BTN)
            self.new_mail.click()
            self.deliver_subject = ''
            print(self.deliver_subject)
            found = False
            while not found:
                for selector in (MailPageLocators.DELIVERED_SUBJECT, MailPageLocators.DELIVERED_SUBJECT2, MailPageLocators.DELIVERED_SUBJECT3):
                    try:
                        self.var = self.browser.find_element(*selector).text
                        if self.var != self.random_subject:
                            self.new_mail = self.browser.find_element(
                                *MailPageLocators.INBOX_BTN)  #
                            self.new_mail.click()
                            print('Refresh page')
                            print('Try to find sended mail in inbox')

                        found = True
                    except:
                        pass

            print("Mail number: ", self.count, "- finded")

            # read_mail
            self.new_mail = self.browser.find_element(
                *MailPageLocators.INBOX_BTN)
            self.new_mail.click()
            self.new_mail = self.browser.find_element(
                *MailPageLocators.INBOX_MAIL)
            self.new_mail.click()
            self.dict = {}
            time.sleep(1)
            self.find_subject = self.browser.find_element(
                *MailPageLocators.INBOX_SUBJECT)
            self.new_subject = self.find_subject.text
            self.find_body = self.browser.find_element(
                *MailPageLocators.INBOX_BODY)
            self.text = self.find_body.text
            self.dict[self.new_subject] = self.text
            # delete_readed_mail
            self.delete_btn = self.browser.find_element(
                *MailPageLocators.DELETE_BTN_IN_MAIL)
            self.delete_btn.click()
            print("Mail number:", self.count, "- read")

            # send_new_mail
            self.new_mail = self.browser.find_element(
                *MailPageLocators.NEW_MAIL)
            self.new_mail.click()
            self.email_receiver = "testhookah@aol.com"
            self.input_email_receiver = self.browser.find_element(
                *MailPageLocators.EMAIL_RECEIVER)
            self.input_email_receiver.send_keys(self.email_receiver)

            for keys, values in self.dict.items():
                new_dict = {'Letters': 0, 'Numbers': 0}
                for value in self.dict.values():
                    for i in value:
                        if i.isalpha():
                            new_dict['Letters'] += 1
                        elif i.isdigit():
                            new_dict['Numbers'] += 1

                self.new_random_subject = get_random_string(10)
                self.input_subject = self.browser.find_element(
                    *MailPageLocators.SUBJECT)
                self.input_subject.send_keys(self.new_random_subject)
                self.input_body = self.browser.find_element(
                    *MailPageLocators.BODY)
                self.input_body.send_keys(
                    f'Received mail on theme {keys} with message: {values}. It contains {new_dict["Letters"]} letters and {new_dict["Numbers"]} numbers')
                self.button = self.browser.find_element(
                    *MailPageLocators.SEND_BTN)
                self.button.click()
                time.sleep(2)

            # re-check deliver mail
            self.new_mail = self.browser.find_element(
                *MailPageLocators.INBOX_BTN)
            self.new_mail.click()
            self.new_deliver_subject = ''
            print(self.new_deliver_subject)

            new_found = False
            while not new_found:
                for selector in (MailPageLocators.DELIVERED_SUBJECT, MailPageLocators.DELIVERED_SUBJECT2, MailPageLocators.DELIVERED_SUBJECT3):
                    try:
                        self.new_var = self.browser.find_element(
                            *selector).text
                        if self.new_var != self.new_random_subject:
                            self.new_mail = self.browser.find_element(
                                *MailPageLocators.INBOX_BTN)  
                            self.new_mail.click()
                            print('Refresh page')
                            print('Try to find new sended mail in inbox')

                        new_found = True
                    except:
                        pass
            print(self.count, "new mail(s) sended")
            print('Task number:', self.count, '- complete')

            self.count += 1

        # delete_all_messages
        self.new_mail = self.browser.find_element(*MailPageLocators.INBOX_BTN)
        self.new_mail.click()
        time.sleep(1)
        self.select_all = self.browser.find_element(
            *MailPageLocators.SELECT_ALL_MSG)
        self.select_all.click()
        self.select_first_msg = self.browser.find_element(
            *MailPageLocators.SELECT_FIRST_MSG)
        self.select_first_msg.click()
        self.delete_mail = self.browser.find_element(
            *MailPageLocators.DELETE_BTN)
        self.delete_mail.click()
        print('Func has done')

    
