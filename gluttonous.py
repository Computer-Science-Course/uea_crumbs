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
        news_html = response.text
        news_soup = BeautifulSoup(news_html, 'lxml', parser='html.parser')
        raw_datetime = news_soup.select('.panel .panel-body h5')[0].text
        raw_title = news_soup.select('.panel .panel-body h2')[0].text
        raw_src_image = news_soup.select('.panel .panel-body .container-fluid .row img')[0]['src']
        raw_paragraphs = news_soup.select('.panel .panel-body > p')
        raw_related_links_title = news_soup.select('.panel .panel-body panel-group list-group-item > list-group-item-heading > p')
        raw_related_links_ancor = news_soup.select('.panel .panel-body panel-group panel-default > a')

        paragraphs = [raw_paragraph.text for raw_paragraph in raw_paragraphs if raw_paragraph.text]
        print(raw_related_links_title)
        # related_links = [
        #     { 'title': raw_related_link_title.text, 'href': raw_related_link_ancor, }
        #     for raw_related_link_title, raw_related_link_ancor in zip(raw_related_links_title, raw_related_links_ancor)
        # ]

        # print(raw_datetime, raw_title, raw_src_image, paragraphs, related_links)
    else:
        print("Failed to retrieve the content:", response.status_code)
        exit(1)
