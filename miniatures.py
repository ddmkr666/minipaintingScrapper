'''
reddit scrapper for saving daily top posts from /r/minipainting
'''
import os
from datetime import date
import urllib.request
import praw

reddit = praw.Reddit(client_id='HptwS1GEQY9Mbg',
                     client_secret='vGF66jp-5xRqFwRMYaWZZsiuw0I',
                     user_agent='scrap')
current_path = os.getcwd()
today = date.today()
daily_directory = (current_path + "\\" + today.strftime("%d.%m"))
daily_file = str(daily_directory + '\\list.txt')
top_posts = reddit.subreddit('minipainting').top('day', limit=10)
top_list = 1

try:
    os.mkdir(daily_directory)
except:
    pass

for post in top_posts:
    url = str(post.url)
    with open(daily_file, 'a') as file:
        file.write(str(top_list) + ' http://reddit/com/' + post.permalink
                   + '\n')
    print('\nDownloading file: ' + str(post.permalink))
    if url.endswith('jpg'):
        extension = 'jpg'
        urllib.request.urlretrieve(url, os.path.join(daily_directory,
                                   f"{top_list} {post.title}.{extension}"))
    elif url.endswith('jpeg'):
        extension = 'jpeg'
        urllib.request.urlretrieve(url, os.path.join(daily_directory,
                                   f"{top_list} {post.title}.{extension}"))
    elif url.endswith('png'):
        extension = 'png'
        urllib.request.urlretrieve(url, os.path.join(daily_directory,
                                   f"{top_list} {post.title}.{extension}"))
    top_list += 1