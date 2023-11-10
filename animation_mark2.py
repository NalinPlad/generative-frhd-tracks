import frhd
import pyperclip
import math


my_track = frhd.Track.Track()


gap = 100
num_frames = 1000


my_track.insLine("p",-50, 50, num_frames * gap, 50)

for i in range(num_frames):
    my_track.insPortal(i*gap, 0, i*gap + gap, 0)


code = my_track.genCode()
pyperclip.copy(code)
print("copied to clipboard")
print(code)

#        -1i 1i 31l0 1i,34 1i 2g 1i##
#        -1i 1i 31l0 1i,34 1i 2g 1i##W 68 0 84 0