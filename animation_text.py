import frhd
import pyperclip
import math


my_track = frhd.Track.Track()


gap = 1000
num_frames = 500

# my_track.insLine("p",-50, 50, num_frames * gap, 50)
# my_track.insAntiGrav(0,0)

platform_width = 100

message = "Hello. this is animated text."

for i in range(num_frames):
    my_track.insPortal(i*gap, 75, i*gap + gap, 75)
    my_track.insLine("p", i*gap-int(platform_width/2), 75, i*gap+int(platform_width/2), 75)
    
    ORIGIN_X = i*gap+1
    ORIGIN_Y = -50
    
    text_pos= int(i/num_frames*len(message))+1
    
    # draw text
    my_track.addText(ORIGIN_X+len(message)*20, ORIGIN_Y, message[0:text_pos])
    
    # draw cursor so it blinks
    # if math.sin(text_pos) > 0.5:
    my_track.insLine("p", ORIGIN_X+len(message)*20 + text_pos*20, ORIGIN_Y +10, ORIGIN_X+len(message)*20 + text_pos*20 +25, ORIGIN_Y+10)
        # my_track.insLine("p", ORIGIN_X+len(message)*20, ORIGIN_Y, ORIGIN_X+len(message)*20, ORIGIN_Y+20)


code = my_track.genCode()
pyperclip.copy(code)
print("copied to clipboard")
# print(code)

#        -1i 1i 31l0 1i,34 1i 2g 1i##
#        -1i 1i 31l0 1i,34 1i 2g 1i##W 68 0 84 0