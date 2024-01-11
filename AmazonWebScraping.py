#pip install selenium

# Import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
from selenium import webdriver #To scrape a webpage that relies on JavaScript to load dynamic content


# Let's create a csv file
import csv

header = ['Title', 'Price', 'Reviews', 'Date']

# Let's name our file
with open('AmazonWebScraperData.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)


import pandas as pd

df = pd.read_csv(r'/Users/haleybengtson/AmazonWebScraperData.csv')
print(df)


# Let's create a function to check the price
def check_price():
    url = 'https://www.amazon.com/Purina-Pro-Plan-Shredded-Chicken/dp/B001VIWHMY/ref=sr_1_1_sspa?c=ts&dib=eyJ2IjoiMSJ9.gTlB5Nw7kn5_xISkmyyvDNEcy5lBTgMwVve74BV4FSuk92cRMtaoje1zlHB2Pv4ttxluzKLSHb-IBu_4M6tEKQ.g6yhi4W91euRABnH1G6S55Fr4Vau_9AfY50wHwoNoSA&dib_tag=se&keywords=Dog%2BFood&qid=1704995498&rdc=1&s=pet-supplies&sr=1-1-spons&ts_id=2975359011&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

    # Use Selenium to load the page with JavaScript
    driver = webdriver.Chrome()  # You need to have the ChromeDriver installed and in your PATH
    driver.get(url)

    # Wait for the page to load (you might need to adjust the sleep time)
    time.sleep(10)

    # Get the page source after JavaScript has loaded
    page_source = driver.page_source

    # Close the browser window
    driver.quit()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    soup_pretty = BeautifulSoup(soup.prettify(), 'html.parser')

    # Let's extract the product title, price, and reviews
    title = soup_pretty.find(id='productTitle').get_text()

    price_element = soup_pretty.select_one('.a-section.a-spacing-none.aok-align-center .a-price.a-text-price.a-size-medium.apexPriceToPay .a-offscreen')
    price = price_element.get_text()
    
    reviews_element = soup_pretty.find(class_='a-icon a-icon-star a-star-4-5 cm-cr-review-stars-spacing-big')
    reviews = reviews_element.find('span', class_='a-icon-alt').get_text()

    # Let's strip the whitespaces of the outputs and then we'll print it so we can verify it worked
    price = float(price.strip()[1:])
    formatted_price = "{:.2f}".format(float(price))
    title = title.strip()
    reviews = reviews.strip()
    
    today = datetime.date.today()
    
    # Let's create a csv file
    import csv

    header = ['Title', 'Price', 'Reviews', 'Date']
    data = [title, formatted_price, reviews, today]
    
    # We are now appending data to the csv
    with open('AmazonWebScraperData.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# We're going to put our function on a timer to run every day
while(True):
    check_price()
    # timer runs every day -> 86,400 seconds
    time.sleep(86400)


import pandas as pd

df = pd.read_csv(r'/Users/haleybengtson/AmazonWebScraperData.csv')
print(df)

