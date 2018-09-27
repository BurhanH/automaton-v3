from selenium import webdriver


class TestBrowserResolution:
    """
    This test suite for browser resolution testing.
    """
    @staticmethod
    def _set_and_verify(set_width, set_height):
            """
            Common static method to initiate browser, set browser resolution, and verify it.
            :param set_width:
            :param set_height:
            """
            driver = webdriver.Firefox()
            driver.set_window_size(set_width, set_height)
            resolution = driver.get_window_size()
            width = resolution.get('width')
            height = resolution.get('height')

            errors = []

            if width != set_width:
                errors.append(u'Width is {} expecting {}'.format(width, set_width))
            if height != set_height:
                errors.append(u'Height is {} expecting {}'.format(height, set_height))

            error_msgs = '\n'.join(errors)

            driver.close()

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
