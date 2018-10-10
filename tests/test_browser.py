from contextlib import contextmanager
from selenium import webdriver

WAIT_IMPL = 10
WINDOW_SIZE = 1280, 1024
BROWSER = 'firefox'


class TestBrowser:
    """
    This test suite for browser testing.
    """
    @contextmanager
    def make_driver(self):
        """
        Method to initiate driver.
        """
        if BROWSER == 'chrome':
            self.driver = webdriver.Chrome()
        if BROWSER == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(WAIT_IMPL)
        self.driver.set_window_size(WINDOW_SIZE[0], WINDOW_SIZE[1])
        try:
            yield
        finally:
            self.driver.close()

    def _set_and_verify(self, set_width, set_height):
            """
            Common method to set browser resolution, and verify it.
            :param set_width:
            :param set_height:
            """
            with self.make_driver():
                self.driver.set_window_size(set_width, set_height)
                resolution = self.driver.get_window_size()
                width = resolution.get('width')
                height = resolution.get('height')

                errors = []

                if width != set_width:
                    errors.append(u'Width is {} expecting {}'.format(width, set_width))
                if height != set_height:
                    errors.append(u'Height is {} expecting {}'.format(height, set_height))

                error_msgs = '\n'.join(errors)

                if errors:
                    raise AssertionError(error_msgs)

    def test_resolution_1(self):
        """
        Testing resolution 800, 600
        """
        self._set_and_verify(800, 600)

    def test_resolution_2(self):
        """
        Testing resolution 1280, 1024
        """
        self._set_and_verify(1280, 1024)

    def test_resolution_3(self):
        """
        Testing resolution 1600, 1200
        """
        self._set_and_verify(1600, 1200)

    def test_resolution_4(self):
        """
        Testing resolution 1680, 1050
        """
        self._set_and_verify(1680, 1050)

    def test_resolution_5(self):
        """
        Testing resolution 1900, 1200
        """
        self._set_and_verify(1900, 1200)

    def test_search_in_google(self):
        """
        Testing search in Google
        """
        with self.make_driver():
            # Going to google.com
            self.driver.get('https://www.google.com')
            # Searching for the input field by name and entering data
            self.driver.find_element_by_name('q').send_keys('python')
            # FIXME workaround, probably the reason is search drop-down menu
            import time
            time.sleep(2)
            # Clicking Google Search button
            self.driver.find_element_by_css_selector("input[name='btnK']").click()
            # Verifying search results
            if not self.driver.find_element_by_class_name('bNg8Rb').is_displayed():
                raise AssertionError("Unable to find results on a page!")
