"""
Environment for Behave Testing
"""

from selenium import webdriver

WAIT_SECONDS = 10
BASE_URL = "http://localhost:8501"


def before_all(context):
    """Executed once before all tests"""
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS

    context.driver = get_chrome()
    context.driver.implicitly_wait(context.wait_seconds)
    context.config.setup_logging()


def after_all(context):
    """Executed after all tests"""
    context.driver.quit()
    print("Driver closed successfully.")


######################################################################
# Utility functions to create web drivers
######################################################################


def get_chrome():
    """Creates a headless Chromium driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")

    # Specify the Chromium binary location explicitly
    options.binary_location = "/usr/bin/chromium-browser"

    return webdriver.Chrome(options=options)
