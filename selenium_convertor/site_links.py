# !/usr/bin/python
import json

from bs4 import BeautifulSoup
import requests as req

import time

class WebSiteLinks():
    def __init__(self,url):
        self.base_url = url
        self.tags =[]
        self.links =[]


    def create_site_tree(self, url=None):
        try:
            resp = req.get(self.base_url + url)
            time.sleep(2)
            soup = BeautifulSoup(resp.text, 'lxml')
            title = soup.find('title')
            #print("Title :" + title.string," Url: " + self.base_url+url)
            if title:
                link = {"title":title.string,"url":self.base_url+url}
                self.links.append(link)
                for tag in soup.findAll("a", {'href': True}):
                    if '/' in tag["href"] \
                            and 'login' not in tag["href"]\
                            and tag["href"] not in self.tags:
                        self.tags.append(tag["href"])
                        self.create_site_tree( url=tag["href"])
        except Exception as e:
            print(e)


site_links = WebSiteLinks('https://www.bankhapoalim.co.il')
#site_links = WebSiteLinks('https://www.makorrishon.co.il/')
site_links.create_site_tree( url="")
print(site_links.links)
json.dump(site_links.links, "site_links.json")
