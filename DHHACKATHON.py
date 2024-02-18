import requests
#Importing the library that deals with the retrieval of info from a url online
from urllib.request import urlopen
#Importing the library that deals with the retrieval of info from a file locally.
from urllib.request import urlretrieve

# Throw an error when there is an issue occured while retrieving the data
from urllib.error import HTTPError
# Used to throw the error when the server is not found at all
from urllib.error import URLError

#This is the library for the web scraper
from bs4 import BeautifulSoup 
import time

def alt_texts(div):
    total_image = 0
    image_with_alt = 0
    images = div.find_all('img')

    for img in images:
        if img.get('alt'):
            image_with_alt += 1
        total_image += 1

    if total_image == 0:
        return [0, "Websites should generally have images to convey visual informations."]

    # To tell the users of the bad images
    if (image_with_alt/total_image) * 10 < 10:
        return [(image_with_alt/total_image) * 10, f"Only {(image_with_alt//total_image).__round__()}% of images in your website have alt text. This this important to implement to aid visually impaired users' uses of text to speech technology."]

    return [10, "Good job! Every images in your website have alt texts."]

def header_font_size(head_section):
    score = 10
    num_lib = {}
    num_lis = []

    head_section = head_section.find("header")

    if head_section is None:
        return [0, "The body section does not exists"]

    for i in range(1,5):
        head = head_section.findAll("h" + str(i))
        if i not in num_lib:
            num_lib[i] = 0
        for j in head:
            num_lib[i] += len(j.text)
            for k in range(len(j.text)):
                num_lis.append(i)

    num_lis = sorted(num_lis)
    avg_size = 0
    total_char = 0

    for i in num_lib:
        avg_size += num_lib[i] * i
        total_char += num_lib[i]

    if total_char == 0:
        return [0, "There seems to be no h texts in the footer section."]
    avg_size = avg_size // total_char

    Q_1 = num_lis[len(num_lis) // 4]
    Q_3 = num_lis[3 * len(num_lis) // 4]

    IQR = Q_3 - Q_1

    if avg_size > Q_3 + IQR or avg_size < Q_1 + IQR:
        score = 5
        return [score, "A sizable portion of texts in the header section have their fonts on the extreme sides in comparision to the average text size in the header."]

    print("foot:", score)
    return [score, "The average text size in the header falls within the acceptable range of deviation."]


def body_font_size(body_section):
    score = 10
    num_lib = {}
    num_lis = []

    body_section = body_section.find("body")

    if body_section is None:
        return [0, "The body section does not exists"]

    for i in range(1,5):
        body = body_section.findAll("h" + str(i))
        if i not in num_lib:
            num_lib[i] = 0
        for j in body:
            num_lib[i] += len(j.text)
            for k in range(len(j.text)):
                num_lis.append(i)

    num_lis = sorted(num_lis)
    avg_size = 0
    total_char = 0

    for i in num_lib:
        avg_size += num_lib[i] * i
        total_char += num_lib[i]

    if total_char == 0:
        return [0, "There seems to be no h texts in the footer section."]
    avg_size = avg_size // total_char

    Q_1 = num_lis[len(num_lis) // 4]
    Q_3 = num_lis[3 * len(num_lis) // 4]

    IQR = Q_3 - Q_1

    if avg_size > Q_3 + IQR or avg_size < Q_1 + IQR:
        score = 10
        return [score, "A sizable portion of texts in the body section have their fonts on the extreme sides in comparision to the average text size in the header."]

    print("foot:", score)
    return [score, "The average text size in the body falls within the acceptable range of deviation."]


def footer_font_size(foot_section):
    score = 10
    num_lib = {}
    num_lis = []

    foot_section = foot_section.find("footer")

    if foot_section is None:
        return [0, "The footer section does not exists"]

    for i in range(1,5):
        foot = foot_section.findAll("h" + str(i))
        if i not in num_lib:
            num_lib[i] = 0
        for j in foot:
            num_lib[i] += len(j.text)
            for k in range(len(j.text)):
                num_lis.append(i)

    num_lis = sorted(num_lis)
    avg_size = 0
    total_char = 0

    for i in num_lib:
        avg_size += num_lib[i] * i
        total_char += num_lib[i]

    if total_char == 0:
        return [0, "There seems to be no h texts in the footer section."]
    avg_size = avg_size // total_char

    Q_1 = num_lis[len(num_lis) // 4]
    Q_3 = num_lis[3 * len(num_lis) // 4]

    IQR = Q_3 - Q_1

    if avg_size > Q_3 + IQR or avg_size < Q_1 + IQR:
        score = 5
        return [score, "A sizable portion of texts in the footer section have their fonts on the extreme sides in comparision to the average text size in the header."]

    return [score, "The average text size in the footer falls within the acceptable range of deviation."]


def get_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    page_load_time = end_time - start_time

    if page_load_time < 1.5:
        return [10, "Your website's average loadtime falls below web users' average attention span when waiting for a website to load."]
    elif page_load_time > 1.5 and page_load_time < 3:
        return [8, "Your website's average loadtime falls within web users' average attention span when waiting for a website to load."]
    elif page_load_time > 3 and page_load_time < 4:
        return [5, "Your website's average loadtime falls above web users' average attention span when waiting for a website to load."]
    else:
        return [0, "Your website took too long to load."]

def calculate_contrast_ratio(color1, color2): # value of (r, g, b) and (r, g, b)
    def rgb_to_luminance(color):
        r, g, b = color
        r_srgb = r / 255.0 if r <= 10 else ((r / 255.0) ** 2.2)
        g_srgb = g / 255.0 if g <= 10 else ((g / 255.0) ** 2.2)
        b_srgb = b / 255.0 if b <= 10 else ((b / 255.0) ** 2.2)
        return 0.2126 * r_srgb + 0.7152 * g_srgb + 0.0722 * b_srgb

    ratio = 0

    luminance1 = rgb_to_luminance(color1)
    luminance2 = rgb_to_luminance(color2)

    if luminance1 > luminance2:
        ratio = (luminance1 + 0.05) / (luminance2 + 0.05)
    else:
        ratio = (luminance2 + 0.05) / (luminance1 + 0.05)

    if ratio < 3:
        return ["Poor contrast ratio between background colour and text colour based on the criterias provided by the WCAG."]
    elif ratio >= 3 and ratio < 4.5:
        return ["Fair contrast ratio between background colour and text colour based on the criterias provided by the WCAG."]
    else:
        return ["Good contrast ratio between background colour and text colour based on the criterias provided by the WCAG."]

def evaluate_responsive_design(soup):
    # Check for the viewport meta tag
    viewport_meta_tag = soup.find('meta', {'name': 'viewport'})
    viewport_present = 1 if viewport_meta_tag is not None else 0

    if viewport_present == 0:
        return [(viewport_present)*10, "Your website  does not support viewport which allows for dynamic resizing whenever the window resizes."]
    # Calculate the overall rating
    return [(viewport_present)*10, "Your website supports viewport which allows for dynamic resizing whenever the window resizes."]


# Vision: Contrast

def evaluvate(url):
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, "lxml")
  return [header_font_size(soup), body_font_size(soup), footer_font_size(soup), alt_texts(soup), get_page_load_time(url), evaluate_responsive_design(soup)]



