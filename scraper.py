import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def scrape_website(base_url):
    page_url = base_url  # Start with the user-provided URL
    all_data = []  # To store the scraped data
    page_count = 0  # Counter for pages scraped

    print("\nStarting scraping process...\n")

    # Initialize progress bar
    with tqdm(desc="Scraping Pages", unit="page") as pbar:
        while True:
            print(f"Scraping {page_url}...")
            try:
                # Fetch the page content
                response = requests.get(page_url)
                response.raise_for_status()  # Check for HTTP request errors
            except requests.exceptions.RequestException as e:
                print(f"Error fetching page: {e}")
                break

            soup = BeautifulSoup(response.content, "html.parser")

            # Automatically detect the structure and scrape data
            data = []
            if soup.find("table"):
                print("Detected table structure.")
                table = soup.find("table")
                rows = table.find_all("tr")
                headers = [header.text.strip() for header in rows[0].find_all("th")]
                for row in rows[1:]:
                    values = [cell.text.strip() for cell in row.find_all("td")]
                    data.append(dict(zip(headers, values)))
            elif soup.find_all("article"):
                print("Detected article structure.")
                articles = soup.find_all("article")
                for article in articles:
                    title = article.find("h2").text.strip() if article.find("h2") else "N/A"
                    description = article.find("p").text.strip() if article.find("p") else "N/A"
                    data.append({"Title": title, "Description": description})
            elif soup.find_all("li"):
                print("Detected list structure.")
                items = soup.find_all("li")
                for item in items:
                    content = item.text.strip()
                    data.append({"Content": content})
            else:
                print("Could not automatically detect structure. Skipping this page.")
                break

            all_data.extend(data)

            # Save the data to a CSV file after each page
            df = pd.DataFrame(all_data)
            df.to_csv("dynamic_scraped_data.csv", index=False)

            # Find the "Next" button to get the next page URL
            next_button = soup.find("a", text="Next") or soup.find("li", class_="next")
            if next_button:
                next_page = next_button["href"]
                if not next_page.startswith("http"):  # Handle relative URLs
                    next_page = "/".join(base_url.split("/")[:-1]) + "/" + next_page
                page_url = next_page
            else:
                break  # Exit if no "Next" button is found

            # Update the progress bar and page count
            page_count += 1
            pbar.update(1)

    print(f"\nScraping completed! {page_count} pages scraped.")
    print("All data saved to 'dynamic_scraped_data.csv'.")

if __name__ == "__main__":
    # Ask for the URL input
    user_url = input("Enter the URL of the website you want to scrape: ").strip()
    scrape_website(user_url)
