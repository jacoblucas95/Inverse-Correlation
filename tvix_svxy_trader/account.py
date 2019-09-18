import time
import urllib
import requests
import json
from splinter import Browser
from selenium import webdriver
from config import client_id, username, password

# path to chrome driver
executable_path = {'executable_path': "/usr/local/bin/chromedriver"}
browser = Browser('chrome', **executable_path, headless=False)

# url components
method = 'GET'
url = 'https://auth.tdameritrade.com/auth?'
client_code = client_id + '@AMER.OAUTHAP'
payload = {'response_type': 'code', 'redirect_uri': 'https://127.0.0.1', 'client_id': client_code}

# build url
built_url = requests.Request(method, url, params=payload).prepare()
built_url = built_url.url

# go to url
browser.visit(built_url)

# define login credentials
payload = {'username': username, 'password': password}

# fill out login
browser.find_by_id('username').first.fill(payload['username'])
browser.find_by_id('password').first.fill(payload['password'])
browser.find_by_id('accept').first.click()

# accept terms and conditions
browser.find_by_id('accept').first.click()

# allow page to load
time.sleep(1)
new_url = browser.url

# grab url and parse
parse_url = urllib.parse.unquote(new_url.split('code=')[1])

# close browser
browser.quit()

# authorization
endpoint = 'https://api.tdameritrade.com/v1/oauth2/token'
headers = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {'grant_type':'authorization_code',
           'access_type': 'offline',
           'code': parse_url,
           'client_id': client_id,
           'redirect_uri': 'https://127.0.0.1'}

# post data for token
authReply = requests.post(endpoint, headers=headers, data=payload)

# convert from json to dict
content = authReply.json()

# access token request header
access_token = content['access_token']
headers = {'Authorization': "Bearer {}".format(access_token)}

# accounts endpoint
endpoint = 'https://api.tdameritrade.com/v1/accounts'
content = requests.get(url = endpoint, headers = headers)
data = content.json()
print(data)
