def append_movies(file_name, movie_list):
    movie_file = open(file_name, "a")

    for movie in movie_list:
        movie_file.write(movie + "\n" )

    movie_file.close()


movies = ["Bad Boys", "Step Brothers", "Toy Story"]

def main():
    print("Appending Movie List")
    append_movies("movies.txt", movies)
    print("Appending complete.")

main()