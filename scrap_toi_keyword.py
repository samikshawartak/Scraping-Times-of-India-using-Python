from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


def search():
    driver = webdriver.Chrome()

    driver.get('https://timesofindia.indiatimes.com/')

    driver.maximize_window()

    time.sleep(10)

    search = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/div/span')
    search.click()

    time.sleep(2)

    search_word = driver.find_element_by_xpath('//*[@id="query"]')
    search_word.send_keys('startups')

    time.sleep(2)

    search_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/div/div/form/input[2]')
    search_button.click()

    time.sleep(2)

    sort = driver.find_element_by_xpath('//*[@id="current-filter"]')
    sort.click()

    time.sleep(2)

    sort_click = driver.find_element_by_xpath('//*[@id="pastmonth"]')
    sort_click.click()

    time.sleep(2)

    return driver

def scrap(driver):

    soup = BeautifulSoup(driver.page_source, 'lxml')

    containers=soup.findAll("li",{"class":"article"})

    container=containers[0]

    for container in containers:

        content=container.find("div",{"class":"content"})

        title=content.find("span",{"class":"title"})
        date=content.find("span",{"class":"meta"})
        para=content.find("p")
        link=content.find("a")

        print(title.text+"\n"+date.text+"\n"+para.text+"\n"+link['href']+"\n")

        time.sleep(2)
        
    time.sleep(5)
    
    driver.quit()


scrap(search())
