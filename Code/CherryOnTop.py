from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path = chromedriver,
                          chrome_options = chromeOptions )
url = 'https://www.youtube.com/watch?v=8aRor905cCw'
driver.get(url)