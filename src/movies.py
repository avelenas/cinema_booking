movies = [
    {"title": "Some film", "genre": "Comedy"},
    {"title": "Another film", "genre": "Tragedy"},
]

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

def search_movie():
    title = input("Enter title: ")
    for movie in movies:
        if title.lower() in movie["title"].lower():
            print(movie["title"])
            print(movie["genre"])


