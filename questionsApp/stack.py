##Youtube example 

import requests
from bs4 import BeautifulSoup
import json
import pprint


# res  = requests.get("https://stackoverflow.com/questions")

res = requests.get("https://stackoverflow.com/questions/tagged/python")

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    "questions": []
}

questions = soup.select(".s-post-summary")
# questions = soup.select("s-post-summary--content-title")
# print(questions[0].attrs)
# print(questions[0].select('.s-post-summary--content-title'))
# print(questions[0].select('.s-link'))
# print(questions[0].select_one('.s-link').getText())

for que in questions:
    q = que.select_one('.s-link').getText()
    link = que.select_one('.s-link')
    vote_count = que.select_one('.s-post-summary--stats-item-number').getText()
    questions_data['questions'].append({
        "question": q, 
        "vote_count": vote_count,
        "link": link
    })

    json_data = json.dumps(questions_data)

    print(json_data)
   
    # print(q)
    # print(l)
    # print(vote_count)
    
    
     # frequent = que.select_one('.s-post-summary--stats-item-is-supernova')
    # answer = que.select_one('.s-post-summary--stats-item-has-answers')
    # views = que.select_one("s-post-summary--stats-item-number").attrs
    # views = que.select_one('.s-post-summary--stats-item-number-views')
    # v = que.select_one('.s-post--stats-item-has-answers')
    # print(v)
    # print(answer)
    
    
    
    # print(q)
    # print(vote_count[0].attrs)
    # print(l)
    # print(views)
    # print(answer)
    # print(frequent)
    # print(questions)
    
    



