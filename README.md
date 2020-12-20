# web-scraping-challenge
In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page

Many programs were utilized in order to scrape and render outputs, like **Flask**, **MongoDB**, **Jupyter Notebook**, **Python**, **Pandas**, **HTML/CSS**, **BeautifulSoup**, and **Splinter**.
![marsimg](https://geneticliteracyproject.org/wp-content/uploads/2017/11/mars-2.jpg)
## Navigating this repository
Contained in the *Missions_to_Mars* folder is all the code used to complete this assignment, including:

- ```mission_to_mars.ipynb``` file used to scrape data using Splinter and Beautiful Soup
- Python files required for running the Flask app, like ```app.py``` and ```scrape_mars.py```
- HTML/CSS files for the Flask page contained in the *templates* and *static* folders

# Step 1: Scraping
The scraping process utilized Jupyter Notebook, BeautifulSoup, Pandas, Requests, and Splinter. <a href="https://github.com/drainganggtb/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb" target="_blank">mission_to_mars.ipynb</a>
 contains all of the scraping work and Pandas data frames which were created in the process.

### The sites which were scraped were:
#### NASA Mars News
 The [Nasa Mars News site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) was scraped to collect the latest news title and paragraph text, which were assigned to referenceable variables
 ```
 news_title = "NASA's Next Mars Mission to Investigate Interior of the Red Planet"
 news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May"
 ```

#### JPL Mars Space Images Featured Image
Next, the [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) was navigated to and scraped. The image url was assigned to a variable called ```featured_image_url```. Care was taken in order to get the full-size ```.jpg``` image. 
```
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```
#### Mars Facts
The [Mars facts website](https://space-facts.com/mars/) was scraped to obtain a table of facts about the planet like mass, diameter, number of moons, etc. Pandas was used to convert the data to a HTML table string.
#### Mars Hemispheres 
[USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) was next visited in order to obtain high resolution images for the hemispheres of Mars. 
- The links to the hemispheres needed to be clicked in order to find the image url to the full resolution image
    - This process entailed using **Splinter** to interact with web pages.
- The image url string for the full resolution image and hemisphere title were stored in Python dictionary/key word pairs using the keys ```img_url``` and ```title```.

# Step 2: MongoDB and Flask Application
MongoDB with Flask was used to create a new HTML page that displays all the previously scraped information from the URLs above. 
- This process began by converting the Jupyter notebook into a python script called ```scrape_mars.py``` with a function called ```scrape``` that will execute all of the scraping code and return one Python dictionary containing all of the scraped data.
- Next, the ```/scrape``` route was made within ```app.py``` to import ```scrape_mars.py``` and call the ```scrape``` function.
    - The return value was stored in Mongo as a Python dictionary
    - It was necessary to overwrite the existing document each time the ```/scrape``` url is visited and new data is obtained. 
- The root route ```/``` will query the Mongo database and pass the Mars data into an HTML template to display the data.
- The template file, ```index.html```, takes the dictionary and displays it in appropriate HTML elements. 

The following images show the output of the Flask app when run.

[first](https://github.com/drainganggtb/web-scraping-challenge/blob/main/Missions_to_Mars/images/homepage.png)
[second](https://github.com/drainganggtb/web-scraping-challenge/blob/main/Missions_to_Mars/images/hemi_img.png)