import unittest
from unittest.case import TestCase
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

url = 'https://news.yahoo.com/science/'
res = requests.get(url).text
soup = BeautifulSoup(res, 'html5lib')

class test_scaper(TestCase):

    #testing when the user enters an empty string as a url
    def test_blank_url(self):
        def is_url(url):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc])
            except ValueError:
                 return False
        self.assertFalse(is_url(''))


    #testing when the user enters an invalid string as a url
    def test_invalid_url(self):
        def is_url(url):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc])
            except ValueError:
                 return False
        self.assertFalse(is_url('hello'))
    
    
    #testing when a valid url is entered
    def test_valid_url(self):
        def is_url(url):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc])
            except ValueError:
                 return False
        self.assertTrue(is_url(url))


    #test if the page content exists
    def test_content_exist(self):
        self.assertIsNotNone(soup)

    #test whether the headlines(h2, h3) are fetched/exists
    def test_headline_exists(self):
        headline = soup.find(['h2', 'h3'])
        self.assertIsNotNone(headline)

    #test whether the story(p tags) are fetched/exists  
    def test_story(self):
        headline = soup.find_all(['h2', 'h3'])

        for data in headline:
            try:
                story = data.find_next_sibling("p").text
            except TypeError:
                story = data.find_next_sibling("p").text
            except:
                story = data.find_previous_sibling("p").text
            self.assertIsNotNone(story)

    #test whether the links to the story are fetched/exists 
    def test_link(self):
        headline = soup.find_all(['h2', 'h3'])
        for data in headline:
            try:
                link = data.findChild("a")['href']
            except TypeError:
                link = data.find_parent('a')['href']

            self.assertIsNotNone(link)

if __name__ == '__main__':
    unittest.main()