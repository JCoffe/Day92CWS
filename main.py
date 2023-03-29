import requests
from bs4 import BeautifulSoup
import csv

position = 0

url = "https://www.billboard.com/charts/south-korea-songs-hotw/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all list items with class "o-chart-results-list__item"
    items = soup.find_all('li', class_='o-chart-results-list__item')
    # Extract title of each song from H3 tag inside list item (if present)
    top_songs = []
    for item in items:
        try:
            title = item.find('h3').text.strip()
            artist = item.find('span').text.strip()
            top_songs.append((title, artist))
        except AttributeError:
            # Ignore list items without an H3 tag
            pass

    # Print top 10 songs
    for i, song in enumerate(top_songs[:10]):
        print(f'{i+1}. {song[0]} - {song[1]}')


    top_10_songs = top_songs[:10]

    with open('top10songs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Position', 'Song', 'Artist'])

        for song in top_10_songs:
            writer.writerow([position + 1, song[0], song[1]])
            position = position + 1



else:
    print("Error accessing website")



