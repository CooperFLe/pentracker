import requests
import json

postings = []
URL = 'https://www.reddit.com/r/pen_swap/new.json?sort=new'
user_agent = {'User-agent': 'Mozilla/5.0'}
last_post = "null"

def get_data():
    r = requests.get(url = URL, headers = user_agent)
    return r.json()

def get_post(data, x):
    return data['data']['children'][x]['data']

def get_postings(data):
    return data['children']

def get_title(post):
    return post['title']

def get_link(post):
    return post['url']

def get_desc(post):
    return post['selftext']

def get_desc_html(post):
    return post['selftext_html']

def get_name(post):
    return post['name']

def get_data_before(name):
    query = URL + "&before=" + name
    r = requests.get(url = query, headers = user_agent)
    return r.json()

def get_post_obj(post_json):
    post = {
            'name': get_name(post_json),
            'title': get_title(post_json),
            'link': get_link(post_json),
            'desc': get_desc(post_json),
            'desc_html': get_desc_html(post_json)
        }
    return post

def get_data_size(data):
    return data['data']['dist']

def process_data(data):
    global last_post
    size = get_data_size(data)
    if size > 0:
        first_post = get_post(data, 0)
        last_post = get_name(first_post)
    for x in range(size):
        post_json = get_post(data, x)
        if("WTS" in get_title(post_json)):
            post = get_post_obj(post_json)
            postings.append(post)

def setup():
    data = get_data()
    process_data(data)

def new_postings():
    data = get_data_before(last_post)
    process_data(data)
