import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from scraper.constant import NETFLIX_URL, NUMBER_EACH_GENRE, NUMBER_SECTION, TIME_SLEEP


def scrape():
    """
    Scrape netflix to get required number of movie information
    """
    # get the driver and soup
    driver = get_driver()
    soup = get_soup(NETFLIX_URL, driver)
    if soup is None:
        return None

    count = 0
    video_list = []
    id_set = set()
    # find the collections of videos
    collections = soup.find('main', role='main')
    sections = collections.find_all('section')
    # for each section of genre
    for section in sections:
        # find all list of videos in this section
        lis = section.find_all('li')
        # count videos scraped in current section
        count_current = 0
        # target number of this section
        target_number = NUMBER_EACH_GENRE
        # for each video in current section/genre
        for li in lis:
            if count_current >= target_number:
                break
            # get the link to detail page
            a = li.find('a')
            if not a:
                break
            link = a['href']
            # find image
            img = li.find('img')
            if not img:
                # img not found, skip
                target_number -= 1
                continue
            # get id
            curr_id = img['data-title-id']
            # check if id is repeated
            if curr_id in id_set:
                target_number -= 1
                continue
            # print progress message
            print('-'*20, f'Scraping video {count + 1}', '-'*20)
            # scrape and get the dict that stores the information of current video
            video_dict = scrape_one(link, driver)
            if not video_dict:
                print('Error in scraping')
                target_number -= 1
                continue
            # add index to dict
            video_dict['index'] = count
            # add Netflix video url to dict
            video_dict['netflix_url'] = link
            # add image url to dict
            video_dict['image_url'] = img['src']
            # add id to dict
            video_dict['id'] = curr_id
            # add current id to id_set
            id_set.add(curr_id)
                
            # add current dict to list
            video_list.append(video_dict)
            # increment count
            count_current += 1
            count += 1
    
    driver.quit()
    return video_list


def scrape_one(url, driver):
    """
    Scrape one movie to get details by url
    
    Parameters:
    url: url of current video
    driver: chrome driver
    """
    video_dict = {}
    # get soup
    soup = get_soup(url, driver)
    if soup is None:
        return video_dict

    title_info_div = soup.find('div', class_='title-info')
    # get name
    name = title_info_div.find('h1').text.strip()
    video_dict['name'] = name
    # get synopsis
    synopsis = title_info_div.find('div', class_='title-info-synopsis').text.strip()
    video_dict['synopsis'] = synopsis
    # get casts
    starring_div = title_info_div.find('div', class_='title-data-info-item item-starring')
    if starring_div:
        starring = starring_div.find('span', class_='title-data-info-item-list').text.strip()
        video_dict['casts'] = starring
    # get creators
    creators_div = title_info_div.find('div', class_='title-data-info-item item-creators')
    if creators_div:
        creators = creators_div.find('span', class_='title-data-info-item-list').text.strip()
        video_dict['creators'] = creators
    # get genres
    genres_div = soup.find('div', class_='more-details-cell cell-genres')
    if genres_div:
        genres_container = genres_div.find('div', class_='more-details-item-container')
        if genres_container:
            genres = genres_container.text.strip()
            video_dict['genres'] = genres
    # get mood tag
    mood_tag_div = soup.find('div', class_='more-details-cell cell-mood-tag')
    if mood_tag_div:
        mood_tag_container = mood_tag_div.find('div', class_='more-details-item-container')
        if mood_tag_container:
            mood_tag = mood_tag_container.text.strip()
            video_dict['mood_tag'] = mood_tag

    return video_dict


def get_soup(url, driver):
    """
    Get the soup by url.
    Uses webdriver object to execute javascript code and get dynamically loaded webcontent
    """
    driver.get(url)
    time.sleep(TIME_SLEEP)
    if url == NETFLIX_URL:
        for idx in range(NUMBER_SECTION):
            print(f'Clicking show more button for section {idx + 1}')
            # load more data by clicking button more
            button_more = driver.find_element_by_xpath(f'/html/body/div/div/div/main/section[{idx + 1}]/div/button')
            for _ in range(4):
                ActionChains(driver).move_to_element(button_more).click(button_more).perform()
                time.sleep(TIME_SLEEP)
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html, 'html.parser')
    return soup


def get_driver():
    """
    Create a webdriver object and set options for headless browsing
    """
    options = Options()
    options.headless = True
    options.add_argument("--disable-infobars")
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome('./chromedriver', options=options)
    return driver
