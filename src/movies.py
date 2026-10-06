movies = [
    {"title": "Some film", "genre": "Comedy"},
    {"title": "Another film", "genre": "Tragedy"},
]

favourites = []

def add_movie():
    title = input("Title: ")
    genre = input("Genre: ")
    movie = {"title": title, "genre": genre}
    movies.append(movie)
    print("Movie added!")

def show_movies():
    for movie in movies:
        print(movie["title"])
        print(movie["genre"])

def add_to_favourites():
    title = input("Enter movie title: ")
    for movie in movies:
        if movie["title"].lower() == title.lower():
            favourites.append(movie)
            print("Movie added to favorites!")
            return
    print("Movie not found.")


def show_favourites():
    if not favourites:
        print("No favorite movies.")
        return
    for movie in favourites:
        print(movie["title"])
        print(movie["genre"])


