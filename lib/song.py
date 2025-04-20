class Song:
    count = 0
    artists = []         # Unique artists
    all_artists = []     # All artists (with duplicates)
    genres = []          # Unique genres
    all_genres = []      # All genres (with duplicates)
    genre_count = {}     # Genre histogram
    artist_count = {}    # Artist histogram

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.all_artists.append(artist)
        Song.all_genres.append(genre)

        Song.add_to_artists()
        Song.add_to_genres()
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_to_artists(cls):
        for artist in cls.all_artists:
            if artist not in cls.artists:
                cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls):
        for genre in cls.all_genres:
            if genre not in cls.genres:
                cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls):
        genre = cls.all_genres[-1]
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        artist = cls.all_artists[-1]
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
