'''import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager'''

'''#give driver a link to the scraping site

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.olx.pl/d/nieruchomosci/mieszkania/")

########################################
#accept cookies

time.sleep(1)
try:
    accept = driver.find_element_by_id(By.ID, 'onetrust-accept-btn-handler')
    accept.click()
except:
    pass'''

##########################################
#filters

#City
city = driver.find_element(By.CLASS_NAME,"css-uvldze").send_keys("Wrocław")
cityChoice = driver.find_element(By.CLASS_NAME,"css-7lx9dr").click()
driver.find_element(By.CLASS_NAME,"css-1veigyg").click()

time.sleep(3)

#typeRent
typeRent = driver.find_element_by_xpath("(//div[@class='css-1qvyz1h'])[2]").click()
driver.find_element_by_xpath("(//div[@class='css-1oi36r6'])[2]").click()

time.sleep(1)

#rooms
numberRooms = driver.find_element_by_xpath("(//div[@class='css-t0lbh8'])[8]").click()
twoBed = driver.find_element_by_xpath("(//div[@class='css-1rfy03l'])[3]").click()

#time.sleep(1)

#priceLow
priceLow = driver.find_element_by_xpath("(//div[@class='css-1qsx3gp'])[3]").click()
driver.find_element_by_xpath("(//div[@class='css-hhk6z5'])[7]").click()

time.sleep(1)

#priceHigh
priceHigh = driver.find_element_by_xpath("(//div[@class='css-1qsx3gp'])[4]").click()
driver.find_element_by_xpath("(//div[@class='css-hhk6z5'])[9]").click()

time.sleep(1)

#space
space = driver.find_element_by_xpath("(//div[@class='css-t0lbh8'])[11]").click()
cubicMeters = driver.find_element_by_xpath("(//div[@class='css-hhk6z5'])[2]").click()

time.sleep(3)

#ownership
for _ in range(2):
    private = driver.find_element_by_xpath("//*[contains(text(), 'Prywatne')]").click()

#######################################
#get all the hrefs

listOffers = driver.find_elements(By.CLASS_NAME, "css-rc5s2u")
links = []

#for i in range(0,len(listOffers)):
#    links.append(listOffers[i].get_attribute("href"))

for i in range(0,len(listOffers)):
    links.append(listOffers[i].get_attribute("href"))

###############################################
#scarping info from every item on the list

nazwa = []
cena = []
prywatne = []
pietro = []
meble = []
rodzajZab = []
pow = []
pokoje = []
czynsz = []

for link in links[1:5]:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)

    #price
    try:
        roomPrice = driver.find_element(By.CLASS_NAME, "css-dcwlyx").get_attribute("textContent")
        cena.append(roomPrice)
    except:
        cena.append("brak danych")

    #nazwa
    try:
        tytulLinka = driver.find_element_by_xpath('//h1[@class="css-1soizd2 er34gjf0"]').get_attribute("textContent")
        nazwa.append(tytulLinka)
    except:
        nazwa.append("brak danych")

    #create list of attributes
    attributes = []
    options = driver.find_elements(By.CLASS_NAME, "css-1r0si1e")

    for i in range(0, len(options)):
        attributes.append(options[i].get_attribute("textContent"))

    try:
        prywatne.append(attributes[0])
        pietro.append(attributes[1])
        meble.append(attributes[2])
        rodzajZab.append(attributes[3])
        pow.append(attributes[4])
        pokoje.append(attributes[5])
        czynsz.append(attributes[6])

    except:
        continue

    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

Results = pd.DataFrame({'URL': links[1:5], 'Tytuł': nazwa, 'Cena': cena, 'Powierzchnia': pow, 'Czynsz': czynsz},
                       columns=['URL', 'Tytuł', 'Cena', 'Powierzchnia', 'Czynsz'])

Results.drop_duplicates(inplace=True)

Results.to_excel('results.xlsx')





