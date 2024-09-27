import requests
from main_content_extractor import MainContentExtractor

# Get HTML using requests
url = "https://developer.mozilla.org/en/docs/Web"
response = requests.get(url)
response.encoding = 'utf-8'
content = response.text

def scrape_data(query):
    url = "https://www.zigwheels.my/latest-cars/"+query
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text
    extracted_markdown = MainContentExtractor.extract(content, output_format="markdown")
    print(extracted_markdown)
    return extracted_markdown
    
#url = "https://www.wapcar.my/cars/honda"
#response = requests.get(url)
#response.encoding = 'utf-8'
#content = response.text
#extracted_markdown = MainContentExtractor.extract(content)
#print(extracted_markdown)


# Get HTML with main content extracted from HTML
#extracted_html = MainContentExtractor.extract(content)

# Get HTML with main content extracted from Markdown
#extracted_markdown = MainContentExtractor.extract(content, output_format="markdown")
