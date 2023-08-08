import requests
import json

artistNames = ['Taylor Swift','The Weeknd','Kanye West','Lana Del Rey','Kendrick Lamar','Drake','Tyler, the Creator','Billie Eilish','Arctic Monkeys','SZA','Rihanna','LIL UZI VERT','Frank Ocean','Olivia Rodrigo','Radiohead','Tame Impala','Doja Cat','Metro Boomin','Ariana Grande','Beyoncé','Harry Styles','Post Malone','Nicki Minaj','Travis Scott','Lady Gaga','Steve Lacy','pinkpantheress','Coldplay','Childish Gambino','Paramore','Kali Uchis','Gorillaz','The Neighbourhood','Bruno Mars','Dua Lipa','Miley Cyrus','The Smiths','Katy Perry','Mac Miller','Nirvana','Mac DeMarco','Eminem','Queen','Playboi Carti','Mitski','The Beatles','Joji','Lorde','A$AP Rocky','TV Girl']
artistNames_ = ['Taylor Swift']
apiKey = ''

def getTopAlbums(artists):
        '''parses provided artist name list'''
        for i in range(len(artists)):
            '''artist name and api_key are inserted into URL'''
            albumURL = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={name}&api_key={key}&format=json'.format(name = artists[i],key = apiKey)
            response = requests.get(albumURL)
            api_data = response.json()
            '''creates list of they album key pairs for specific artist'''
            nameList = api_data['topalbums']['album']
            
            
            for name in nameList:
                    print(name['name'])
        

        '''print(api_data['topalbums']['album'][0]['name'])'''

       


getTopAlbums(artistNames)