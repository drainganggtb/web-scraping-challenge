from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def scrape():
    
    #splinter setup
    #Insert splinter path to chromedriver
    executable_path = {'executable_path': r"C:\chromedriver"}
    browser = Browser('chrome', **executable_path, headless=False)

    #set up dictionary
    mars_info={}

    #All of these sites must be scraped
    news_url = 'https://mars.nasa.gov/news/'
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    facts_url = 'http://space-facts.com/mars/'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    #access NASA Mars page using splinter for NEWS
    browser.visit(news_url)
    time.sleep(5)

    #html object
    news_html = browser.html
    #create beautiful soup object to parse
    soup = bs(news_html, 'html.parser')

    #find title and p elements using splinter after looking in inspector
    titles = soup.find_all('div', class_='content_title')
    p_elements = soup.find_all('div', class_='article_teaser_body')
    news_title = titles[1].text
    news_p=p_elements[0].text

    mars_info['news_title']=news_title
    mars_info['news_p']=news_p

    #tell splinter to visit image url for IMAGE
    browser.visit(image_url)
    time.sleep(5)
    #html object
    img_html = browser.html
    img_soup = bs(img_html, 'html.parser')

    #get url of full image from inside style tag
    featured_image = img_soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Display url of the full image
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image}"

    mars_info['featured_image_url']=featured_image_url

    # use pandas to scrape and create df for FACTS
    fact_list = pd.read_html(facts_url)
    #navigate to desired table and create df
    fact_df = fact_list[0].rename(columns={0:"Descriptor", 1: "Mars"})
    fact_df.set_index('Descriptor', inplace=True)

    #save df into html table format
    mars_html_facts = fact_df.to_html()

    #remove unwatned new lines
    mars_html_facts.replace('\n','')

    #add to dict
    mars_info['mars_facts']=mars_html_facts

    #use splinter to visit HEMISPHERES site
    browser.visit(hemispheres_url)

    #main url for loop
    hemisphere_base_url = 'https://astrogeology.usgs.gov'
    time.sleep(5)

    #HTML object
    html_hemisphere = browser.html

    #start parsing with BS
    soup = bs(html_hemisphere, 'html.parser')

    #get all info about hemispheres by scraping item classes
    astropedia = soup.find_all('div', class_='description')

    #create list to populate using for loop for image urls
    hemisphere_image_url =[]

    #loop which gathers hemisphere info
    for item in astropedia:
        #Take name of hemisphere and clean it
        item_name=str(item.find('a').text).replace(" Enhanced","")
        
        #create new link to download full quality image
        url_add=item.find('a')['href']
        full_url=hemisphere_base_url+url_add
        
        #click on hemisphere page
        browser.visit(full_url)
        time.sleep(5)
        link=browser.html
        
        #parse through second page
        souplink=bs(link,'html.parser')
        #from second site, hone in on link using class = wide-image
        item_image=hemisphere_base_url+souplink.find('img',class_="wide-image")['src']
        #append links to list in python dictionary form
        hemisphere_image_url.append({"title":item_name, "img_url":item_image})

        #add more to dict
        mars_info['hemispheres_info']=hemisphere_image_url

    
    browser.quit()

    return mars_info



