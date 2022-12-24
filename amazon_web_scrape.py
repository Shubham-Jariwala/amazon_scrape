from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_6%3AA14CZOWI0VEHLG%7CA1P3OPO356Q9ZB%7CA2HIN95H5BP4BL%2Cp_89%3AApple&ref=mega_elec_s23_1_2_1_6"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="s-card-container")

with open('amazon.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Iphone_model', 'Rating out of 5', 'Price', 'Number of Ratings']
    thewriter.writerow(header)

    for list in lists:
        iphone_model = list.find('span', class_="a-text-normal").text
        rating = list.find('span', class_="a-size-base").text
        price = list.find('span', class_="a-price-whole").text
        number_of_ratings = list.find('span', class_="s-underline-text").text

        info = [iphone_model, rating, price, number_of_ratings]
        thewriter.writerow(info)