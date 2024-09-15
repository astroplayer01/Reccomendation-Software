import Movie_Data

#creates the dictionaries to house the data at certain indexes
genre_index = {}
name_index = {}
rating_index = {}
length_index = {}



#puts the data into the table
def set_hash():

    for movie in Movie_Data:
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
    pass



