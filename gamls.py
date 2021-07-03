import pprint
import time
import sqlite3
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType

'''headers = {
    'Referer': 'https://www.gamls.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
payload = 'username=OLIVERCRYSTE&password=DreamTeam18!&sendLogin='
s = requests.session()
s.get("https://www.gamls.com")
resp = s.post("https://www.gamls.com/login/login", data=payload, headers=headers)
html = resp.text
f = open("login.html", "w")
f.write(html)
f.close()
'''

WAIT = 5
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.gamls.com")
time.sleep(WAIT)
driver.find_element_by_id('username2').send_keys("OLIVERCRYSTE")
driver.find_element_by_id('Password2').send_keys("DreamTeam18!")
driver.find_element_by_id('sendLoginSm').click()
time.sleep(WAIT*2)



'''with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.set_default_timeout(120000)
        page.goto('https://www.gamls.com/secure/default')
        #input("solve captcha and enter to continue")
        page.fill("#username", "OLIVERCRYSTE")
        page.fill("#password", "DreamTeam18!")
        page.click("#sendLoginLg")
        time.sleep(WAIT*2)
        page = 1
        page.goto(f"https://www.gamls.com/secure/membership/index.cfm?Typ=Member&Fn=Name&Page={page}")
        for tr in page.query_selector_all("tr"):
            name = tr.query_selector_all("td")[0].inner_text()
            company = tr.query_selector_all("td")[6].inner_text()
            office = tr.query_selector_all("td")[7].inner_text()
            cell = tr.query_selector_all("td")[8].inner_text()
            email = tr.query_selector_all("td")[9].inner_text()
            print(name,company,office,cell,email)


'''