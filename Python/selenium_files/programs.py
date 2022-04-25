#fetch product name and corresponding prices
# from selenium.webdriver import Chrome
# from time import sleep
# import re
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
# p_name=driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")
# p_price=driver.find_elements_by_xpath("//span[@class='art-price' or @calss='art-price art-price--offer']")
# name =[]
# for p_text in p_name:
#     name.append(p_text.text)
# price=[]
# for p_text in p_price:
#     price.append(float("".join(re.findall(r"[\d\.]",p_text.text))))
# print(name)
# print(price)
# with open("priya.csv","w"):
#     for name1,price1 in zip(name,price):
#         print(name1,price1)
#################################################################################################################
#fetch dynamic text
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("D:/priya/selenium%20files/demo-html/demo.html")
# sleep(2)
# l=["AAPL","MSFT","AA","FB"]
# while True:
#     for item in l:
#         ele = driver.find_element_by_xpath(f"//td[text()='{item}']/..//td[@class='price']").text
#         print(ele,end="\t\t")
#         sleep(3)
#     print()
##############################################################################################################
#window popup pgm1:ok
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("file:///D:/priya/selenium%20files/demo-html/demo.html")
# sleep(3)
# driver.find_element_by_id("delete").click()
# sleep(2)
# driver.switch_to.alert.accept()
# sleep(2)
# driver.close()
#################################################################################################
#window popup pgm2:cancel
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("file:///D:/priya/selenium%20files/demo-html/demo.html")
# sleep(3)
# driver.find_element_by_id("delete").click()
# sleep(2)
# driver.switch_to.alert.dismiss()
# sleep(2)
################################################################################################
#window popup pgm3:text
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("file:///D:/priya/selenium%20files/demo-html/demo.html")
# sleep(3)
# driver.find_element_by_id("delete").click()
# sleep(2)
# print(driver.switch_to.alert.text)
# sleep(2)
#######################################################################################
#hidden division
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://www.goibibo.com/")
# sleep(3)
# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)
# for _ in range(12):
#     try:
#         driver.find_element_by_xpath("//div[text()='September 2022']/../..//p[text()='30']").click()
#     except NoSuchElementException:
#         driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
#         sleep(2)
#########################################################################################################
##fetch product name and corresponding prices in to the csv file
# import csv
# from selenium.webdriver import Chrome
# from time import sleep
# import re
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
# p_name=driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")
# p_price=driver.find_elements_by_xpath("//span[@class='art-price' or @calss='art-price art-price--offer']")
# name =[]
# for p_text in p_name:
#     name.append(p_text.text)
# price=[]
# for p_text in p_price:
#     price.append(float("".join(re.findall(r"[\d\.]",p_text.text))))
# print(name)
# print(price)
# with open("priya.csv","w") as file:
#     l=[]
#     obj  = csv.writer(file)
#     for name1,price1 in zip(name,price):
#         l.append([name1,price1])
#     obj.writerow(l)
    ##############################################################################################
