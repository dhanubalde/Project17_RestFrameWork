import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# application programming interfaces
get_response = requests.post(
    endpoint, json={"title": "abc123", "content": "Hello World", "price": 123})
print(get_response.json())

# print(get_response.headers)
# print(get_response.text)  # print out the response or source code
# print(get_response.status_code)  # print out the status code
# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0','X-Amzn-Trace-Id': 'Root=1-64c335ed-6423b4dd22bc78c271dbc1d6'}, 'json': None, 'method': 'GET', 'origin': '110.54.223.184', 'url': 'https://httpbin.org/anything'}
