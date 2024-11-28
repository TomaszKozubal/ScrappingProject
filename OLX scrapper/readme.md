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
