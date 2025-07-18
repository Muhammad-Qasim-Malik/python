import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches";
    response = requests.get(url)
    
    data = response.json()

    if data["success"] and "data" in data:
        new_data = data["data"]
        if "data" in new_data:
            product_data = new_data["data"]
            for product in product_data:
                print (f"{product['id']}. {product['title']}, {product["category"]}, {product["price"]}")
            # print(new_data["data"][0])


fetch_random_user()