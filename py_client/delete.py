import requests


products = int(input("what is your product id :"))
try:
    product_id = int(products)
except:
    product_id = None
    print(f'{product_id} is not a valid product')
if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
