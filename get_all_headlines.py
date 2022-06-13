from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import requests

def getLinksForArticles():
    print("We are starting to gather Article headlines and links.")
    # Website for episodes     
    TAG_URL = "https://order-order.com/page/"
    invalid_url = False
    current_page = 1
    num_added=0
    page_links= []
    
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
                if len(text_clean.split()) > 1:
                    if text_clean.split()[0] == "mdi-timer":
                        date = datetime.strptime(' '.join(text_clean.split()[1:6]), '%d %B %Y @ %H:%M')
                        page_links[num_added][2] = date
                        num_added += 1
                
            current_page += 1
        else:
            invalid_url = True
            
    print("Overall, we found " + str(len(page_links)) + " headlines")
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
    print("exists")
else:
    # file does not exist
    print("File does not exist, generating a new one!")
    df = pd.DataFrame(getLinksForArticles(), columns=['Link', 'Headline', 'Post Time'])
    df.to_pickle('headlines.pkl')