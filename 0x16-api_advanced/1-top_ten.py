#!/usr/bin/python3
"""get first 10 hot posts"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "khaledxab"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    posts = response.json().get('data')
    """children titles"""
    for sub in posts.get('children'):
        print(sub.get('data').get('title'))
