import frhdtools
import pyperclip
import math
import random

my_track = frhdtools.Track.Track()

orig_x = 50
orig_y = 50

stair_length = 15
stair_height = 15

my_track.insLine(orig_x, orig_y, orig_x - 100, orig_y, "p")

num_iters = 10000

for i in range(num_iters):
    # Generate a staircase with each step having a length of 10 and a height of 15
    # my_track.insLine(orig_x + (i * stair_length), orig_y + (i * stair_height), orig_x + ((i + 1) * stair_length), orig_y + (i * stair_height), "p")
    # my_track.insLine(orig_x + ((i + 1) * stair_length), orig_y + (i * stair_height), orig_x + ((i + 1) * stair_length), orig_y + ((i + 1) * stair_height), "p")

    for x in range(3):
        my_track.insLine(orig_x + (i * stair_length) + int((random.random()-0.5)*10), orig_y + (i * stair_height),orig_x + ((i + 1) * stair_length), orig_y + ((i + 1) * stair_height) + int((random.random()-0.5)*20), "p")
        for s in range(int(random.normalvariate(1, 0.5)*10)):
            my_track.insLine(orig_x + (i * stair_length) + int((random.random()-0.5)*10), orig_y + (i * stair_height) + int((random.random()-0.5)*50) - 50*s,orig_x + ((i + 1) * stair_length), orig_y + ((i + 1) * stair_height) + int((random.random()-0.5)*20) + int((random.random()-0.5)*50) - 50*s, "s")

    if i % 10 == 0:
        for b in range(random.randint(1, 50)):
            my_track.insBomb(orig_x + (i * stair_length) + int((b*random.random()-0.5)*5), orig_y + (i * stair_height)+b*50+int((b*random.random()-0.5)*2) + 50)


code = my_track.genCode()
pyperclip.copy(code)
print(my_track.genCode(), " copied to clipboard")