#fetch product name and corresponding prices less than 100
# from selenium.webdriver import Chrome
# from time import sleep
# import re
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
# p_name=driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")
# p_price=driver.find_elements_by_xpath("//span[@class='art-price' or @calss='art-price art-price--offer']")
# name =[]
# for p_text in p_name:
#     name.append(p_text.text)
# price=[]
# for p_text in p_price:
#     price.append(float("".join(re.findall(r"[\d\.]",p_text.text))))
# print(name)
# print(price)
# for name1,price1 in zip(name,price):
#     if price1<100:
#         print(name1,price1)
###########################################################################################
# description of the product
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://www.ajio.com/")
# sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("shoes")
# sleep(5)
# driver.find_element_by_xpath("//span[@class='ic-search']").click()
# sleep(5)
# ele=driver.find_elements_by_xpath("//div[@class='imgHolder']/..//div[@class='contentHolder']")
# for item in ele:
#     print(item.text)
#     sleep(2)
###########################################################################################
# price of the product
# import re
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://www.ajio.com/")
# sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("shoes")
# sleep(5)
# driver.find_element_by_xpath("//span[@class='ic-search']").click()
# sleep(5)
# ele=driver.find_elements_by_xpath("//div[@class='nameCls']/..//span[@class='price  ']")
# l= []
# for item in ele:
#     res =(int("".join(re.findall(r"\d",item.text))))
#     if res < 3000:
#         print(res)
#         sleep(2)
##########################################################################################
# import csv
# import re
# from selenium.webdriver import Chrome
# from time import sleep
#
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver=Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://www.myntra.com/")
# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("dress")
# sleep(2)
# driver.find_element_by_xpath("//span[@class='myntraweb-sprite desktop-iconSearch sprites-search']").click()
# price=driver.find_elements_by_xpath("//h3[@class='product-brand']/..//span[@class='product-discountedPrice']")
# sleep(2)
# product = driver.find_elements_by_xpath("//h3[@class='product-brand']")
# sleep(2)
# #print on the console
# # for price_t in price:
# #     res=int("".join(re.findall(r"\d",price_t.text)))
# #     if res < 1000:
# #         print(res)
# #         sleep(0.3)
# # for product_t in product:
# #     print(product_t.text)
# #     sleep(2)
# #print in the file product corresponding price in the list
# # l=[]
# # for price_t in price:
# #     l.append(int("".join(re.findall(r"\d",price_t.text))))
# # l1=[]
# # for product_t in product:
# #     l1.append(product_t.text)
# #
# # for i1,i2 in zip(l1,l):
# #     print(i1,i2)
# #print in the file product corresponding price in the dict
#
# d={}
# l=[]
# for price_t in price:
#     l.append(int("".join(re.findall(r"\d",price_t.text))))
# l1=[]
# for product_t in product:
#     l1.append(product_t.text)
# for i in range(len(l1)):
#     d[l1[i]] = l[i]
# print(d)
# #print in the file
#
# with open("honey.csv","w")as file:
#     res=[]
#     o=csv.writer(file)
#     for i1, i2 in zip(l1, l):
#         res.append([i1,i2])
#     o.writerows(res)
####################################################################################################
from selenium.webdriver import Chrome
from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("https://www.myntra.com/")
# sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("dress")
# sleep(2)
# def enter_text(loctype,locvalue,value):
#     driver.find_element(loctype,locvalue).send_keys("value")
#
# def click_ele(loctype,locvalue):
#     driver.find_element(loctype, locvalue).click()
##################################################################

# def enter_text(locator,*, value):
#     loctype,locvalue=locator
#     driver.find_element(loctype, locvalue).send_keys("value")
#
# def click_ele(locator):
#     driver.find_element(*locator).click()
###############################################################
from selenium.webdriver import Chrome
from time import sleep

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from selenium.webdriver.support.wait import WebDriverWait

driver=Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
driver.get("https://www.myntra.com/")
# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("dress")
# sleep(2)
class child(visibility_of_element_located):
    def __call__(self,driver):
        res = super().__call__(driver)
        #checking if __call__ has returned webele
        if isinstance(res,WebElement):
            return res.is_enabled()
        return res

def wait(func):
    def wrapper(*args,**kwargs):
        locator=args[0]
        #wait for 3 cond
        wait=WebDriverWait(driver,5)
        v=child(locator)
        wait.until(v)
        return func(*args,**kwargs)
    return wrapper
@wait
def enter_text(locator,*, value):
    loctype,locvalue=locator
    driver.find_element(loctype, locvalue).send_keys("value")
@wait
def click_ele(locator):
    driver.find_element(*locator).click()


enter_text(("Xpath", "//input[@placeholder='Search for products, brands and more']"),value="dress")
click_ele(("xpath","//span[@class='myntraweb-sprite desktop-iconSearch sprites-search']"))
#################################################################################################
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# driver.get("file:///D:/priya/selenium%20files/demo-html/demo.html")
# ele=driver.find_elements_by_xpath("//table[@name='customers']//td[2]")
# names=[item.text for item in ele ]
# if names==sorted(names):
#     print("true")
# else:
#     print("false")
# print(names)
# print(sorted(names))
###################################################################################################

