import frhd
import pyperclip
import math


my_track = frhd.Track.Track()

gap = 1000
num_frames = 1000

def box(x, y, w, h):
    my_track.insLine("p", x, y, x+w, y)
    my_track.insLine("p", x+w, y, x+w, y+h)
    my_track.insLine("p", x+w, y+h, x, y+h)
    my_track.insLine("p", x, y+h, x, y,)

# my_track.insLine("p",-50, 50, num_frames * gap, 50)
# my_track.insAntiGrav(0,0)

platform_width = 100

for i in range(num_frames):
    my_track.insPortal(i*gap, 75, i*gap + gap, 75)
    my_track.insLine("p", i*gap-int(platform_width/2), 75, i*gap+int(platform_width/2), 75)
    
    ORIGIN_X = i*gap
    ORIGIN_Y = -200
    
    box(ORIGIN_X, ORIGIN_Y, int(math.cos(i/100)*100), int(math.sin(i/100)*100))
    box(ORIGIN_X + int(math.cos(i/75)*150), ORIGIN_Y - int(math.sin(i/75)*150), 10, 10)


code = my_track.genCode()
print("copied to clipboard")
print(code)

#        -1i 1i 31l0 1i,34 1i 2g 1i##
#        -1i 1i 31l0 1i,34 1i 2g 1i##W 68 0 84 0