import billboard

old = "2018-04-22"

chart = billboard.ChartData('billboard-200', date=old)

song = chart[0]

print(song.title)
print(song.artist)
