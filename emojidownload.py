import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#for newer versions of chrome, replace with your version of chromedriver
service = Service(executable_path='./chromedriver.exe')

options = Options()
options.add_argument('--headless')

# you can replace this line with `driver = webdriver.Chrome(options=options)` if using chromedriver-autoinstaller
driver = webdriver.Chrome(service= service, options=options)


driver.get('https://googlefonts.github.io/noto-emoji-animation/')
time.sleep(3)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(10)
page = driver.page_source
soup = BeautifulSoup(page, "lxml")
result = soup.find('body')
result = result.find('icons-app')
result = result.find('mat-sidenav-container')
elements = result.find_all('button', class_ = "is-svg ng-star-inserted")

file = open('emoji-lotties.csv', 'w')
fields = ["name", "svg","lottie"]
writer = csv.writer(file, lineterminator='\n')

writer.writerow(fields)

for element in elements:
    src = element.find('img')
    label = src.get('src')
    location = label.strip()
    location = location [47:]
    index = location.find('/')
    if (index >= 0):
        location = location[0:index];
    name = element.find('span', class_ = 'icon-name mat-caption')
    print(f"{name.text.strip()}: ")
    lottie = 'https://fonts.gstatic.com/s/e/notoemoji/latest/{}/lottie.json'.format(location)
    print(f"Writing {name.text.strip()} lottie: {lottie}...")
    svg = 'https://fonts.gstatic.com/s/e/notoemoji/latest/{}/emoji.svg'.format(location)
    print(f"Writing {name.text.strip()} svg: {svg}...")
    r = requests.get(lottie, allow_redirects=True)

################################################################
# Uncomment the following line to download the json files to directory of script
    #open('{}.json'.format(name.text.strip()), 'wb').write(r.content)
################################################################

    writer.writerow(["{}.json".format(name.text.strip()), svg, lottie])
    print(f"{name.text.strip()} Successfully Scraped.")


file.close()

driver.quit()