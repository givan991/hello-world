current_movies = {'The Grinch':'11:00am',
                  'Rudolph':'1:00pm',
                  'Frosty the Snowman':'3:00pm',
                  'Christmas Vacation':'5:00pm'}

print('We are showing the following movies:')
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')
if current_movies.get(movie):
    print(movie, 'starts at', current_movies[movie])
else:
    print('Wrong input')
