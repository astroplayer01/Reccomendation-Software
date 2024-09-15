from Inverted_Index_Hash import hash

def Reccomendation_Software():
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