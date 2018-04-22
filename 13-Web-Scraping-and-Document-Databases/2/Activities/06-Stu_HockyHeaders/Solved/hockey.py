# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.nhl_db
collection = db.articles

# URL of page to be scraped
url = 'https://www.nhl.com/'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Retrieve the parent divs for all articles
results = soup.find_all('li', class_='mixed-feed__item--article')

# Loop through results to retrieve article title, header, and timestamp of article
for result in results:
    title = result.find('h4', class_='mixed-feed__header').text

    lede = result.find('h5', class_='mixed-feed__subheader').text

    # The time and date of article publication
    date = result.find('time')['datetime']
    # Slice the datetime string for the date
    article_date = date[:10]
    # Slice the datetime string for the time
    time = date[11:16]
    # Determine whether article was published in AM or PM
    if (int(time[:2]) >= 13):
        meridiem = 'pm'
    else:
        meridiem = 'am'

    # Concatenate time string
    time = time + meridiem
    print('-----------------')
    print(title)
    print(lede)
    print(article_date)
    print(time)

    # Dictionary to be inserted into MongoDB
    post = {
        'title': title,
        'lede': lede,
        'date': article_date,
        'time published': time
    }

    # Insert dictionary into MongoDB as a document
    collection.insert_one(post)

# Display the MongoDB records created above
articles = db.articles.find()
for article in articles:
    print(article)
