import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/title/?title_type=feature&num_votes=10000,&sort=user_rating,desc"

# we need this user-agent because imdb rejects the request otherwise
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

if response.status_code == 200: #if the request was a success

    soup = BeautifulSoup(response.text, 'html.parser')
    
    headings = soup.find_all('h3', class_="ipc-title__text")

    for head in headings:
        f=open('scrapedmovies.txt', 'a')
        f.write(head.text.strip() + '\n') #separates text and adds a line
        f.close()
else:                       
    print(response.status_code)