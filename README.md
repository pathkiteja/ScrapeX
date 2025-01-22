# Automated Web Scraping 

> A Python-based web scraper that automatically detects and extracts data (from tables, articles, or lists), paginates through “Next” links, and saves the results in a CSV file for analysis.

---

## Project Overview

This repository contains a Python script that scrapes data from web pages by intelligently detecting common HTML structures (tables, articles, or lists). It also follows “Next” links to scrape multiple pages automatically, storing all collected data in a CSV file (`dynamic_scraped_data.csv`).

Typical use cases:
- Gathering product data from paginated e-commerce sites.  
- Scraping news articles from multi-page blog listings.  
- Collecting tabular information (e.g., leaderboard, rankings, or financial data) that span multiple pages.

---

## Demo Video

Below is a short screen recording demonstrating how to use and run the scraper:

[Click here to watch the demo video](Screen Recording 2025-01-21 170805)

---
 Usage
     Run the scraper


      python scraper.py
      
 Enter the target URL
---> When prompted, provide the URL of the website you want to scrape. The script will:

     Identify whether the page has a table, article, or list structure.
     Extract relevant data from each item.
 Write/append the data to dynamic_scraped_data.csv.
    Look for a “Next” link or button, then continue scraping subsequent pages until no more “Next” links are found.
Check the CSV output
    Once the script finishes, a file named dynamic_scraped_data.csv will appear in the same directory. This file contains all scraped data.

Important: Always verify that your scraping activities comply with the target site’s Terms of Service and/or Robots.txt. Use this tool responsibly.
---
Features
   --->   Automatic HTML Structure Detection:
          Detects tables, articles, or lists in the HTML for data extraction.

   --->   Pagination Handling:
          Automatically follows “Next” or similarly labeled links to scrape multiple pages.

   --->   Progress Feedback:
          Utilizes tqdm for a progress bar in the terminal.

   =-->   CSV Output:
          Writes all data to dynamic_scraped_data.csv at every page iteration, ensuring you always have the most recent data.
---

Contributing
1) Fork the project
2) Create a new feature branch (git checkout -b feature/new-feature)
3) Commit your changes (git commit -m 'Add new feature')
4) Push to the branch (git push origin feature/new-feature)
5) Create a new Pull Request on GitHub
