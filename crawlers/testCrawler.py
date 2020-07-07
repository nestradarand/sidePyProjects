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
        temp = {}
        for item in children_elements[::3]:
            try:
                splits = item.text.split(":")
                temp[splits[0]] = splits[1]
            except:
                continue
        details.append(temp)
    to_return.append(details)

    ###get the number of photos
    thumbnails = small_soup.find('div',{'id':'thumbs'})
    if thumbnails:
        thumbnails = int(len(thumbnails.find_all())/2)
    to_return.append(thumbnails)

    ###get time since post
    time_posted = small_soup.find('p',{'id':'display-date'}).find('time',{'class':'date timeago'})
    if time_posted:
        time_posted = time_posted['datetime']
    to_return.append(time_posted)
    

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
    columns = ["title","price","location","date","condition","make / manufacturer",
                "model name / number","size / dimensions","number_images","time_posted"]
    new_data = pd.DataFrame(columns = columns)

    
    while len(url_queue) >= 1:
        html_content = requests.get(url_queue[-1]).text

        ##get parsing tree 
        soup = BeautifulSoup(html_content, "html.parser")

        ###parse the data and get next page
        page_res = parse_craigs_data(soup)

        for res in page_res:
            temp_dict = {}
            if len(res[4]) > 0:
                temp_dict.update({key:value for key,value in res[4][0].items()})

            temp_dict.update({
                'price' : res[0],
                'location' : res[1],
                'date' : res[2],
                'title' : res[3],
                'number_images' : res[5],
                'time_posted' : res[6]
            })
            new_data = new_data.append(temp_dict,ignore_index = True)
                





        ###find next page and if found insert the new link
        new_url = parse_next_page(soup,base_url)
        if new_url:
            url_queue.insert(0,new_url)
        url_queue.pop()

        ###write the data to a csv
        new_data.to_csv("craigs_data.csv",index = False)
    print('---Crawling completed---')
            



    
    

if __name__ == '__main__':
    main()

