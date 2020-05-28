import requests, bs4
from val_info import get_value

def get_data():
    response = requests.get("http://127.0.0.1/dashboard/test.html")
    data = response.text
    return data

def to_parse_title(data):
    bs = bs4.BeautifulSoup(data, "html.parser")
    a_list = bs("a")
    a_item = a_list[0]
    link = a_item.text
    return link

print(to_parse_title(get_data()))
get_value(to_parse_title(get_data()))

# html = open("response.text").read()
# html = open("test.html").read()
# html = open(requests.get("http://127.0.0.1/dashboard/test.html")).read()
# bs = bs4.BeautifulSoup(html, "html.parser")
# bs = bs4.BeautifulSoup(data, "html.parser")
# get_value(bs)
# a_list = bs("a")
# a_item = a_list[0]
# a_item.text

# get_value(a_list)
# get_value(a_item)
# get_value(a_item.text)
# get_value(a_item["href"])


