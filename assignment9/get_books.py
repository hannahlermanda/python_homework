from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def scrape_dl(query):
    base_url = f"https://durhamcounty.bibliocommons.com/v2/search?query={query}&searchType=smart"
    driver.get(base_url)
    sleep(2)

    #Empty list
    results = []
    #Start on the first page
    page = 1

    while True:
        print(f"Scraping page {page}...")
        items = driver.find_elements(By.CSS_SELECTOR, 'li.row.cp-search-result-item')

        for item in items:
            try:
                #Finding the title
                title_elem = item.find_element(By.CSS_SELECTOR, 'h2.cp-title .title-content')
                title = title_elem.text.strip()
            except:
                title = ''

            #Find the author(s)
            author_elems = item.find_elements(By.CSS_SELECTOR, 'a.author-link')
            authors = [ae.text.strip() for ae in author_elems if ae.text.strip()]
            #If there's more than one author
            author_text = '; '.join(authors)

            try:
                #Find the format of the book
                fmt_elem = item.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
                fmt_year = fmt_elem.text.strip()
            except:
                fmt_year = ''

            #Append the results to the dictionary
            results.append({
                'Title': title,
                'Author': author_text,
                'Format-Year': fmt_year
            })

        #Attempt to go to the next page
        try:
            next_page_link = driver.find_element(
                By.CSS_SELECTOR,
                'li.cp-pagination-item.pagination__next-chevron a.pagination-item__link'
            )
            next_url = next_page_link.get_attribute('href')
            if not next_url:
                break

            #Get the next page and add 1 (Iterate through the pages)
            driver.get(next_url)
            page += 1
            sleep(3)
        except:
            #No more pages
            break  

    #Print and return the dataframe
    df = pd.DataFrame(results)
    return df

#Task 4: Write out the Data
#Run
if __name__ == '__main__':
    df_results = scrape_dl('learning spanish')
    print(df_results)
    df_results.to_json('durham_search_results.json', orient='records', force_ascii=False)
    df_results.to_csv('get_books.csv', index=False)
    driver.quit()