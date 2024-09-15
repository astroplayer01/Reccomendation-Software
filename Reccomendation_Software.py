from Inverted_Index_Hash import hash, find_movie_by_name, find_movies_by_genre, find_movies_by_length, find_movies_by_rating

def main():
    welcome_message()



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

def user_input():
    
    print()
    user_prompt = input("Please enter either the Name, Genre, Rating, or Length of the movie you want to find: ")

    if type(user_input) == str:
        pass


print("finish")