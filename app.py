import requests
import urllib3
from bs4 import BeautifulSoup



# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://libraries.uc.edu/about/hours-locations.html"

# Disable SSL certificate verification and suppress warning
page = requests.get(url, verify=False)

# Check if the request was successful
if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")

    # finding all titles of libraries
    libraries = soup.find_all("div", class_="accordion component")

    # finding the title in all of the components
    for library in libraries:
        name = library.find("span", class_="title")
        print(name.text)
else:
    print(f"Failed to fetch URL: HTTP status code {page.status_code}")
