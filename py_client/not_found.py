import requests
products = int(input("Enter Product Id:"))
products_id = products
endpoint = f"http://localhost:8000/api/products/{products_id}/"


get_response = requests.get(endpoint)
print(get_response.json())
