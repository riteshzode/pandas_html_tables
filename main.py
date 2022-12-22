import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

scraped = pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

for index, table in enumerate(scraped):
    print("######################################")
    print(index)
    print(table)
    
print(scraped[4])