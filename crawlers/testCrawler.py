import requests
from bs4 import BeautifulSoup
import pandas as pd

####get the desired data from the tree from beautiful soup
def parse_craigs_data(tree):

    results_p = tree.find_all('p',{'class':'result-info'})
    for res_data in results_p:
        ###pull all the relevant data
        price = res_data.findChild('span',{'class':'result-price'})
        area = res_data.findChild('span',{'class':'result-hood'})
        date =  res_data.findChild('time',{'class':'result-date'})
        post_link = res_data.findChild('a',{'class':'result-title hdrlnk'})

        ####if returned data is notnull then get the text from the tag
        if price:
            price = price.text
        if area:
            area = area.text
        if date:
            date = date.text
        if post_link:
            post_link = post_link['href']

        ###get page specifics ###
        post_res = parse_post_details(post_link)

        to_return = [price,area,date]
        to_return.extend(post_res)
        
        yield to_return
        


def parse_post_details(new_link:str):
    to_return = []

    ###get html for new link
    new_html = requests.get(new_link).text
    small_soup = BeautifulSoup(new_html,'html.parser')

    ### get the title and check for location 
    title_span = small_soup.find('span',{'id':'titletextonly'})
    if title_span:
        to_return.append(title_span.text)

    ###get all the extra post attributes
    attrs_p = small_soup.find('p',{'class':'attrgroup'})
    details = []
    if attrs_p:
        children_elements = attrs_p.find_all()
        for item in children_elements[::3]:
            details.append(item.text.split(":"))
    to_return.append(details)

    ###get the number of photos
    thumbnails = small_soup.find('div',{'id':'thumbs'})
    if thumbnails:
        thumbnails = int(len(thumbnails.find_all())/2)
    to_return.append(thumbnails)

    ###get time since post
    time_since = small_soup.find_all('time',{'class':'date timeago'})
    for item in time_since[1:]:
        to_return.append(item['datetime'])
    

    return to_return

    
            
###get the next page by tag
def parse_next_page(tree,root_url:str):
    next_page = tree.find('a',{'class':'button next'})
    if next_page:
        return '{0}{1}'.format(root_url,next_page['href'])
    else:
        return None


def main():
    url_queue = []
    starting_url = 'https://orangecounty.craigslist.org/search/sss?query=surfboard&sort=rel'
    base_url = 'https://orangecounty.craigslist.org'

    url_queue.append(starting_url)

    ###initialize df ####
    # columns = ["title","price","location","date","number_images","time_posted"]
    # new_data = pd.DataFrame(columns = columns)


    while len(url_queue) >= 1:
        html_content = requests.get(url_queue[-1]).text
        ##get parsing tree 
        soup = BeautifulSoup(html_content, "html.parser")

        ###parse the data and get next page
        page_res = parse_craigs_data(soup)


        for res in page_res:
            print(res)
    


        ###find next page and if found insert the new link
        new_url = parse_next_page(soup,base_url)
        if new_url:
            url_queue.insert(0,new_url)
        url_queue.pop()
    print('---Crawling completed---')
            



    
    

if __name__ == '__main__':
    main()

