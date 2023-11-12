import frhd
my_track = frhd.Track.Track()
my_track.insLine('p',-40,50,100,50)
my_track.addTriangle(50,-50,100,100)

print(my_track.genCode())