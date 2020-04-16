import aiohttp.ClientSession #asynchronous requests

class Song:
    def __init__(self, name, author, mbid=''):
        self.name = name
        self.author = author
        self.mbid = mbid #can also do mbid or '' but looks cleaner 
       
async def getSongs(search):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://ws.audioscrobbler.com/2.0/?method=track.search&track="+ search +"&limit=10&api_key=804da8b01316d96c9da44d8fa1cee47e&format=json") as r:
            res = await r.json() #can't get the result from coroutines
    r = res['results']['trackmatches']['track']
    songs = []
    for i in r:
        songs.append(Song(
            i['name'],
            i['artist'],
            i['mbid'] #TODO ask about Nonetype
        ))
    return songs

async def getSimilarSongsObjects(search):
    similarSongs = []
    songs = await getSongs(search)
    for i in songs:
        if i.mbid != '':
            async with aiohttp.ClientSession as session:
                async with session.get("http://ws.audioscrobbler.com/2.0/?method=track.getSimilar&mbid="+ i.mbid +"&limit=10&api_key=804da8b01316d96c9da44d8fa1cee47e&format=json") as r:
                    res = await r.json()
            r = res['similartracks']['track']
            for x in r:
                if 'mbid' in x:
                    similarSongs.append(Song(x['name'], x['artist'], x['mbid']))
                else:
                    similarSongs.append(Song(x['name'], x['artist'])) #mkbid is already set to '' so redundant
    similarSongs = list(dict.fromkeys(similarSongs)) #I love this
    return similarSongs

async def getSimilarSongs(search):
    songs = await getSimilarSongsObjects(search) #Calling coroutine
    result = ""
    # for song in songs: #This code is redundant can shorten
    #    result += song.name + " by " + song.author['name'] + ", " 
    result = ', '.join([f'{song.name} by {song.author["name"])
    # result = result[:-2] fixed redundancy
    return result
