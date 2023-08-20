import requests
products = int(input("Search Product Id: "))
search_id = products
endpoint = f"http://localhost:8000/api/products/{search_id}/"

get_response = requests.get(endpoint)
print(get_response.json())
