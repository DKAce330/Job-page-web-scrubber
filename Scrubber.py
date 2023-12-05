#import libraries
from splinter import Browser
from bs4 import BeautifulSoup

#welcome the user (this is for testing only)
print("Hello user!")

#Need to import the titles
title_list = ("Resources/Title_list.md")
titles=[]
with open(title_list, "r") as f:
    for line in f:
        # Process each line as a title
        title = line.strip()
        titles.append(title)

#Print a confirmation
print(f"We are searching for the following jobs:")
for t in titles:
    print(t)

#Need to import the websites
site_list= ("Resources/Website_list.md")
sites=[]
with open(site_list, "r") as f:
    for line in f:
        # Process each line as a title
        site = line.strip()
        sites.append(site)

#Print a confirmation
print("On these websites: ")
for s in sites:    
    print(s)

#BeautufulSoup setup
def surfer():
    browser = Browser('chrome')
    url = ""
    browser.visit(url)
    html= browser.html
    soup= BeautifulSoup(html,'html.parser')

#lets make lists of urls for each website


#Scrub data from links


#Compile the data, process it and create a .txt


