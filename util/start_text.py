def startTest():
    from time import sleep
    from selenium import webdriver

    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    browser.get("https://www.typingtest.com/")
    startBTN = browser.find_element_by_xpath("//button[text()='Start test']")
    startBTN.click();