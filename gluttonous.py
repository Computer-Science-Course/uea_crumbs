from bs4 import BeautifulSoup
import requests

url = "https://www3.uea.edu.br/"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=9fe6d52b483ec09d2929859d29a6f1c8",
    "Host": "www3.uea.edu.br",
    "Referer": "https://www.google.com/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Specify UTF-8 encoding when writing to a file
    with open("output.html", "w", encoding="utf-8") as file:
        # Write the response content to the file
        file.write(response.text)
else:
    print("Failed to retrieve the content:", response.status_code)
    exit(1)

html = response.text
soup = BeautifulSoup(html, 'lxml', parser='html.parser')

a_tags = soup.select('.carousel-inner .item a')

for key, a_tag in enumerate(a_tags):
    url = a_tag['href']
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        news_html = response.text
    else:
        print("Failed to retrieve the content:", response.status_code)
        exit(1)
