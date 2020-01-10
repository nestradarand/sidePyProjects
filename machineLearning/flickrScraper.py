from bs4 import BeautifulSoup
import requests
import re
import sys


url = 'https://www.flickr.com/photos/nasacommons/35549696665/in/album-72157648186433655/'
BASE_SITE = 'https://www.flickr.com'
# response = requests.get(url, timeout = 5)
# content = BeautifulSoup(response.content,'html.parser')


def get_parser(the_url:str):
    response = requests.get(the_url,timeout = 5)
    return BeautifulSoup(response.content,'html.parser')


###get title and date
# title = return_Items(url, 'h1', {"class": " meta-field photo-title "})
# for i in title:
#     print(title)

###getting the description
# descrs = return_Items(url,'p',None)


'''
Need to use automation to get the links of all photos and put them in a text file.
Then this can read them one by one and travel to other discovered sources and pull
the description and the title.
'''


def main():
    site_stack = []
    args = sys.argv
    try:
        base_site = sys.argv[2]
        starting_url = sys.argv[1]

        ####get all links on the page
        ####links
        # for line in return_Items(starting_url, 'a', None):
        #     link = line.get('href')
        #     split = link.split('/')
        #     for i in split:
        #         if i == 'photos':
        #             print(link)
        soup = get_parser(starting_url)  
        found  = soup.findAll('div')
        print(found[0])


    

    except Exception:
        print('Invalid number of parameters entered as command line arguments')


    return 0

if __name__ == '__main__':
    main()






