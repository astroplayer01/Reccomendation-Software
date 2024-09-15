# Movie Search Application

## Overview
This project is a command-line application that allows users to search for movies by genre, rating, length, or name. The application uses an inverted index hash to store and retrieve movie data efficiently.

## Features
- Search for movies by genre, rating, length, or name.
- Display search results in a user-friendly format.
- Exit the application gracefully.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/moviesearchapp.git
    cd moviesearchapp
    ```
2. Ensure you have Python installed (version 3.6 or higher).

## Usage
1. Run the application:
    ```bash
    python main.py
    ```
2. Follow the on-screen instructions to search for movies.

## Code Structure
- `Reccomendation_Software.py`: Contains the main logic of the application.
- `Inverted_Index_Hash.py`: Contains functions to create and query the inverted index.
- `Movie_Data.py`: Contains the movie data used by the application.

## Functions

### main()
- Initializes the hash table.
- Displays a welcome message.
- Prompts the user for search input and displays results.

### welcome_message()
- Prints a welcome message to the user.

### determine_input_type(user_input)
- Determines the type of input (genre, rating, length, or name) based on the user's input.

### print_result(value, results, input_type)
- Prints the search results in a formatted manner.

### hash()
- Creates dictionaries to store movie data indexed by genre, name, rating, and length.

### find_movies_by_genre(genre)
- Returns a list of movies that match the specified genre.

### find_movies_by_rating(rating)
- Returns a list of movies that match the specified rating.

### find_movies_by_length(length_range)
- Returns a list of movies that fall within the specified length range.

### find_movie_by_name(partial_name)
- Returns a list of movies that match the specified name.

## Movie Data
The movie data is stored in a list of lists, where each sublist contains the following information about a movie:
- Genre
- Name
- Rating
- Length

Example:
```python
movie_data = [
    ['drama', 'The Shawshank Redemption', '9.3', '142'],
    ['crime', 'The Godfather', '9.2', '175'],
    ...
]
```

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.
