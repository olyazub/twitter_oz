import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def findall(key):
    """
    (str) -> (str)
    Returns screen name and  additional info about a user,
    if it's sub-key in users
    """
    acct = input('\nEnter Twitter Account:')
    if (len(acct) < 1):
        return
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '200'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    lst = []
    for u in js['users']:
        print()
        if key not in u:
            print("Sorry, can't find such information")
            continue
        lst.append([u['screen_name'], u[key]])
    return lst

