import requests
import json


albumList = ['Fearless']
albumResult = open("topArtistAlbumsMBID.txt", "w",encoding='utf-8')

with open("topArtistAlbums.txt","r",encoding='utf-8') as albumFile:        
    for albumName in albumFile:
        api_url = f'https://musicbrainz.org/ws/2/release/?query={albumName}&fmt=json'

        response = requests.get(api_url, headers={'User-Agent': 'albumMBIDmapper'})

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
                    albumResult.write(f"Album: {albumName}, MBID: {mbid}"+'\n')
                    break



