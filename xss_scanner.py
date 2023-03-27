#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def find_vulnerable_link():
    '''
        This should be a spider that looks for a vulnerable link
    '''
    return

def is_vulnerable(soup):

    links = soup.find_all('a')

    returnList = []

    for link in links:
        if "returnPath" in link['href']:

            returnList.append(link['href'])

            return returnList

    return False

# Exploit urls
exploit_url = "http://127.0.0.1/admin"

# SSRF Vulnerability tool
home_url = "https://0a4f00b2046572a7c2757f3a00a50064.web-security-academy.net/"
url = "https://0a4f00b2046572a7c2757f3a00a50064.web-security-academy.net/product?productId=2"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# Check to see if the server is vulnerable
returnList = is_vulnerable(soup)

if (returnList):
    print(returnList)