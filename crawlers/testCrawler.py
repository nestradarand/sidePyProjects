import requests
from bs4 import BeautifulSoup


def parse_craigslist_data(tree):

    results_p = tree.find_all('p',{'class':'result-info'})
    for res_data in results_p:
        print('_____NEWITEM_______')
        price = res_data.findChild('span',{'class':'result-price'})
        area = res_data.findChild('span',{'class':'result-hood'})
        date =  res_data.findChild('time',{'class':'result-date'})
        ####deal with none type in the event of text property
        if price:
            print(price.text)
        if area:
            print(area.text)
        if date:
            print(date.text)

def parse_next_page(tree,root_url):
    next_page = tree.find('a',{'class':'button next'})
    print('{0}{1}'.format(root_url,next_page['href']))


def main():
    starting_url = 'https://orangecounty.craigslist.org/search/sga?query=surfboard&sort=pricedsc&hasPic=1'
    base_url = 'https://orangecounty.craigslist.org'

    html_content = requests.get(starting_url).text
    ##get parsing tree 
    soup = BeautifulSoup(html_content, "html.parser")

    parse_craigslist_data(soup)
    parse_next_page(soup,base_url)
    

if __name__ == '__main__':
    main()

