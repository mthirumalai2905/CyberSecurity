import requests
from bs4 import BeautifulSoup

def web_scraper():
    try:
        # Ask the user to enter the domain
        url = input("Enter the URL you want to scrape: ")

        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Customize the code below to extract the desired information
        # For example, let's extract all the links from the webpage
        links = soup.find_all('a')

        # Store the extracted links in a file
        with open("scraped_links.txt", "w") as file:
            for link in links:
                href = link.get('href')
                if href:
                    file.write(href + "\n")

        print("Scraped data has been saved in 'scraped_links.txt'.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    web_scraper()
