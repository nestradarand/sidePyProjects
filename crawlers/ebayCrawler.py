import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_ebay_page(new_tree):
    ###getting the post 
    posts = new_tree.find_all('div',{'class':'s-item__info clearfix'})
    for post in posts:
        post_link = post.find('a')
        if post_link:
            yield parse_ebay_post_info(post_link['href'])


def parse_ebay_post_info(new_url:str):
    ###return object
    to_return = []

    ###grab the html
    html_stuff = requests.get(new_url).text
    small_soup = BeautifulSoup(html_stuff,'html.parser')

    ##get the title
    title = small_soup.find('h1',{'id':'itemTitle'})
    if title:
        title = title.text.lstrip('Details about  ')
    to_return.append(title)
    
    ###get the price 
    price = small_soup.find('span',{'id':'prcIsum'})
    if price:
        price = price['content']
    to_return.append(price)

    ###get the currency
    currency = small_soup.find('span',{'itemprop':'priceCurrency'})
    if currency:
        currency = currency['content']
    to_return.append(currency)

    ###location
    location = small_soup.find('span',{'itemprop':'availableAtOrFrom'})
    if location:
        location = location.text 
    to_return.append(location)

    ###condition 
    condition = small_soup.find('div',{'id':'vi-itm-cond'})
    if condition:
        condition = condition.text
    to_return.append(condition)

    ###number photos
    photo_list = small_soup.find('ul',{'class':'lst icon'})
    num_photos = None
    if photo_list:
        num_photos = photo_list.find_all('li')
        if num_photos:
            num_photos = len(num_photos)

    to_return.append(num_photos)

    ###seller rating 
    rating = small_soup.find('div',{'id':'si-fb'})
    if rating:
        rating = rating.text.split()[0]
    to_return.append(rating)

    ###get area where sold 
    area = small_soup.find('span',{'itemprop':'areaServed'})    
    if area:
        area = area.text.rstrip().split('|')[0].strip(r'\n\t\t\t').strip('\xa0\n').lstrip()
    to_return.append(area)

    ###check to see if returns are accepted 
    returns = small_soup.find('span',{'id':'vi-ret-accrd-txt'})
    if returns:
        returns = returns.text 
        if 'does not' in returns:
            returns = 0
        else:
            returns = 1
    to_return.append(returns)

    return to_return

    


def parse_next_ebay_page(tree):
    next_page = tree.find('a',{'class':'pagination__next'})
    if next_page:
        return next_page['href']
    else:
        return None

def main():

    #starting url 
    start_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR11.TRC1.A0.H0.Xsurboard.TRS0&_nkw=surboard&_sacat=0'

    url_queue = [start_url]

    columns = ["title","price","location","currency","condition","number_images",
                "shipment_zone","accepts_returns"]
    new_data = pd.DataFrame(columns = columns)

    while len(url_queue) >= 1:
        ###get the page's html
        html_content = requests.get(start_url).text
        soup = BeautifulSoup(html_content, "html.parser")

        ###for each post on the page do something
        for res in parse_ebay_page(soup):
            temp_dict = {
                'title' : res[0],
                'price' : res[1],
                'location' : res[3],
                'currency' : res[2],
                'condition' : res[4],
                'number_images' : res[5],
                'shipment_zone' :res[6],
                'accepts_returns' : res[7]
            }
            new_data = new_data.append(temp_dict,ignore_index = True)

        ###get the next page
        next_page = parse_next_ebay_page(soup)

        if next_page:
            url_queue.insert(0,next_page)
        url_queue.pop()
    new_data.to_csv("ebayOutput.csv",index = False)

        
    print('----Crawling completed----')





if __name__ == '__main__':
    main()