# from selenium.webdriver import Chrome
# from time import sleep
# driver=Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# sleep(2)
# driver.get("https://www.")
# sleep(2)
# driver.find_element_by_id("SE_home_autocomplete").send_keys("python jobs")
# sleep(2)
# driver.find_element_by_xpath("//div[@class='col-xl-2 col-lg-3 col-sm-2 col-xxs-12 fl no-padding']").click()
# driver.close()
###############################################################################################################
#click ruby checkbox
# from selenium.webdriver import Chrome
# from time import sleep
# driver=Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
# sleep(2)
# driver.get(r"file:///D:/priya/selenium%20files/demo-html/demo.html")
# sleep(2)
# driver.find_element_by_xpath("//td[text()='Ruby']/..//input[@type='checkbox']").click()
# sleep(2)
###################################################################################################################
#checking all the checkbox using dynamic xpath
from selenium.webdriver import Chrome
from time import sleep
driver=Chrome(r"C:\Users\Anvitha\PycharmProjects\Python\selenium_files\chromedriver.exe")
sleep(2)
driver.get(r"file:///D:/priya/selenium%20files/demo-html/demo.html")
sleep(2)
l=["Ruby","Java","Perl","Python","C#","JavaScript"]
for item in l:
    xpath_=f"//td[text()='{item}']/..//input[@type='checkbox']"
    driver.find_element_by_xpath(xpath_).click()
    sleep(2)














d
