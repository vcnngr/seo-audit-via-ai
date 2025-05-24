import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    data = {
        "meta_tags": "",
        "headings": [],
        "text": "",
        "links": []
    }

    try:
        response = requests.get(url, verify=False, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup(["script", "style"]):
            tag.decompose()

        for tag in soup.find_all(True):
            if "style" in tag.attrs:
                del tag.attrs["style"]

        data["meta_tags"] = str(soup.find_all("meta"))
        data["headings"] = [tag.get_text(strip=True) for tag in soup.find_all(["h1", "h2", "h3"])]
        text_content = soup.get_text(separator=' ', strip=True)
        data["text"] = text_content[:3000]
        data["links"] = [a.get("href") for a in soup.find_all("a", href=True)]

    except Exception as e:
        data["text"] = f"Errore durante lo scraping del sito: {str(e)}"

    return data
