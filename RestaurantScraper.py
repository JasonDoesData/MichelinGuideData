import requests
import webbrowser
from bs4 import BeautifulSoup
import time

class Michelin:
    def __init__(self, page_num):
        self.page_num = page_num
        self.url = f'https://guide.michelin.com/gb/en/restaurants/page/{self.page_num}'
        # webbrowser.open(url)
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def find_elements(self):
        return self.soup.find_all('div', {"class": "card__menu-content js-match-height-content"})

    def get_details(self):
        elements = self.find_elements()
        restaurants_dict = {}
        for num in range(len(elements)):
            restaurant_name = elements[num].find('h3').getText().strip()
            location = elements[num].find('div',
                                          {"class": "card__menu-footer--location flex-fill pl-text"}).getText().strip()
            if ',' in location:
                city = location.split(",")[0]
                country = location.split(",")[1].strip()
            else:
                city = None
                country = location

            price = \
            elements[num].find('div', {"class": "card__menu-footer--price pl-text"}).getText().strip().replace(" ",
                                                                                                               '').replace(
                '·', '').split()[0]

            if "·" in elements[num].find('div', {"class": "card__menu-footer--price pl-text"}).getText():
                cuisine = elements[num].find('div', {"class": "card__menu-footer--price pl-text"}).getText()[
                          41:].replace('·', '').strip()
            else:
                cuisine = elements[num].find('div', {"class": "card__menu-footer--price pl-text"}).getText().strip()
            images = elements[num].find_all('img')
            stars = 0

            if len(images) > 0:
                for image in images:
                    if 'star' in image['src']:
                        stars += 1

            restaurants_dict[restaurant_name] = [city, country, price, cuisine, stars]
        return restaurants_dict