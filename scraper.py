import requests, sys
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_headings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = soup.find_all('h1')
    return [heading.text.strip() for heading in headings]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    print(url)
    page_content = fetch_page(url)
    
    if page_content:
        headings = parse_headings(page_content)
        print("Headings found:", headings)
    else:
        print("Failed to retrieve the webpage.")
