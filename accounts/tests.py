import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import Client
from accounts.models import Account


class B1_Testing(StaticLiveServerTestCase):

    fixtures = ['b1_testing.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_register(self):
        path = self.live_server_url
        pathStart = path + '/accounts/register'
        pathEnd = path + '/accounts/logout'
        client = Client()

        test_email = 'johnny@appleseed.com'
        test_username = 'Jonnhy_Appleseed'
        test_dob = '12-07-2020'
        test_password = 'Ireallylikeapples23!'

        # testing register get page request and verifying
        register_page = self.client.get('/accounts/register')
        self.assertContains(register_page,'csrfmiddlewaretoken')
        self.assertEqual(register_page.status_code, 200)

        # simulating register
        register_body = register_page.content.decode('utf-8')

        self.selenium.get(pathStart)
        input_form = self.selenium.find_element_by_name('csrfmiddlewaretoken')
        token = input_form.get_attribute("value")
        register = { 'csrfmiddlewaretoken' : token,
        'email' : test_email,
        'username' : test_username,
        'dob' : test_dob,
        'password1' : test_password,
        'password2' : test_password,
        }
        register_post = self.client.post('/accounts/register', register)
        self.assertEqual(register_post.status_code, 200)
        self.selenium.get(pathEnd)

        # end to end testing of register feature
        self.selenium.get(pathStart)
        email_input = self.selenium.find_element_by_name('email')
        username_input = self.selenium.find_element_by_name('username')
        dob_input = self.selenium.find_element_by_name('dob')
        password1_input = self.selenium.find_element_by_name('password1')
        password2_input = self.selenium.find_element_by_name('password2')
        register_button = self.selenium.find_element_by_id('register_button')

        email_input.send_keys(test_email)
        time.sleep(1)
        username_input.send_keys(test_username)
        time.sleep(1)
        dob_input.send_keys(test_dob)
        time.sleep(1)
        password1_input.send_keys(test_password)
        time.sleep(1)
        password2_input.send_keys(test_password)
        time.sleep(2)

        register_button.click()
        time.sleep(2)
        self.selenium.get(pathEnd)
        time.sleep(2)

    def test_login(self):
        path = self.live_server_url
        pathStart = path + '/accounts/login'
        pathEnd = path + '/accounts/logout'

        client = Client()

        login_email = 'tester@test.com'
        login_pass = 'Thetester123'

        # testing login get page request and verifying
        login_page = self.client.get('/accounts/login')
        self.assertContains(login_page,'csrfmiddlewaretoken')
        self.assertEqual(login_page.status_code, 200)

        # simulating login
        login_body = login_page.content.decode('utf-8')

        self.selenium.get(pathStart)
        input_form = self.selenium.find_element_by_name('csrfmiddlewaretoken')
        token = input_form.get_attribute("value")
        login = { 'csrfmiddlewaretoken' : token,
        'email' : login_email,
        'password' : login_pass,
        }
        login_post = self.client.post('/accounts/login', login)
        self.assertEqual(login_post.status_code, 302)
        self.selenium.get(pathEnd)

        # end to end testing of login feature
        self.selenium.get(pathStart)
        email_input = self.selenium.find_element_by_name('email')
        password_input = self.selenium.find_element_by_name('password')
        login_button = self.selenium.find_element_by_id('login_button')

        email_input.send_keys(login_email)
        time.sleep(1)
        password_input.send_keys(login_pass)
        time.sleep(2)

        login_button.click()
        time.sleep(2)
        self.selenium.get(pathEnd)
        time.sleep(2)
