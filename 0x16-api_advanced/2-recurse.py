#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """return list of titles of all hot posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    limits = {
            "after": after,
            "count": count,
            "limit": 10
            }
    response = requests.get(url, headers=headers, limits=limits, allow_redirects=False)    # noqa
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
