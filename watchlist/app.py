
import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user.
7) Search movies.
8) Exit.
Your selection: """

welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_table()

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date,"%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title,timestamp)


def prompt_add_user():
    username = input("username: ")
    database.add_user(username)



def print_movie_list(heading,movies):
    print(f"--{heading} movies --")
    for _id,title,release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {human_date})")
    print("--- \n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username,movie_id)

def prompt_search_movies():
    search_term = input("Enter the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found: ",movies)
    else:
        print("Found no movies for that search term!")

while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    if user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming",movies)
    if user_input == "3":
        movies = database.get_movies()
        print_movie_list("All",movies)
    if user_input == "4":
        prompt_watch_movie()
    if user_input == "5":
        username = input("Username: ")
        movies = database.get_watched_movies(username)
        if movies:
            print_movie_list("watched",movies)
        else:
            print("That user has watched no movies yet!")
    if user_input == "6":
        prompt_add_user()
    if user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
