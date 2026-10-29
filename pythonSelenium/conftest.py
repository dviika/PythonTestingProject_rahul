import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox"
    )


@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")  # Forces Firefox to run without a GUI
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit() #it will be executed after the test = test_e2eTestFramework.py is completed, to close the browser


@pytest.hookimpl (hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    html_plugin = item.config.pluginmanager.getplugin("html")
    driver = item.funcargs.get("browser_instance")
    if html_plugin is None or driver is None:
        return

    image = html_plugin.extras.image(driver.get_screenshot_as_base64())
    report.extras = getattr(report, "extras", [])
    report.extras.append(image)
    report.extras = getattr(report, "extras", [])
    report.extras.append(image)
