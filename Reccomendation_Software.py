from Inverted_Index_Hash import hash, find_movie_by_name, find_movies_by_genre, find_movies_by_length, find_movies_by_rating


def main():
    print("Welcome to the Movie Recommendation System!")
    print("You can search for movies by typing a genre, rating, length, or name.")
    
    while True:
        user_input = input("\nEnter your search term (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        input_type, value = determine_input_type(user_input)
        
        if input_type == 'genre':
            results = find_movies_by_genre(value)
            print("Movies in genre", value, ":", results)
        
        elif input_type == 'rating':
            results = find_movies_by_rating(value)
            print("Movies with rating", value, ":", results)
        
        elif input_type == 'length':
            results = find_movies_by_length(value)
            print("Movies in length range", value, ":", results)
        
        elif input_type == 'name':
            results = find_movie_by_name(value)
            print("Movies matching name", value, ":", results)
        
        else:
            print("Invalid input. Please try again.")



def welcome_message():
    message = """
    **************************************************
    *                                                *
    *                WELCOME TO OUR                  *
    *                                                *
    *                  MOVIE APP!                    *
    *                                                *
    *        We hope you find the perfect movie!     *
    *                                                *
    **************************************************
    """
    print(message)


def determine_input_type(user_input):
    try:
        # Check if input is a float (rating)
        rating = float(user_input)
        return 'rating', rating
    except ValueError:
        pass

    try:
        # Check if input is an integer (length)
        length = int(user_input)
        length_range = f"{(length // 10) * 10}-{((length // 10) + 1) * 10}"
        return 'length', length_range
    except ValueError:
        pass

    # Check if input is a genre
    genres = ['drama', 'crime', 'action', 'thriller', 'biography', 'adventure', 'sci-fi', 'mystery', 'war', 'fantasy']
    if user_input.lower() in genres:
        return 'genre', user_input.lower()

    # Otherwise, assume it's a movie name
    return 'name', user_input



if __name__ == "__main__":
    main()