import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(params=['firefox', 'chrome', 'edge'])
# def multi_driver(request):
#     if request.param == 'firefox':
#         driver = webdriver.Firefox()
#     elif request.param == 'chrome':
#         driver = webdriver.Chrome()
#     elif request.param == 'edge':
#         driver = webdriver.Edge()
#     yield driver
#     driver.quit()

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    options.add_argument("--headless=new")
    options.add_argument("--log-level=3")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    driver.set_window_size(1920,1200)
    yield driver
    driver.quit()
