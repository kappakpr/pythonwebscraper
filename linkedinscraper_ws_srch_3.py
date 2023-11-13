from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Creating a webdriver instance
options = Options()
options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Adjust the path accordingly
driver = webdriver.Firefox(options=options)

#login
driver.get("https://linkedin.com/uas/login")
time.sleep(5)
username = driver.find_element(By.ID, "username")
username.send_keys("emailid")
pword = driver.find_element(By.ID, "password")
pword.send_keys("password1")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

search_url = "https://www.linkedin.com/pub/dir?firstName=Anupam&lastName=Gupta&trk=people-guest_people-search-bar_search-submit"
driver.get(search_url)  # this will open the link
start = time.time()
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll});")
	initialScroll = finalScroll
	finalScroll += 300
	time.sleep(3)
	end = time.time()
	if round(end - start) > 20:
		break
src = driver.page_source


soup = BeautifulSoup(src, 'lxml')
results_all = soup.find('div', {'class': 'base-serp-page__content'})

results_list_ul = results_all.find("section", {'class': 'serp-page__results-list'}).find('ul') if results_all else "results_all none"
results_list_li = results_list_ul.find_all('li')
for li in results_list_li:
	print(li.find('h3',{'class':'base-search-card__title'}).get_text().strip() if li.find('h3',{'class':'base-search-card__title'}) else "Name not found")
	print(li.find('h4', {'class': 'base-search-card__subtitle'}).get_text().strip() if li.find('h4', {'class': 'base-search-card__subtitle'}) else "short desc. not found")
	print(li.find('div', {'class': 'base-search-card__metadata'}).find('p',{'class':'people-search-card__location'}).get_text().strip() if li.find('div', {'class': 'base-search-card__metadata'}).find('p',{'class':'people-search-card__location'}) else "Name not found")
	li_meta_list = li.find_all('div',{'class':'entity-list-meta'})#
	for li_meta in li_meta_list:
		print(li_meta.find('span', {'class': 'entity-list-meta__entities-list'}).get_text().strip() if li_meta.find('span', {'class': 'entity-list-meta__entities-list'}) else "Name not found")
	print("next --->")
else:
	print("ul li not found")

driver.quit()
