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


def alt_texts(div):
    images_without_alt = []
    images = div.find_all('img')

    for img in images:
        if not img.get('alt'):
            images_without_alt.append(img)

    # To tell the users of the bad images
    return images_without_alt


html_text = requests.get("https://webscraper.io/test-sites").text
soup = BeautifulSoup(html_text, "lxml")
# divs = soup.findAll('div')
divs = soup.find('div')
print(font_colour(divs))
