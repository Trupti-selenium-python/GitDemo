from selenium import webdriver
import time
print("starting line in develop branch.............")
driver=webdriver.Chrome("C:\\Users\\Sakhamuri\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_name('q').send_keys("wipro")
time.sleep(5)
all_Results=driver.find_elements_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li/div/div[2]")
for Result in all_Results:
    req_Result=Result.text
    if req_Result=="wipro ceo":
        Result.click()
        break

print("Added a new line in gitX----------------")
print("added from GitX in develop branch.............")
