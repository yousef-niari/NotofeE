from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.sanarate.ir/")
time.sleep(5)
#pdate = browser.find_element_by_xpath('//*[@id="MainContent_ViewCashChequeRates_persianDate"]')
edate = browser.find_element_by_xpath('//*[@id="MainContent_ViewCashChequeRates_divEnglishDate"]')
day_price = browser.find_element_by_xpath('//*[@id="MainContent_ViewCashChequeRates_divTimely"]/div[2]/table')
print(day_price.text)
#print(pdate.text)
print(edate.text)

#browser.maximize_window()
#browser.quit()