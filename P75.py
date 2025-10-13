import requests
from bs4 import BeautifulSoup

r = requests.get("https://detailed.com/50/")
# print(r.text)      #for get requests

# for post requests
# data = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1,
#   }

# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.post(url,headers = headers, json = data)

# print(response.text)


# bs4 module
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
for h in soup.find_all("h2"):
    print(h.text)