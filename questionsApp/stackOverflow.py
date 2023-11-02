
import requests
from requests_html import HTML
import time
import pandas as pd
import json

# https://stackoverflow.com/questions/tagged/python?tab=Votes

base_url = "https://stackoverflow.com/questions/tagged/"
tag = "python"
query_filter = "Votes"
url = f"{base_url}{tag}?tab={query_filter}"
print(url)

r = requests.get(url)
html_str = r.text
html = HTML(html=html_str)

question_summaries = html.find(".s-post-summary")
# print(question_summaries)

question_summaries[0].text

key_names = ['question', 'metrics', 'tags']
classes_needed = ['.s-link', '.s-post-summary--stats', '.post-tag']
this_question_element = question_summaries[0]
this_question_element.find('.s-link', first=True).text
this_question_element.find('.s-post-summary--stats', first=True).text.replace('\n', ' ')


def clean_scraped_data(text, keyname=None):
    if keyname == 'metrics':
        return text.replace('\n', ' ')
    if keyname == 'post-tag':
        return text.replace('\n', ',')
    return text


datas = []

for q_el in question_summaries:
    question_data = {}
    for i, _class in enumerate(classes_needed):
        sub_el = q_el.find(_class, first=True)
        keyname = key_names[i]
        question_data[keyname] = clean_scraped_data(sub_el.text, keyname=keyname)
    datas.append(question_data)
    
def parse_tagged_page(html):
    question_summaries = html.find(".s-post-summary")
    key_names = ['question', 'metrics', 'tags']
    classes_needed = ['.s-link', '.s-post-summary--stats', '.post-tag']
    datas = []
    for q_el in question_summaries:
        question_data = {}
        for i, _class in enumerate(classes_needed):
            sub_el = q_el.find(_class, first=True)
            keyname = key_names[i]
            question_data[keyname] = clean_scraped_data(sub_el.text, keyname=keyname)
        datas.append(question_data)
    return datas



def extract_data_from_url(url):
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return[]
    html_str = r.text
    html = HTML(html=html_str)
    datas = parse_tagged_page(html)
    return datas
    
  
def scrape_tag(tag = "python", query_filter = "Votes", max_pages=50, pagesize=50):
    base_url = "https://stackoverflow.com/questions/tagged/"
    datas = []
    for p in range(max_pages):
        page_num = p + 1
        url = f"{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}"
        datas += extract_data_from_url(url)
        time.sleep(1.2)
    return datas

datas = scrape_tag(tag="python")
# print(datas)
json_data = json.dumps(datas, sort_keys=True, indent=4)
print(json_data)


# len(datas)

# df = pd.DataFrame(datas)
# df.head()

# df.shape

# df.to_csv("Pythontwo.csv", index=False)




