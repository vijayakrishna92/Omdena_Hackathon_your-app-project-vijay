from seleniumbase import Driver
from crewai_tools import tool
import time



@tool
def search_and_scrape(prompt: str) -> str:
    """
    A tool to scrape web data based on the given query.

    Parameters:
    - prompt (str): The search query for web scraping.

    Returns:
    - list of dict: The collected data including URLs and full page content.
    """
    # Set up the web driver
    driver = Driver(browser="chrome")
    
    # Perform a Google search
    search_url = f"https://www.google.com/search?q={prompt.replace(' ', '+')}"
    driver.get(search_url)
    
    # Wait for the page to load (you can increase sleep time if necessary)

    # Collect the first few search results
    links = driver.find_elements("css selector", "a")
    urls = []
    for link in links:
        href = link.get_attribute("href")
        if href and "http" in href and "google" not in href:
            urls.append(href)
        if len(urls) >= 2:  # Limiting to the first 3 results
            break
    
    contents = []
    
    for url in urls:
        # Navigate to the page
        driver.get(url)
        time.sleep(5)
        # Scrape the content
        content = driver.find_element("tag name", "body").text
        contents.append({"url": url, "content": content})
        with open("links.txt", 'a') as file:
            file.write(url + '\n')
    
    # Close the web driver
    driver.quit()
    
    return contents