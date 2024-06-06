#!/usr/bin/python3
"""
Function to print the titles of the first 10 hot posts in a given subreddit
"""
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        
        for post in posts:
            print(post.get("data", {}).get("title", None))
    except requests.RequestException:
        print(None)

