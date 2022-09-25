violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_count = int(input('Сколько песен выбрать? '))
total_songs_time = 0

for num in range(songs_count):
    print('Название', num + 1, 'песни:', end = ' ')
    song = input()
    for i in range(len(violator_songs)):
        if violator_songs[i][0] == song:
            total_songs_time += violator_songs[i][1]

print('\nОбщее время звучания песен:', round(total_songs_time, 2))