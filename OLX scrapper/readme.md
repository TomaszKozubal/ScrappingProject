# Real Estate Data Scraper

This project is a web scraping script designed to extract data from a Polish real estate website, **OLX.pl**, focusing on rental apartment listings. It uses Selenium and Pandas to gather, process, and export data into an Excel file.

## Features

- **Automated Navigation**: The script automates interactions with the website, including accepting cookies, setting search filters (city, price range, number of rooms, etc.), and collecting data from multiple listings.
- **Data Extraction**: Scrapes details such as:
  - Listing URL
  - Title
  - Price
  - Area (in square meters)
  - Additional fees (e.g., rent, maintenance)
- **Export**: Outputs the scraped data into an Excel file for further analysis.

## Technologies Used

- **Python**: Main programming language.
- **Selenium**: For browser automation and data scraping.
- **Pandas**: To organize and export scraped data into Excel.
- **GeckoDriver**: To interact with Firefox browser.
- **Webdriver Manager**: Simplifies the setup of GeckoDriver.

How to Use
Install Requirements: Ensure all required packages are installed using the command above.

Run the Script: Execute the script in your preferred Python environment. If using Jupyter Notebook, ensure each cell is executed sequentially:

python
Skopiuj kod
# Install necessary packages
!pip install selenium pandas webdriver-manager
Run the script:

python
Skopiuj kod
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Initialize WebDriver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.olx.pl/d/nieruchomosci/mieszkania/")

# Accept cookies
time.sleep(1)
try:
    accept = driver.find_element_by_id(By.ID, 'onetrust-accept-btn-handler')
    accept.click()
except:
    pass

# Set filters
city = driver.find_element(By.CLASS_NAME, "css-uvldze").send_keys("Wrocław")
cityChoice = driver.find_element(By.CLASS_NAME, "css-7lx9dr").click()
driver.find_element(By.CLASS_NAME, "css-1veigyg").click()

# Continue with filters and scraping process...
Output: The scraped data will be saved as results.xlsx in the script's directory.

Example Output
URL	Title	Price	Area (m²)	Additional Fees
link to listing	Cozy Apartment in Wrocław	2,500 zł	50	300 zł
