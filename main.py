import requests, numpy

class Song:
    mbid = ''
    def __init__(self, name, author, mbid):
        self.name = name
        self.author = author
        self.mbid = mbid

def getSongs(search):
    r = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.search&track="+ search +"&limit=10&api_key=804da8b01316d96c9da44d8fa1cee47e&format=json")
    r = r.json()['results']['trackmatches']['track']
    songs = []
    for i in r:
        songs.append(Song(
            i['name'],
            i['artist'],
            i['mbid']
        ))
    return songs

def getSimilarSongsObjects(search):
    similarSongs = []
    songs = getSongs(search)
    for i in songs:
        if i.mbid != '':
            r = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getSimilar&mbid="+ i.mbid +"&limit=10&api_key=804da8b01316d96c9da44d8fa1cee47e&format=json")
            r = r.json()['similartracks']['track']
            for x in r:
                if 'mbid' in x:
                    similarSongs.append(Song(x['name'], x['artist'], x['mbid']))
                else:
                    similarSongs.append(Song(x['name'], x['artist'], ''))
    similarSongs = list(dict.fromkeys(similarSongs))
    return similarSongs

def getSimilarSongs(search):
    songs = getSimilarSongsObjects(search)
    result = ""
    for i in songs:
        result = result + i.name + " by " + i.author['name'] + ", "
    result = result[:-2]
    return result