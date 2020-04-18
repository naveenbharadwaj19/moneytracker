from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


def json_pdf():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    "download.default_directory": "path\\json-pdf", #Download directory use \\ only 
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True })
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('headless')
    driver = webdriver.Chrome(executable_path= 'path/chromedriver',options= options)
    url = "https://pdfmall.com/json-to-pdf"
    driver.get(url)

    sleep(3)
    #upload the file
    print("Uploading the json file")
    try:
        driver.find_element_by_xpath('//*[@id="files"]').send_keys(os.path.abspath("path/trackmoney.json"))
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
