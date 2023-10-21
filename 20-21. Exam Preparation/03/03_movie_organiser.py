from collections import defaultdict


def movie_organizer(*movies):
    movies_dict = defaultdict(list)
    for movie, genre in movies:
        movies_dict[genre].append(movie)

    sorted_movies = sorted(movies_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for genre, movies in sorted_movies:
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"

    return result


def main():
    # print(movie_organizer(
    #     ("The Godfather", "Drama"),
    #     ("The Hangover", "Comedy"),
    #     ("The Shaw shank Redemption", "Drama"),
    #     ("The Pursuit of Happiness", "Drama"),
    #     ("The Hangover Part II", "Comedy"))
    # )

    print(movie_organizer(("Avatar: The Way of Water", "Action"),
                          ("House Of Gucci", "Drama"),
                          ("Top Gun", "Action"),
                          ("Ted", "Comedy"),
                          ("Duck Soup", "Comedy"),
                          ("The Dark Knight", "Action"),
                          ("A Star Is Born", "Musicals"),
                          ("The Warrior", "Action"),
                          ("Like A Boss", "Comedy"),
                          ("The Green Mile", "Drama"),
                          ("21 Jump Street", "Comedy")
                          )
          )


if __name__ == "__main__":
    main()
