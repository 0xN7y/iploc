from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup as B
import requests
import sys
import json
import random
import time



count = 1
for i in range(6):
    try:
        sys.argv[int(i)]
    except IndexError:
        break
    count = count + 1
count = count - 2

if count != 1:
    print("Usage : python3 ip2loc.py ip ")
    exit()

ip = sys.argv[1]

def ipformat(ip):
        try:
            if len(ip.split('.')) == 4:
                ind = ip.split('.')
                for i in ind:
                    if i.isnumeric():
                        pass
                    else:
                        return False
                return True
            else:
                return False
        except:
            return False

if ipformat(ip) == False:
    print("invalid ip format!")
    exit()


# ip = '196.190.249.229'




ipinf = requests.get("https://ipinfo.io/"+ip).text


ipinf = json.loads(ipinf)
for i in ipinf:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01,0.0353))
loc = ipinf["loc"]

print(ipinf)


exit()





#print(f"supplied argument = {count -2}")

query = loc
    

driver = webdriver.Firefox()

searchbox_id = 'searchboxinput'
searchbox_class = 'tactile-searchbox-input'
searchbox_xpath = '//*[@id="searchboxinput"]'
searchbox_name = 'q'

zoomIN_id = 'widget-zoom-in'
zoomIN_class = 'ujtHqf-zoom-LgbsSe widget-zoom-in'
zoomIN_xpath = '//*[@id="widget-zoom-in"]'


driver.get("https://www.google.com/maps/")
s = driver.find_element_by_name("q")
s.clear()
s.send_keys(query)
s.send_keys(Keys.RETURN)
sleep(3)

#zoom_button = driver.find_element_by_xpath(zoomIN_xpath).click()


loc  = driver.execute_script('window.location.href')
loc = driver.current_url

html = requests.get(loc)
soup = B(html.text, "html.parser")


info_class = 'x3AX1-LfntMc-header-title'
info = soup.findAll('div', {'class': info_class})
print(info)

if info_class in soup:
    print("we got em")
else:
    pass
    #print("we lost")

