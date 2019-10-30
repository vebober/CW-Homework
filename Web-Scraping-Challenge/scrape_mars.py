from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time


weather_url = "https://twitter.com/marswxreport?lang=en"
facts_url = "https://space-facts.com/mars/"
hemishpere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


def init_browser():
    return webdriver.Chrome("mac/chromedriver")


def scrape_info():
    mars_news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser = init_browser()
    browser.get(mars_news_url)
    time.sleep(1)

    html = browser.page_source
    soup = bs(html, "lxml")

    title = soup.find_all("div", class_="content_title")[0].text
    headline_text = soup.find_all("div", class_="article_teaser_body")[0].text

    

    feature_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # browswer = init_browser()
    browser.get(feature_img_url)
    time.sleep(1)
    html2 = browser.page_source
    soup2 = bs(html2, "lxml")

    style = soup2.find()"article",class_="carousel_item")[0]
    
    image = style.split("('", 1)[1].split("')")[0]

    feature_img = feature_img_url + image

    data = {"title": title, "headline_text": headline_text,"feature_img":feature_img}
    browser.close()
    return data
/html/body/div[1]/div/div[3]/section[1]/div/div/article