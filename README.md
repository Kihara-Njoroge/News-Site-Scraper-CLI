[![Code Quality Score](https://www.code-inspector.com/project/24614/score/svg)](https://frontend.code-inspector.com/project/24614/preferences)   [![Code Grade](https://www.code-inspector.com/project/24614/status/svg)](https://frontend.code-inspector.com/project/24614/preferences)


# Scrappy News Site Scraper.
### A final project done in completion of the Skaehub boot bamp.

### 1.Problem Definition
The main objective of the project was to come up with an app for scraping news sites and retrieving the news articles.

### Who is it for?
The app can be used by everyone interested in getting news articles from sites that allow webscarping.


## 2.Commands
   1.<code>python3 scrappy.py </code> -- To run the program
   
   2.<code>scrappy run</code> -- To run the scrappy app
   
   3.<code>scrappy quit</code> ---  To close scrappy the app
   
   
## 3.Installation and Setup

1. Clone this repository into your local machine

2. Create a virtualenv into your machine and activate it.

3. cd into the folder of the clone of the repository.

4. install the packages and dependancies using pip <code> pip install -r requirements.txt </code>

5. run the app using <code> python3 app/scrappy.py </code>

## 4. Testing
We will use nose and coverage to test our app

run: 
    <code>nosetests app --with-covearge </code> and <code> coverage report </code>
  
# Bugs
Due to the inconsistency in the DOM structure of different News Websites. Some websites might not return the the p or a tag.


# Credits
1.[Kihara Njoroge](https://github.com/Babuuh)

2.Skaehub
