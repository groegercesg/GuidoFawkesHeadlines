from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time

def getHeadlinesForArticles(stop_headline = None):
    print("We are starting to gather Article headlines and links.")
    # Website for episodes     
    TAG_URL = "https://order-order.com/page/"
    invalid_url = False
    current_page = 1
    num_added=0
    page_links= []
    adding_complete = False
    
    while invalid_url is not True:
        page = requests.get(TAG_URL+str(current_page)+"/")
        soup = BeautifulSoup(page.content, "html.parser")
        
        if ((current_page % (250)) == 0):
            print("We are on page " + str(current_page) + ".")
        
        if soup.title.string != "Page not found – Guido Fawkes":
            links = soup.find_all("a", {"class": "link--title"})
            for i in range(0, len(links)):
                if links[i]['href'] not in [a[0] for a in page_links]:
                    page_links.append([links[i]['href'], "", None])
            
            for i in range(0, len(links)):    
                text_clean = links[i].text.lstrip().rstrip().replace('\n', ' ')
                if text_clean != None and text_clean != "\n" and text_clean != "" and text_clean.split()[0] != "mdi-timer":
                    page_links[num_added][1] = text_clean
                    adding_complete = False
                if len(text_clean.split()) > 1:
                    if text_clean.split()[0] == "mdi-timer":
                        date = datetime.strptime(' '.join(text_clean.split()[1:6]), '%d %B %Y @ %H:%M')
                        page_links[num_added][2] = date
                        num_added += 1
                        adding_complete = True
                if adding_complete == True and page_links[num_added-1][1] == stop_headline:
                    invalid_url = True
                    break
                
            current_page += 1
        else:
            invalid_url = True
            
    
    index_of_headline = 0
    for i in range(0, len(page_links)):
        if page_links[i][1] == stop_headline:
            index_of_headline = i
            
    if stop_headline != None:
        print("Overall, we found " + str(len(page_links[:index_of_headline])) + " new headlines")
        return page_links[:index_of_headline]
    else:
        print("Overall, we found " + str(len(page_links)) + " headlines")
        return page_links
    
def getContentForArticles(article_links):
    print("We are now going to gather Article content.")
    for i in range(0, len(article_links)):
        if ((i % int(len(article_links)*0.1)) == 0):
            print("We are on article " + str(i+1) + " out of " + str(len(article_links)) + ".")
        
        link = article_links[i][0]

        # max try count
        trycount = 5  
        while trycount > 0:
            try:
                page = requests.get(link)
                # success
                trycount = 0 
            except ConnectionResetError as ex:
                if trycount <= 0:
                    # done retrying
                    print("Failed to retrieve: " + (link) + "\n" + str(ex))  
                    exit()
                else:
                    # retry
                    trycount -= 1
                    # wait 1/2 second then retry
                    time.sleep(0.5)  

        soup = BeautifulSoup(page.content, "html.parser")

        title = soup.find("v-card-title", {"class": "red accent-4 white--text d-block"}).text.lstrip().rstrip()
        post_time = soup.find("span", {"class": "posted-on blue-grey--text text--darken-4"}).text
        article_links[i][1] = title
        article_links[i][2] = datetime.strptime(post_time, '%B %d %Y @ %H:%M')
        
    print("Overall, we filled in the content for " + str(len(article_links)) + " articles.")
    return article_links
        
def getLinksForArticles(stop_link = None):
    print("We are starting to gather Article links.")
    
    TAG_URL = "https://order-order.com/page/"
    invalid_url = False
    current_page = 1
    page_links= []
    
    while invalid_url is not True:
        
        # max try count
        trycount = 5  
        while trycount > 0:
            try:
                page = requests.get(TAG_URL+str(current_page)+"/")
                # success
                trycount = 0 
            except ConnectionResetError as ex:
                if trycount <= 0:
                    # done retrying
                    print("Failed to retrieve: " + (TAG_URL+str(current_page)+"/") + "\n" + str(ex))  
                    exit()
                else:
                    # retry
                    trycount -= 1
                    # wait 1/2 second then retry
                    time.sleep(0.5)  
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        if ((current_page % (250)) == 0):
            print("We are on page " + str(current_page) + ".")
        
        if soup.title.string != "Page not found – Guido Fawkes":
            links = soup.find_all("a", {"class": "link--title"})
            for individual_link in set([a['href'] for a in links]):
                if stop_link != None and individual_link == stop_link:
                    invalid_url = True
                    break
                else:
                    page_links.append([individual_link, None, None])
                
            current_page += 1
        else:
            invalid_url = True
            
    print("Overall, we found " + str(len(page_links)) + " article links.")
    return page_links

# if .pkl doesn't exist, new run, create one
    # loop from 1 through to when title is wrong, adding to dataframe
    # save as pkl
# else
    # load pkl, get bottom record
    # load 1, if headline == bottom record stop, print up to date
    # otherwise, add to dataframe, continue finding until headline == bottom record
    # save as pkl
my_file = Path("headlines.pkl")
if my_file.is_file():
    # file exists
    original_headlineDetails = pd.read_pickle('headlines.pkl')
    link_additions = getLinksForArticles(original_headlineDetails['Link'][0])
    
    # Iterate through Headline additions, to prepare it into array
    headline_additions_df = pd.DataFrame(getContentForArticles(link_additions), columns=['Link', 'Headline', 'Post Time'])
    new_headlineDetails = pd.concat([headline_additions_df, original_headlineDetails], ignore_index=True)
    
    new_headlineDetails.to_pickle('headlines.pkl')
else:
    # file does not exist
    print("File does not exist, generating a new one!")
    article_links = getLinksForArticles()
    df = pd.DataFrame(getContentForArticles(article_links), columns=['Link', 'Headline', 'Post Time'])
    df.to_pickle('headlines.pkl')