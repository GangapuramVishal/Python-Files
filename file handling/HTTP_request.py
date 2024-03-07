import requests

r = requests.post('https://www.linkedin.com/feed/ post',data = {'name': 'bob'})
print(r.request)