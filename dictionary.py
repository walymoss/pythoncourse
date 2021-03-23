movies = {"The Grinch":"11:00", "Titanic":"13:00"}
# for a in movies:
#     print(a)

movie_wanted = input("What movie would you like to see\n")    
if movie_wanted in movies:
    print(movies[movie_wanted])
else:
    print("this movie isn't in schedule")