import requests


headers = {'Authorization': 'Bearer 9f30aca8b169a2f7d9aac49e0ca00b096bfb31fc'}
endpoint = "http://localhost:8000/api/products/"
# http://localhost:8000/
# session -> post data
# selenium ->
data = {
    "title": "this field is done",
    "price": 13.00
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
