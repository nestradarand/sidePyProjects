import requests
from bs4 import BeautifulSoup

####get the desired data from the tree from beautiful soup
def parse_craigslist_data(tree):

    results_p = tree.find_all('p',{'class':'result-info'})
    for i, res_data in enumerate(results_p):
        print('Result:{0}'.format(i))
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

###get the next page by tag
def parse_next_page(tree,root_url:str):
    next_page = tree.find('a',{'class':'button next'})
    if next_page:
        return '{0}{1}'.format(root_url,next_page['href'])
    else:
        return None


def main():
    url_queue = []
    starting_url = 'https://orangecounty.craigslist.org/search/sga?query=surfboard&sort=pricedsc&hasPic=1'
    base_url = 'https://orangecounty.craigslist.org'

    url_queue.append(starting_url)

    while len(url_queue) >= 1:
        html_content = requests.get(url_queue[-1]).text
        ##get parsing tree 
        soup = BeautifulSoup(html_content, "html.parser")
        ###parse the data and get next page
        parse_craigslist_data(soup)
        ###find next page and if found insert the new link
        new_url = parse_next_page(soup,base_url)
        if new_url:
            url_queue.insert(0,new_url)
        url_queue.pop()
    print('---Crawling completed---')
            



    
    

if __name__ == '__main__':
    main()

