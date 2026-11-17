import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    # Bu basit bir örnek taslaktır. Gerçek bir botta rate-limiting ve hata yönetimi gerekir.
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        # Etsy fiyat etiketi örneği (seçici değişebilir)
        price = soup.find('span', {'class': 'currency-value'}).text
        return price
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    target_url = "https://www.etsy.com/listing/EXAMPLE"
    print(f"Checking: {target_url}")
    print(f"Price: {get_product_price(target_url)}")
