import requests
from bs4 import BeautifulSoup
import html2text

def get_data_from_website(url):
    response = requests.get(url)
    if response.status_code == 500:
        print("Server error")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    html = str(soup)
    html2text_instance = html2text.HTML2Text()
    html2text_instance.images_to_alt = True
    html2text_instance.body_width = 0
    html2text_instance.single_line_break = True
    text = html2text_instance.handle(html)
    try:
        page_title = soup.title.string.strip()
    except:
        page_title = url.path[1:].replace("/", "-")
    meta_description = soup.find("meta", attrs={"name": "description"})
    meta_keywords = soup.find("meta.", attrs={"name": "keywords"})
    if meta_description:
        description = meta_description.get("content")
    else:
        description = page_title
    if meta_keywords:
        meta_keywords = meta_description.get("content")
    else:
        meta_keywords = ""
    metadata = {'title': page_title,
                'url': url,
                'description': description,
                'keywords': meta_keywords}

    return text, metadata

url = "https://www.udemy.com/"  
text_content, metadata = get_data_from_website(url)
print("Text Content:")
print(text_content)
print("\nMetadata:")
print(metadata)
