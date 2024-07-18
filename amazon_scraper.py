import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_string = title.text.strip()
    except AttributeError:
        title_string = ""
    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).text.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).text.strip()
        except AttributeError:
            price = ""
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).text.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).text.strip()
        except AttributeError:
            rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).text.strip()
    except AttributeError:
        review_count = ""
    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'}).find("span").text.strip()
    except AttributeError:
        available = "Not Available"
    return available

if __name__ == '__main__':
    HEADERS = {'User-Agent': 'Your User-Agent', 'Accept-Language': 'en-US, en;q=0.5'}
    URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"

    # Make the request and get the soup
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links]

    data = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}

    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Collect data
        data['title'].append(get_title(new_soup))
        data['price'].append(get_price(new_soup))
        data['rating'].append(get_rating(new_soup))
        data['reviews'].append(get_review_count(new_soup))
        data['availability'].append(get_availability(new_soup))

        # Add delay to avoid overloading the server
        time.sleep(2)  # Adjust the delay as necessary

    amazon_df = pd.DataFrame.from_dict(data)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)

    print(amazon_df)
