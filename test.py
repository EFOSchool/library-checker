import requests

def test_website_blocking(url):
    try:
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            print("Request successful. You were able to access the website.")
        else:
            print("Request unsuccessful. The website may be blocking your requests.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url_to_test = "https://example.com"  # Replace with the URL you want to test
    test_website_blocking(url_to_test)
