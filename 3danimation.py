import frhd
import pyperclip
import math


my_track = frhd.Track.Track()


gap = 1000
num_frames = 500


# my_track.insLine("p",-50, 50, num_frames * gap, 50)
# my_track.insAntiGrav(0,0)

platform_width = 100



def drawCube(x_off, y_off, camera_x, camera_y, camera_z):

    x_values = list(map(lambda x: x - camera_x, [-10,10,-10,10,-10,10,-10,10]))
    y_values = list(map(lambda x: x - camera_y,[10,10,-10,-10,10,10,-10,-10]))
    z_values = list(map(lambda x: x - camera_z,[40,40,40,40,60,60,60,60]))

    faces = [
        # [0,1,3,4,0],
        [4,0,2,6,4],
        [4,5,7,6,4],
        [3,7,5,1,3],
        [0,1,3,2,0],
        [2,3,7,6,2]
        ]


    def project(x, y, z):
        if z != 0:
            return (x/z, y/z)
        else: 
            return (x, y)

    projected_points = []


    for i in range(len(x_values)):
        # plot points
        x, y = project(x_values[i], y_values[i], z_values[i])
        (x,y) = (int(x*100), int(y*100))
        projected_points.append([x,y])

    for face in faces:
        # print(face)
        my_track.insLine("s", 
                        projected_points[face[0]][0] + x_off, projected_points[face[0]][1] + y_off,
                        projected_points[face[1]][0] + x_off, projected_points[face[1]][1] + y_off,
                        projected_points[face[2]][0] + x_off, projected_points[face[2]][1] + y_off,
                        projected_points[face[3]][0] + x_off, projected_points[face[3]][1] + y_off,
                        projected_points[face[4]][0] + x_off, projected_points[face[4]][1] + y_off
                        )


message = "3D Cube Animation Test One"

for i in range(num_frames):
    my_track.insPortal(i*gap, 75, i*gap + gap, 75)
    my_track.insLine("p", i*gap-int(platform_width/2), 75, i*gap+int(platform_width/2), 75)
    
    
    ORIGIN_X = i*gap
    ORIGIN_Y = 0
    
    anim = int(i/num_frames*100)
    # print(anim)
    drawCube(ORIGIN_X, ORIGIN_Y, math.sin(anim/5)*20,math.cos(anim/5)*20,math.sin(anim/5 + math.pi*2)*20)
    
    text_pos = int(i/num_frames*len(message) * 3)+1
    
    # draw text
    my_track.addText(ORIGIN_X - int(len(message))*5, ORIGIN_Y + 150, message[0:text_pos])
    
    # stop drawing cursor when text is done
    if text_pos < len(message)*3:
        my_track.insLine("p", ORIGIN_X + text_pos*20- int(len(message))*5, ORIGIN_Y +10 + 150, ORIGIN_X + text_pos*20 +25- int(len(message))*5, ORIGIN_Y+10 + 150)
    


code = my_track.genCode()
pyperclip.copy(code)
print("copied to clipboard")
# print(code)