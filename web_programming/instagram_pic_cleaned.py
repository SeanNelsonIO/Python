from datetime import datetime

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = input("Enter image url: ").strip()
    print(f"Downloading image from {url} ...")
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    image_url = soup.find("meta", {"property": "og:image"})["content"]
    image_data = requests.get(image_url).content
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
    with open(file_name, "wb") as fp:
        fp.write(image_data)
    print(f"Done. Image saved to disk as {file_name}.")
