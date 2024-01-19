import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# for newer versions of chrome, replace with your version of chromedriver
service = Service(executable_path="./chromedriver.exe")

options = Options()
options.add_argument("--headless")

# you can replace this line with `driver = webdriver.Chrome(options=options)` if using chromedriver-autoinstaller
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://googlefonts.github.io/noto-emoji-animation/")
time.sleep(3)
print(f"Executing driver...")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
page = driver.page_source
soup = BeautifulSoup(page, "lxml")
result = soup.find("body")
result = result.find("icons-app")
result = result.find("mat-sidenav-container")
elements = result.find_all("button", class_="is-svg ng-star-inserted")

file = open("emoji.csv", "w")
fields = ["name", "svg", "lottie"]

writer = csv.writer(file, lineterminator="\n")

print(f"Opening file... ")
writer.writerow(fields)

output_folder_svg = "svg_files"
output_folder_lottie = "lottie_files"
os.makedirs(output_folder_svg, exist_ok=True)
os.makedirs(output_folder_lottie, exist_ok=True)

for number, element in enumerate(elements):
    src = element.find("img")
    label = src.get("src")
    location = label.strip()
    location = location[47:]
    index = location.find("/")
    if index >= 0:
        location = location[0:index]
    name = element.find("span", class_="icon-name mat-caption")
    print(f"[{number +1}/{len(elements)}] {name.text.strip()}: ")
    lottie = "https://fonts.gstatic.com/s/e/notoemoji/latest/{}/lottie.json".format(
        location
    )
    print(f"Writing {name.text.strip()} lottie: {lottie}...")
    svg = "https://fonts.gstatic.com/s/e/notoemoji/latest/{}/emoji.svg".format(location)
    print(f"Writing {name.text.strip()} svg: {svg}...")
    r = requests.get(svg, allow_redirects=True)
    print(f"{location[-2:]}")
    if location[-2:] == "fb":
        name.append("-1")
    if location[-2:] == "fc":
        name.append("-2")
    if location[-2:] == "fd":
        name.append("-3")
    if location[-2:] == "fe":
        name.append("-4")
    if location[-2:] == "ff":
        name.append("-5")

    ################################################################
    # Uncomment the following lines to download the lottie and SVG files to directory of script
    lottie_filename = os.path.join(
        output_folder_lottie, "{}.json".format(name.text.strip())
    )
    open(lottie_filename, "wb").write(r.content)
    svg_filename = os.path.join(output_folder_svg, "{}.svg".format(name.text.strip()))
    # print(f"Saving {name.text.strip()}")
    open(svg_filename, "wb").write(r.content)
    # print(f"Saved {name.text.strip()}")
    # print(f"{name.text.strip()} Successfully Scraped.")
    ################################################################

    writer.writerow(["{}.json".format(name.text.strip()), svg, lottie])


print(f"Closing file ... ")
file.close()

print(f"Closing script ... ")
driver.quit()
