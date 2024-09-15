from Inverted_Index_Hash import hash, find_movie_by_name, find_movies_by_genre, find_movies_by_length, find_movies_by_rating


def main():
    hash()
    welcome_message()
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
        # First, try to convert the input to an integer
        length = int(user_input)
        if length >= 10:
            length_range = f"{(length // 10) * 10}-{((length // 10) + 1) * 10}"
            return 'length', length_range
    except ValueError:
        pass

    try:
        # If it's not an integer, try to convert it to a float (rating)
        rating = float(user_input)
        if rating < 10:
            return 'rating', rating
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