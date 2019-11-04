from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

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
    feature_img_url2 = "https://www.jpl.nasa.gov"
    browser.get(feature_img_url)
    time.sleep(1)
    html2 = browser.page_source
    soup2 = bs(html2, "lxml")

    image = soup2.find("article", class_="carousel_item")['style']
    feature_image = image.split("('", 1)[1].split("')")[0]

    feature_img = feature_img_url2 + feature_image

    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.get(weather_url)
    time.sleep(1)
    html3 = browser.page_source
    soup3 = bs(html3, "lxml")
    weather = soup3.find("p", class_="TweetTextSize").text

    hemishpere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.get(hemishpere_url)
    html4 = browser.page_source
    soup4 = bs(html4, "lxml")
    time.sleep(1)
    hemisphere_img_urls = {}
    all_titles = soup4.find_all('h3')
    y = len(all_titles)
    for x in range(0, y):
        hemisphere_img_urls["title"] = all_titles[x].text
        doc = browser.find_element_by_link_text(all_titles[x].text)
        doc.click()
        time.sleep(1)
        html4 = browser.page_source
        soup4 = bs(html4, "lxml")
        hemisphere_img_urls["img_url"] = soup4.find_all('a', target='_blank')[x]['href']
        browser.back()
    print(hemisphere_img_urls)


# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# {% for hemisphere in mars_data.hemisphere %}
#     <div>
#       <img src="{{hemisphere.url}}">
#       <h3>{{hemisphere.title}}</h3>
#     </div>
#     {% endfor %}

    browser.quit()

    data = {"title": title, "headline_text": headline_text,
            "feature_img": feature_img, "weather": weather}
    browser.close()
    return data
