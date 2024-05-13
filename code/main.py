import json
from excel_load import get_links_from_excel
from scrape import scrape_from_link

# Replace 'path_to_your_file.xlsx' with the path to your Excel file
values = get_links_from_excel('code/websites.xlsx')
results = []


# Loop through the links
for index, (key, val) in enumerate(values.items()):
    print(f"[{index+1}/{len(values)}] Scraping from: {val['LINK']}")

    # Attempt to scrape and handle potential failures gracefully
    try:
        scraped_data = scrape_from_link(val['LINK'])
        results.append({val['NAME']: scraped_data})
    except Exception as e:
        print(f"Failed to scrape {val['LINK']}: {e}")
        results.append({val['NAME']: None})

# Write a file with the result using json.dump to ensure proper JSON formatting
with open("result.json", "w") as f:
    json.dump(results, f)

print("Scraping completed successfully!")
