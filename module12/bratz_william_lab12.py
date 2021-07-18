movie_list = ["Scott Pilgrim vs The World", "O' Brother Where Art Thou?", "Sandlot"]

movies = open("movies.txt", "w")

for movie in movie_list:
    movies.write(movie + "\n")

movies.close()

print("Finished writing to file.")
