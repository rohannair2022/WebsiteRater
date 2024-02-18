from bs4 import BeautifulSoup, NavigableString
import requests
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
       return 0
    # To tell the users of the bad images
    return (image_with_alt/total_image) * 10


def get_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    page_load_time = end_time - start_time
    
    if page_load_time < 2:
      return 10
    elif page_load_time > 2 and page_load_time < 3:
      return 8
    elif page_load_time > 3 and page_load_time < 5:
      return 5
    else:
      return 0


def evaluate_responsive_design(soup):
    # Check for the viewport meta tag
    viewport_meta_tag = soup.find('meta', {'name': 'viewport'})
    viewport_present = 1 if viewport_meta_tag is not None else 0

    # Calculate the overall rating
    return (viewport_present)*10

# Vision: Contrast

def evaluvate(url):
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, "lxml")
  return [alt_texts(soup), get_page_load_time(url), evaluate_responsive_design(soup)]



