from bs4 import BeautifulSoup
import requests


# color
def font_colour(div):
    colours = []
    elements = div.find_all(attrs={"color": True})

    for element in elements:
        colour = element.get('color')
        colours.append(colour)

    return colours


# background-color
def bg_colour(div):
    bg_colours = []
    bg_elements = div.find_all(attrs={"background-color": True})

    for element in bg_elements:
        colour = element.get('color')
        # can call font_colour here to compare the current background colour and the text colour of the div here




        bg_colours.append(colour)

    return bg_colours


# First task - eqaution
def alt_texts(div):
    total_image = 0
    image_with_alt = 0
    images = div.find_all('img')

    for img in images:
        if img.get('alt'):
            image_with_alt += 1 
        total_image += 1

    # To tell the users of the bad images
    return image_with_alt/total_image


html_text = requests.get("https://webscraper.io/test-sites").text
soup = BeautifulSoup(html_text, "lxml")
divs = soup
print(font_colour(divs))