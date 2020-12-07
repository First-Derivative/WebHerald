import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import Client
from accounts.models import Account


class B1_Testing(StaticLiveServerTestCase):

    fixtures = ['b2_b3_testing.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_comments(self):
        path = self.live_server_url
        pathLogin = path + '/accounts/login'
        pathArticle = path + '/article/1#comments_section'

        login_email = 'tester@test.com'
        login_pass = 'Thetester123'

        comment_0 = "This my first new comment"
        comment_1 = "What an interesting article, really would like to see more of this."

        client = Client()

        # end to end testing of posting a two new comments and deleting the first one
        self.selenium.get(pathLogin)
        email_input = self.selenium.find_element_by_name('email')
        password_input = self.selenium.find_element_by_name('password')
        login_button = self.selenium.find_element_by_id('login_button')

        email_input.send_keys(login_email)
        time.sleep(1)
        password_input.send_keys(login_pass)
        time.sleep(1)
        login_button.click()
        time.sleep(2)

        self.selenium.get(pathArticle)

        new_comment_field = self.selenium.find_element_by_id('new_comment_content')
        new_comment_submit = self.selenium.find_element_by_id('new_comment_submit')

        # posting first comment
        new_comment_field.send_keys(comment_0)
        time.sleep(1)
        new_comment_submit.click()
        self.selenium.execute_script("window.scrollTo(0, 10000);")

        time.sleep(2)

        # posting second comment
        new_comment_field.send_keys(comment_1)
        time.sleep(1)
        new_comment_submit.click()
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # verifying newly posted comment content
        new_comment_0 = self.selenium.find_elements_by_class_name('comment_content')[0]
        new_comment_1 = self.selenium.find_elements_by_class_name('comment_content')[1]

        new_comment_0_content = new_comment_0.text
        new_comment_1_content = new_comment_1.text

        self.assertEqual(new_comment_0_content, comment_0)
        self.assertEqual(new_comment_1_content, comment_1)

        time.sleep(3)

        delete_first_comment_button = self.selenium.find_elements_by_class_name('target')[1]
        delete_first_comment_button.click()

        time.sleep(3)

    def test_likes(self):
        path = self.live_server_url
        pathLogin = path + '/accounts/login'
        pathArticle = path + '/article/4'

        login_email = 'tester@test.com'
        login_pass = 'Thetester123'

        client = Client()

        # end to end testing of liking an article
        self.selenium.get(pathLogin)
        email_input = self.selenium.find_element_by_name('email')
        password_input = self.selenium.find_element_by_name('password')
        login_button = self.selenium.find_element_by_id('login_button')

        email_input.send_keys(login_email)
        time.sleep(1)
        password_input.send_keys(login_pass)
        time.sleep(1)
        login_button.click()
        time.sleep(2)

        self.selenium.get(pathArticle)

        like_button = self.selenium.find_element_by_class_name('like-button')

        #liking article
        like_button.click()
        time.sleep(2)

        #verifying article like count increment
        like_count_wrapper = self.selenium.find_element_by_class_name('display_numlikes')
        like_count = like_count_wrapper.text
        self.assertEqual(like_count, '2')

        #unliking article
        like_button.click()
        time.sleep(2)

        #verifying article like count decrement
        like_count_wrapper = self.selenium.find_element_by_class_name('display_numlikes')
        like_count = like_count_wrapper.text
        self.assertEqual(like_count, '1')
