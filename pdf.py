from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


def json_pdf():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    "download.default_directory": "D:\\OTHER FILES D\\CS ALL FOLD\\Python own projects\\trackmoney v 2.0\\json-pdf", #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True }) #It will not show PDF directly in chrome
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('headless')
    driver = webdriver.Chrome(executable_path= 'C:/Program Files (x86)/Google/Chrome/Application/chrome driver/chromedriver',options= options)
    url = "https://pdfmall.com/json-to-pdf"
    driver.get(url)

    sleep(3)
    #upload the file
    print("Uploading the json file")
    try:
        driver.find_element_by_xpath('//*[@id="files"]').send_keys(os.path.abspath("D:/OTHER FILES D/CS ALL FOLD/Python own projects/trackmoney v 2.0/trackmoney.json"))
    except Exception:
        print("Json does not exist make one!")
        driver.close()
        exit()
    driver.find_element_by_xpath('//*[@id="convertButton"]').click()
    print("Converting the json file to PDF")
    sleep(12)
    try:
        driver.find_element_by_xpath('//*[@id="iconConvertLinkDown"]').click()
        print("Opening the pdf file")
    except Exception:
        print("Something went wrong!")
        exit()


    sleep(2)
    print("Downloaded pdf file to json-pdf folder")
    driver.close()
