import requests
from bs4 import BeautifulSoup

####get the desired data from the tree from beautiful soup
def parse_main_page_data(tree):

    results_p = tree.find_all('p',{'class':'result-info'})
    for i, res_data in enumerate(results_p):
        print('Result:{0}'.format(i))
        price = res_data.findChild('span',{'class':'result-price'})
        area = res_data.findChild('span',{'class':'result-hood'})
        date =  res_data.findChild('time',{'class':'result-date'})
        post_link = res_data.findChild('a',{'class':'result-title hdrlnk'})
        ####deal with none type in the event of text property
        if price:
            print(price.text)
        if area:
            print(area.text)
        if date:
            print(date.text)
        if post_link:
            parse_post_details(post_link['href'])


def parse_post_details(new_link:str):
    new_html = requests.get(new_link).text
    small_soup = BeautifulSoup(new_html,'html.parser')

    attrs_p = small_soup.find('p',{'class':'attrgroup'})
    if attrs_p:
        children_elements = attrs_p.find_all()
        for i,item in enumerate(children_elements):
            if i % 3 == 0:
                print(item.text.split(':'))
            
###get the next page by tag
def parse_next_page(tree,root_url:str):
    next_page = tree.find('a',{'class':'button next'})
    if next_page:
        return '{0}{1}'.format(root_url,next_page['href'])
    else:
        return None


def main():
    url_queue = []
    starting_url = 'https://orangecounty.craigslist.org/search/sga?query=surf&sort=pricedsc&hasPic=1'
    base_url = 'https://orangecounty.craigslist.org'

    url_queue.append(starting_url)

    while len(url_queue) >= 1:
        html_content = requests.get(url_queue[-1]).text
        ##get parsing tree 
        soup = BeautifulSoup(html_content, "html.parser")
        ###parse the data and get next page
        parse_main_page_data(soup)
        ###find next page and if found insert the new link
        new_url = parse_next_page(soup,base_url)
        if new_url:
            url_queue.insert(0,new_url)
        url_queue.pop()
    print('---Crawling completed---')
            



    
    

if __name__ == '__main__':
    main()

