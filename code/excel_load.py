import pandas as pd


def get_links_from_excel(file_path):
    # Load the Excel file
    data = pd.read_excel(file_path, engine='openpyxl')

    results = {}

    # Check if the column 'LINK_SITO_INFO' exists
    if "LINK_SITO_INFO" in data.columns and "DENOM_SITO_INFO" in data.columns:

        for index, row in data.iterrows():
            # Get the value in the 'LINK_SITO_INFO' column
            name = row["DENOM_SITO_INFO"]
            # Get the value in the 'LINK_SITO_INFO' column
            link = row["LINK_SITO_INFO"]
            # Check if the value is a string
            if isinstance(link, str) and isinstance(name, str):
                results[index] = {"NAME": name, "LINK": link}

        # Return the column as a list
        return results

    else:
        print("Column 'LINK_SITO_INFO' not found in the Excel file.")
        return {}
