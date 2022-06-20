from homework_test.send_email import get_random_string
from .base_page import BasePage
from .locators import MailPageLocators
import time



class MailPage(BasePage):

    def get_random_string(self, length):
        random_string = self.string.ascii_lowercase + self.string.digits
        return ''.join(self.random.choice(random_string) for i in range(length))

    def try_click_element(self, selector, refresh = False):
        current_try = 0
        TRIES_MAXIMUM = 10
        while current_try < TRIES_MAXIMUM:
            try:
                # print('click try #', current_try)
                self.browser.find_element(*selector).click()
                return
            except Exception as e:
                # print('click error!', e)
                if refresh:
                    self.browser.refresh()
                else:
                    time.sleep(1)
                pass
            current_try += 1
        raise Exception("Click did not work :(")

    def load_inbox(self):
        print('load inbox')
        self.try_click_element(MailPageLocators.INBOX_BTN, True)

    def find_random_subject(self, random_subject):
        # print("find_random_subject --->", random_subject)
        timeStart = time.time()
        INBOX_WAIT_TIMEOUT_30_SEC = 30
        while time.time() - timeStart < INBOX_WAIT_TIMEOUT_30_SEC:
            self.load_inbox()
            for selector in (MailPageLocators.DELIVERED_SUBJECT, MailPageLocators.DELIVERED_SUBJECT2, MailPageLocators.DELIVERED_SUBJECT3):
                try:
                    subjectFound = self.browser.find_element(*selector).text
                    # print("subjectFound == random_subject", subjectFound, random_subject)
                    if subjectFound == random_subject:
                        return
                except Exception as e:
                    # print("error... :(", e)
                    pass
            time.sleep(1)

    def send_mail(self):
        time.sleep(3)
        self.random_subject = get_random_string(10)

        self.try_click_element(MailPageLocators.NEW_MAIL)
        time.sleep(1)
        self.input_email_receiver = self.browser.find_element(*MailPageLocators.EMAIL_RECEIVER).send_keys("testhookah@aol.com")

        subject = (self.random_subject)
        self.browser.find_element(*MailPageLocators.SUBJECT).send_keys(subject)

        random_body = get_random_string(10)
        body = (random_body)
        self.browser.find_element(*MailPageLocators.BODY).send_keys(body)
        self.try_click_element(MailPageLocators.SEND_BTN)

        print("Mail number:", self.count, "- sent")
        time.sleep(3)

    def try_to_find_deliverd_message(self):
        self.load_inbox()
        self.find_random_subject(self.random_subject)
        print("Mail number: ", self.count, "- found")

    def find_subject_inbox(self, subject):
        rows = self.browser.find_elements(*MailPageLocators.ROW);
        # print("rows", len(rows))
        if len(rows) == 0:
            raise Exception("Zero rows :(")

        for row_element in rows:
            subject_element = row_element.find_element(*MailPageLocators.ROW_SUBJECT)
            span_elements = subject_element.find_elements(*MailPageLocators.ROW_SUBJECT_SPAN)
            row_subject = span_elements[0].text
            row_body = span_elements[1].text
            # print("row ->", row_subject, ", row_body", row_body)
            if subject == row_subject:
                subject_element.click()
                return [row_subject, row_body]

    def read_mail(self):
        # read mail
        self.load_inbox()
        self.dict = {}
        time.sleep(1)
        # find_subject = self.browser.find_element(*MailPageLocators.INBOX_SUBJECT).text
        # self.dict[find_subject] = self.browser.find_element(*MailPageLocators.INBOX_BODY).text

        [subject, body] = self.find_subject_inbox(self.random_subject)
        self.dict[subject] = body
        # print("dict --> ", self.dict)

        # delete read mail
        self.try_click_element(MailPageLocators.DELETE_BTN_IN_MAIL)
        print("Mail number:", self.count, "- read")

    def send_new_mail(self):
        # send_new_mail
        self.try_click_element(MailPageLocators.NEW_MAIL)
        self.browser.find_element(*MailPageLocators.EMAIL_RECEIVER).send_keys("testhookah@aol.com")

        for keys, values in self.dict.items():
            new_dict = {'Letters': 0, 'Numbers': 0}
            for value in self.dict.values():
                for i in value:
                    if i.isalpha():
                        new_dict['Letters'] += 1
                    elif i.isdigit():
                        new_dict['Numbers'] += 1

            self.new_random_subject = get_random_string(10)
            self.browser.find_element(*MailPageLocators.SUBJECT).send_keys(self.new_random_subject)
            self.browser.find_element(*MailPageLocators.BODY).send_keys(
                f'Received mail on theme {keys} with message: {values}. It contains {new_dict["Letters"]} letters and {new_dict["Numbers"]} numbers')
            self.try_click_element(MailPageLocators.SEND_BTN)
            time.sleep(2)
    
    def re_check_deliver_mail(self):
        # re-check deliver mail
        self.load_inbox()
        self.find_random_subject(self.new_random_subject)
        print(self.count, "new mail(s) sent")
        print('Task number:', self.count, '- complete')

    def delete_all_messages(self):
        self.load_inbox()
        time.sleep(1)
        self.try_click_element(MailPageLocators.SELECT_ALL_MSG)
        self.try_click_element(MailPageLocators.SELECT_FIRST_MSG)
        self.try_click_element(MailPageLocators.DELETE_BTN)

    def prepare_test(self):
        self.count = 1

    def finalize_test_round(self):
        print(self.count, " round is finished")
        self.count += 1



    
