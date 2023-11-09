import frhdtools
import pyperclip
import math


my_track = frhdtools.Track.Track()
my_track.insLine(-50, 50, 100000, 50, "p")


gap = 50

def box(x, y, w, h):
    my_track.insLine(x, y, x+w, y, "p")
    my_track.insLine(x+w, y, x+w, y+h, "p")
    my_track.insLine(x+w, y+h, x, y+h, "p")
    my_track.insLine(x, y+h, x, y, "p")


anim_divisor = 50

for i in range(2000):
    my_track.insBoost(-50 + i * gap, 50+int(math.sin(i/10)*10), 90+int(math.sin(i/10)*10))

    if i % 15 == 0:
        box(-50 + i * gap, 50+int(math.sin(i/anim_divisor)*30)-300, 90+int(math.cos(i/anim_divisor)*50), 90+int(math.sin(i/anim_divisor)*100))
        box(-50 + i * gap + int(math.cos(i/anim_divisor)*100), 50+int(math.cos(i/anim_divisor)*30)-300, 90+int(math.sin(i/anim_divisor)*20), 90+int(math.cos(i/anim_divisor)*50))
    gap += 0


code = my_track.genCode()
pyperclip.copy(code)
print("copied to clipboard")