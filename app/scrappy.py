import requests
import pandas
from bs4 import BeautifulSoup
import fire



#get articles function
def get_articles():

    #asking user to input a link
    url = input('Enter A News Site URL: ')

    #sending GET request to the url and parsing it
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html5lib')

    articles_list = []

    file = open("articles.txt", "w")

    for data in soup.find_all(['h2','h3']):
        article_link = ''
        description = ''
        try:
            article_link = data.findChild("a")['href']
            description = data.find_next_sibling("p").text

        except TypeError:
            article_link = data.find_parent('a')
            description = data.find_next_sibling("p")
        except AttributeError:
            description = data.find_next_sibling("a")
            description = data.find_previous_sibling("p")
        
        articles_list = [str(data.getText()),str(description), str(article_link)]
   
   
        file.write(str(articles_list))


        print('Headline: ', data.getText())
        print('Story: ', description)
        print('Read More: ', article_link, '\n')
        
if __name__ == '__main__':
    fire.Fire(get_articles)