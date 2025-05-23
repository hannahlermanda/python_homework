#Task 6: Scraping Structured Data

#top 10 security risks 
#<li><a href="https://owasp.org/Top10/A01_2021-Broken_Access_Control/"><strong>A01:2021-Broken Access Control</strong></a> moves up from the fifth position; 94% of applications were tested for some form of broken access control. The 34 Common Weakness Enumerations (CWEs) mapped to Broken Access Control had more occurrences in applications than any other category.</li>
#within <li><a><strong>

from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def scrape_owasp_top_10():
    url = "https://owasp.org/www-project-top-ten/"
    driver.get(url)
    sleep(2)

    results = []

    #XPath -Find <li> elements that contain <a><strong>
    xpath_expr = '//li[a[strong]]'
    items = driver.find_elements(By.XPATH, xpath_expr)

    #Get the first 10 items
    for item in items[:10]:
        try:
            a_tag = item.find_element(By.XPATH, './a')
            title = a_tag.text.strip()
            href_link = a_tag.get_attribute('href')
        except:
            title = ''
            href_link = ''
        
        #Append results in a dictionary
        results.append({
            'Title': title,
            'Link': href_link
        })

    #Print check
    print("Top 10 OWASP Vulnerabilities:")
    for entry in results:
        print(entry)

    #Save to CSV
    df = pd.DataFrame(results)
    df.to_csv('owasp_top_10.csv', index=False)

#Run
if __name__ == '__main__':
    scrape_owasp_top_10()
    driver.quit()