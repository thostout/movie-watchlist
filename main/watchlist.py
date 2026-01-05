import tmdbsimple as tmdb

tmdb.API_KEY = "4f5ab13628b2c3705dc646b7673e3c7e"

movie_name = input("What movie do you want to search for? ")

search = tmdb.Search()
response = search.movie(query=movie_name)
results = response["results"]
print(f"Found {len(results)} movies")


for i, movie in enumerate(results):
    print(f"{i}. {movie['title']} - {movie['release_date']}")

choice = int(input("\nPick the number corelating to corect movie. "))

selected_movie = results[choice]
movie_id = selected_movie["id"]

movie = tmdb.Movies(movie_id)
detail = movie.info()

print(f"\nTitle {detail['title']}")
print(f"Release Date: {detail['release_date']}")
print(f"Rating: {detail['vote_average']}")
