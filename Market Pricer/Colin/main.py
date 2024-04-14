
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver

with open("Output.txt", "w") as text_file:
    def targetFetch():
        text_file.write("Target:")
    # instantiate options
        options = webdriver.ChromeOptions()
#ask user what they would like to search
        query = input("what would you like from Target? ")
 # run browser in headless mode
        options.headless = True

# instantiate driver
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)

# load website
        url = 'https://www.target.com/s?searchTerm=' + query

# get the entire website content
        driver.get(url)
        time.sleep(3)
# initialize array containing product info
        product = []
#loop four times for first four products
        for i in range(1, 5):
                text_file.write("INSERT INTO ITEM VALUES (")
# grab name of product
                elements = driver.find_elements(By.XPATH, "//div/div[1]/div/div[4]/div/div/section/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/a")
                product_info = [element.text for element in elements]
                product.append(product_info)
                text_file.write(str(product_info))
#grab product price
                elements = driver.find_elements(By.XPATH, "//div/div[1]/div/div[4]/div/div/section/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/span[1]/span")
                product_info = [element.text for element in elements]
                product.append(product_info)
                text_file.write(str(product_info))
#grab product price per metric
                elements = driver.find_elements(By.XPATH, "//div/div[1]/div/div[4]/div/div/section/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/span[2]")
                product_info = [element.text for element in elements]
                product.append(product_info)
                text_file.write(str(product_info))
                print("INSERT INTO ITEM VALUES("+str(product)+");")
                product.clear()
                text_file.write(");\n")
    def walmartFetch():
        text_file.write("Walmart:")
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
    # instantiate options
        options = webdriver.ChromeOptions()
    # ask user what they would like to search
        query = input("what would you like from Walmart? ")
    # run browser in headless mode
        options.headless = True

    # instantiate driver
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver = undetected_chromedriver.Chrome()
    # load website
        url = 'https://www.walmart.com/search?q=' + query

    # get the entire website content
        driver.get(url)
        time.sleep(1)
    # initialize array containing product info
        product = []
    # loop four times for the first four products
        for i in range(1, 5):
    #grab product title
            elements = driver.find_elements(By.XPATH, "//section/div/div[" + str(i) + "]/div/div/div/div[2]/span/span")
            product_info = [element.text for element in elements]
            product.append(product_info)
            text_file.write(str(product_info))
    #grab product price
            elements = driver.find_elements(By.XPATH, "//section/div/div[" + str(i) + "]/div/div/div/div[2]/div[1]/div[1]")
            product_info = [element.text for element in elements]
            product.append(product_info)
            text_file.write(str(product_info))
    #grab product price per metric
            elements = driver.find_elements(By.XPATH, "//section/div/div[" + str(i) + "]/div/div/div/div[2]/div[1]/div[2]")
            product_info = [element.text for element in elements]
            product.append(product_info)
            text_file.write(str(product_info))
            print(product)
            product.clear()
            text_file.write("\n")
