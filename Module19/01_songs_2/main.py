violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_count = int(input('Сколько песен выбрать? '))
sum_songs_len = 0

for i in range(songs_count):
    song = input('Введите название {0} песни: '.format(i + 1))
    sum_songs_len += violator_songs[song]

print('\nОбщее время звучания песен:', round(sum_songs_len, 2), 'минуты')
