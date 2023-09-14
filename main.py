from RestaurantScraper import Michelin
import pandas as pd
import time


all_restaurants = {}
for number in range(1,2):
    michelin_page = Michelin(number)
    time.sleep(3)
    curr_dict = michelin_page.get_details()
    time.sleep(3)
    all_restaurants[number] = curr_dict

names = []
cities = []
countries = []
prices = []
styles = []
awards = []
for num in range(1, 833):
    for name in all_restaurants[num]:
        city = all_restaurants[num][name][0]
        country = all_restaurants[num][name][1]
        price = all_restaurants[num][name][2]
        style = all_restaurants[num][name][3]
        award = all_restaurants[num][name][4]
        names.append(name)
        cities.append(city)
        countries.append(country)

        if len(price) > 4:
            prices.append(None)
        elif len(price) == 4:
            prices.append(4)
        elif len(price) == 3:
            prices.append(3)
        elif len(price) == 2:
            prices.append(2)
        else:
            prices.append(1)

        styles.append(style)
        awards.append(award)

restaurant_dictionary = {'Restaurant Name': names, 'City': cities, 'Country': countries, 'Price': prices, 'Style': styles, 'Awards': awards}
df = pd.DataFrame(data=restaurant_dictionary)
