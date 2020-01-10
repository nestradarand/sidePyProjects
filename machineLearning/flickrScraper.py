from bs4 import BeautifulSoup
import requests
import re


url = 'https://www.flickr.com/photos/nasacommons/35549696665/in/album-72157648186433655/'
# response = requests.get(url, timeout = 5)
# content = BeautifulSoup(response.content,'html.parser')

####works
def return_Items(the_url:str,to_look_for:str,attrs1:dict) -> list():
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, 'html.parser')
    if attrs1 is not None:
        return content.findAll(to_look_for,attrs=attrs1)
    else:
        return content.findAll(to_look_for)

def get_all_html_text(the_url:str):
    response = requests.get(url,timeout = 5)
    return BeautifulSoup(response.content,'html.parser')



###get title and date
# title = return_Items(url, 'h1',{"class":" meta-field photo-title "})
###getting the description
# descrs = return_Items(url,'p',None)

####links
# for link in return_Items(url,'a',{'href':re.compile("^http://")}):
#     print(link.get('href'))



