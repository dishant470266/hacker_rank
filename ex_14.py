user = {}

name = input('enter your name : ')
age = input('enter your age : ')
fav_movie = input('your fav_movie name : ').split(',')
fav_song = input('your fav_song name : ').split(',')

user['name'] = name
user['age'] = age
user['fav_movie'] = fav_movie
user['fav_song'] = fav_song
for key,value in user.items():
    print(f" {key} : {value} ")

