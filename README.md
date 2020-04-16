# Song-Similarity
Using the last.fm/audioscrobbler API to find similar songs to the title you search

## Syntax
`Song`: an object with attributes `name`, `author`, and `mbid`
`getSongs(SEARCHTERM)`: returns a list of `Song` objects that match the `SEARCHTERM`
`getSimilarSongsObjects(SEARCHTERM)`: returns a list of `Song` objects similar to the songs found in `getSongs`
`getSimilarSongs`: Returns a readable string with a list of songs similar to the songs found in `getSongs`
