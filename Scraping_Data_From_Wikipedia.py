from bs4 import BeautifulSoup
import requests

# Let's grab the url of the site we want to extract data from and save it in a variable
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

# There's 3 tables in the page, the table we want is the 2nd table in the html code, so we'll use indexing.
soup.find_all('table')[1]
table = soup.find_all('table')[1]

# Let's grab the column headers from the table
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)

# Now let's import pandas so we can create a table visual
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

# Now let's grab the rows
column_data = table.find_all('tr')

# We'll grab the 'td' element inside of each 'tr' and place those in a list
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # Let's add these rows to our table
    length = len(df)
    df.loc[length] = individual_row_data

# Let's export it to a csv, we'll say index=False to remove the first column of numbering we don't want
df.to_csv(r'/Users/username/Python/World_Companies.csv', index=False)
