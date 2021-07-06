from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from pyfiglet import Figlet
from requests.api import get
from termcolor import colored
import sys, os
from bs4 import BeautifulSoup
import requests

#displaying app name
f = Figlet(font='slant')
print('--------------------------------------------------------------------------------------------------------------')
print(colored(f.renderText('SCRAPPY'),'green'))
print('Hello User, Welocome To Scrappy. Scrappy Is A web Scrapping cli App')
print('\n''-------------BASIC USAGE----------------' '\n')
print('   1."python app/scrappy.py" ---> to run the app')
print('   2."scrappy run" --> to start the app')
print('   3."scrappy quit" ---> To close the app' '\n')
print('---------------------------------------------------------------------------------------s----------------------')


#prompting user for a command
command = input('Enter a command: ' '\n')

#definig the main function scrappy
def scrappy():
    
    #running the app when user inputs the run command
    if command == 'scrappy run':
        def get_articles():

        #asking a link from the user using pyinquirer
            questions = [
        {
            'type':'input',
            'name':'url',
            'message': 'Enter a news site link: '
        }
    ]
            url = prompt(questions)

            #sending GET request to the url and parsing it
            res = requests.get(url['url']).text
            soup = BeautifulSoup(res, 'html5lib')

            #creating an empty txt file
            file = open("articles.txt", "w")
            file.write('News Articles From ' +url['url'])
            file.write('\n')
            print('\n' '\n')
            print('News Articles From ' + url['url'])

            #fetching the a and p tags
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
            

                #writing the obtained content to the text file     
                file.write("Headline: " + str(data.getText()))
                file.write("\n")
                file.write("story: " + str(description))
                file.write("\n")
                file.write("Link: " + str(article_link))
                file.write("\n")
                file.write("\n")

                #displaying the articles in the cli
                print('Headline: ', data.getText())
                print('Story: ', description)
                print('Read More: ', article_link, '\n')
        return get_articles()

    #closing the app when user enters the quit command
    elif command == 'scrappy quit':
        f = Figlet(font='small')
        print(colored(f.renderText('GoodBye , Thanks for using Scrappy !'),'green'))
        sys.exit()

    #restarting the app if user inputs an invalid command
    else:
        print('Invalid Command!')
        print('Try Again' '\n')
        os.execv(sys.executable, ['python'] + sys.argv)
        







if __name__ == '__main__':
    scrappy()
    while True:
        questions = [
            {
            'type':'input',
            'name':'quiz',
            'message': 'Do Want to Continue Using Scrappy? (repy with Yes to continue or No to Qiut: ) :'
            }   
        ]
        ansa = prompt(questions)
        answer = ansa['quiz']
        if answer.lower() == 'yes':
            scrappy()
        elif answer.lower() == 'no':
            f = Figlet(font='small')
            print(colored(f.renderText('GoodBye , Thanks for using Scrappy !'),'green'))
            break
        