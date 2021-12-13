from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class Sam:

    def __init__(self):
        self.s = Service("C:\\Users\\ustjavasdetb418\\Downloads\\chromedriver_win32\\chromedriver.exe")
        browser = webdriver.Chrome(service=self.s)
        url = 'https://www.urbanladder.com/'
        print("Accessing Website of Urbanladder")
        browser.get(url)
        browser.maximize_window()
        print("Maximizing the window of urbanladder")
        browser.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/ul/li[4]/span").click()
        time.sleep(1)
        print("Clicked Dining module session")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/header/div[2]/div/nav/div/ul/li[4]/div/div/ul/li[1]/ul/li[1]/a/span").click()
        time.sleep(1)
        print("Clicked Dining Tables")
        browser.get("https://www.urbanladder.com/dining-tables?src=g_topnav_dining_dining-tables-sets_dining-tables")
        time.sleep(5)
        print("Accessing Dining Tables Sets in urbanladder")
        browser.find_element(By.XPATH, "/html/body/div[7]/div/div[1]/div/div[2]/a[1]").click()
        time.sleep(5)
        print("Checking radiobutton by Excluding Out of Stock")
        browser.find_element(By.XPATH,
                             "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[2]/div/input").click()
        time.sleep(1)
        print("Removing Pop-Up")
        browser.find_element(By.XPATH,
                             "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li/div[1]/div").click()
        time.sleep(2)
        print("Click the price filter button")
        browser.find_element(By.XPATH,
                             "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li/div[2]/div/div/ul/li[2]/div[1]/label/input").click()
        time.sleep(2)
        print("Price filtering from 4199-49055")
        browser.find_element(By.XPATH,
                             "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li/div[1]/div").click()
        time.sleep(2)
        print("Price filtering")
        browser.find_element(By.XPATH,
                             "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li/div[2]/div/div/ul/li[2]/div[1]/label/input").click()
        time.sleep(2)
        browser.get("https://www.urbanladder.com/products/arabia-6-seater-dining-table?sku=FNTBDI11TK10001&src=room")
        time.sleep(5)
        print("Accessing page of Arabian 6- Seater dining table")
        browser.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/section[1]/a/figure").click()
        time.sleep(3)
        print("Back to homepage of urbanladder")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/header/div[1]/div/section[2]/div/form/div/span/input[2]").send_keys(
            "Dining Chair")
        time.sleep(2)
        print("Searching Dining Chair")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/header/div[1]/div/section[2]/div/form/div/button/span").click()
        time.sleep(2)
        browser.get("https://www.urbanladder.com/products/doris-dining-chairs-set-of-2?sku=FNCOMB90BL10895&src=subcat")
        time.sleep(5)
        print("Accessing webpage of particular product")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[2]/div[3]/div[3]/div[3]/div[1]/div[2]/div[1]/div[10]/form/div/div[2]/div[1]/div[3]/button").click()
        print("Clicked Add to cart")
        browser.find_element(By.ID, "checkout-link").click()
        print("Clicked checkout")

        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[1]/fieldset/ul/li[1]/div/div/input").send_keys(
            "helnaeldho5@gmail.com")
        print("Passing Email Id")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[1]/fieldset/ul/li[2]/div/input").send_keys(
            "683556")
        print("Passing Pincode")
        time.sleep(3)
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[1]/fieldset/ul/li[7]/div/textarea").send_keys(
            "ABC")
        print("Passing Address")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[1]/fieldset/ul/li[8]/div/input").send_keys(
            "Harry")
        print("Passing First Name")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[1]/fieldset/ul/li[9]/div/input").send_keys(
            "Ron")
        print("Passing Lastname")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[1]/fieldset/ul/li[10]/div/div/input").send_keys(
            "9876543210")
        print("Passing Mobno")
        browser.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/input").send_keys(
            "xyz")
        print("Passing code")
        browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/form/div[2]/input").click()

        browser.close()


ob1 = Sam()
