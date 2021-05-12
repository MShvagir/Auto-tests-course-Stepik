import unittest
from selenium import webdriver

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]


def fill_form(link, driver, person):
    driver.get(link)
    for key in person:
        driver.find_element_by_css_selector(f".form-control.{key}[required]").send_keys(person[key])
    driver.find_element_by_css_selector(".btn.btn-default").click()
    return driver.find_element_by_css_selector(".container").text


class TestWebElements(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.person = {
            'first': 'Tamara',
            'second': 'Stowns',
            'third': 'blabla@mail.ru'
        }

    def test_first_page(self):
        self.assertEqual(fill_form(links[0], self.driver, self.person),
                         "Congratulations! You have successfully registered!", "Fail")

    def test_second_page(self):
        self.assertEqual(fill_form(links[1], self.driver, self.person),
                         "Congratulations! You have successfully registered!", "Fail")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
