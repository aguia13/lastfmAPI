import requests
import json

albumList = ['Fearless']

for albumName in albumList:
    api_url = f'https://musicbrainz.org/ws/2/release/?query={albumName}&fmt=json'

    response = requests.get(api_url, headers={'User-Agent': 'YourApp/1.0'})

    if response.status_code == 200:
        search_results = response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
    
    # Extract MBID from search results
    if 'releases' in search_results:
        for release in search_results['releases']:
            if 'id' in release:
                mbid = release['id']
                print(f"Album: {albumName}, MBID: {mbid}")
                break


