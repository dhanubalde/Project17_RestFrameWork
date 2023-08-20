import requests
# from getpass import getpass
# auth_endpoint = "http://localhost:8000/api/products/auth/"
# password = getpass()

# auth_response = requests.get(
#     auth_endpoint, json={"username": "staff", "password": password})
# print(auth_response.json())

endpoint = "http://localhost:8000/api/products/1/"

get_response = requests.get(endpoint)
print(get_response.json())
