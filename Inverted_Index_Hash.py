from Movie_Data import movie_data

#creates the dictionaries to house the data at certain indexes
genre_index = {}
name_index = {}
rating_index = {}
length_index = {}



#puts the data into the table
def hash():
    global genre_index, name_index, rating_index, length_index
    for movie in movie_data:
        #declares variables with each data point
        genre, name, rating, length = movie

        #creates the key if not already existing then inserts the 2d index there
        if genre not in genre_index:
            genre_index[genre] = []

        genre_index[genre].append(movie)

        if name not in name_index:
            name_index[name] = []
        
        name_index[name].append(movie)

        rating = float(rating)
        if rating not in rating_index:
            rating_index[rating] = []
        
        rating_index[rating].append(movie)

        length = int(length)
        #using a range for the movie length
        length_range = f"{(length // 10) * 10}-{((length // 10) + 1) * 10}"
        if length_range not in length_index:
            length_index[length_range] = []
        
        length_index[length_range].append(movie)

#querey the indexes
def find_movies_by_genre(genre):
    return genre_index.get(genre, [])

def find_movies_by_rating(rating):
    return rating_index.get(rating, [])

def find_movies_by_length(length_range):
    return length_index.get(length_range, [])

def find_movie_by_name(partial_name):
    results = []
    for name in name_index:
        if partial_name.lower() in name.lower():
            results.extend(name_index[name])
    return results



