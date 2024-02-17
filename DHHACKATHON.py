from bs4 import BeautifulSoup, NavigableString
import requests

def color_contrast_helper(div):
    lst = []
    font_color = None
    background_color = None
    if isinstance(div, NavigableString):
        return []
    else:
        background_color = div.get('background-color')
        if div.find(text = True) is None:
            return [background_color, None]
        for i in div.find('',text=True).children:
            font_color = i.get('color')
            lst.append([font_color, background_color])
            for child in div.children:
                lst.extend(color_contrast_helper(child))
    return lst    

def color_contrast(lst):
    i = 0
    sum = 0
    while i < len(lst):
        if lst[i][0] is not None and lst[i][1] is not None:
            hex_color1 = lst[i][0].lstrip('#')
            hex_color2 = lst[i][1].lstrip('#')
            rgb1 = [int(hex_color1[i:i+2], 16) for i in (0, 2, 4)]
            rgb2 = [int(hex_color2[i:i+2], 16) for i in (0, 2, 4)]
            normalized_rgb1 = [component / 255.0 for component in rgb1]
            normalized_rgb2 = [component / 255.0 for component in rgb2]
    
             # Apply luminance formula
            luminance1 = 0.2126 * normalized_rgb1[0] + 0.7152 * normalized_rgb1[1] + 0.0722 * normalized_rgb1[2]
            luminance2 = 0.2126 * normalized_rgb2[0] + 0.7152 * normalized_rgb2[1] + 0.0722 * normalized_rgb2[2]
            sum += luminance1/luminance2

        i += 1
            
    return i

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
    total_image = 0
    image_with_alt = 0
    images = div.find_all('img')

    for img in images:
        if img.get('alt'):
            image_with_alt += 1 
        total_image += 1

    # To tell the users of the bad images
    return (image_with_alt/total_image) * 10


html_text = requests.get("https://webscraper.io/test-sites").text
soup = BeautifulSoup(html_text, "lxml")
print(color_contrast(color_contrast_helper(soup)))
