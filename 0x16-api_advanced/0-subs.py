#!/usr/bin/python3
"""subs number from api"""
import requests


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "khaledxab"}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit),
                            headers=headers)
    if response.status_code == 404:
        return 0
    subs = response.json().get("data").get("subscribers")
    return subs
