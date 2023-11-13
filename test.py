import frhd
import pyperclip
my_track = frhd.Track.Track()
my_track.insLine('p',-40,50,10000,50)
my_track.addTriangle(50,-50,100,100)

pyperclip.copy(my_track.genCode())
# print(my_track.genCode())