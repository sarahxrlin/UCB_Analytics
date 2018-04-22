# Dependencies
from bs4 import BeautifulSoup
import requests

# URL of Python reddit
url = 'https://www.reddit.com/r/Python/'

# Retrieve page with the requests module
html = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html.text, 'html.parser')

# Examine the results, then determine element that contains sought info
# results are returned as an iterable list
results = soup.find_all('div', class_='top-matter')

# Loop through returned results
for result in results:
    # Retrieve the thread title
    title = result.find('p', class_='title')
    # Access the thread's text content
    title_text = title.a.text
    # print(title_text)

    # Access the thread with CSS selectors
    thread = result.find('li', class_='first')
    # The number of comments made in the thread
    comments = thread.text.lstrip()
    # Parse string, e.g. '47 comments' for possible numeric manipulation
    if (' comments' in comments):
        comments_num = comments.replace(' comments', '')
        comments_num = int(comments_num)
    else:
        comments_num = comments.replace('comment', '')

    # Access the href attribute with bracket notation
    link = thread.a['href']

    # Run if the thread has comments
    if (comments_num):
        print('\n-----------------\n')
        print(title_text)
        print('Comments:', comments_num)
        print(link)
