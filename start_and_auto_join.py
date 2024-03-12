#import pyautogui
# import os
# #screenWidth, screenHeight = pyautogui.size()

# #pyautogui.getWindowsWithTitle

# #"\"${config:zomboid_folder}\\ProjectZomboid64 - nosteam-debug.bat\""
# # "zomboid_folder": "E:\\Steam\\steamapps\\common\\ProjectZomboid",
# from subprocess import Popen, CREATE_NEW_CONSOLE

# Popen([path], creationflags=CREATE_NEW_CONSOLE)


import subprocess
import time
import pyautogui
import pydirectinput

# Open zomboids
process_list = []


open_programs = True

# Scaling 150%
resX = 3840 #/ 1.5           
resY = 2160 #/ 1.5

def open_program_instances(program_path, num_instances):
    process_list = []
    for _ in range(num_instances):
        process = subprocess.Popen(program_path, shell=True)
        process_list.append(process)


if __name__ == "__main__":

    path = r'start "" "E:\Steam\steamapps\common\ProjectZomboid\ProjectZomboid64 - nosteam-debug.bat"'

    click_map = []

    num_instances = 4


    if open_programs:
        open_program_instances(path, num_instances)
        time.sleep(5)

    windows = pyautogui.getWindowsWithTitle("Project Zomboid")

    incX = int(resX/num_instances) * 2
    incY = int(resY/num_instances) * 2

    print("incX=" + str(incX) + ", incY=" + str(incY))
    cX = 0
    cY = 0
    for win in windows:
        #print("CX = " + str(cX) + ", cY = " + str(cY))
        win.resizeTo(incX, incY)
        win.moveTo(cX,cY)

        # Click Map
        temp_map = {"join" : {
            "x" : cX + 240,
            "y" : cY + 785
        }}


        click_map.append(temp_map)


        cX += incX
        if cX >= resX:
             cX = 0
             cY += incY
        # #win.close()


    # if open_programs:
    #     time.sleep(18)
    # count = 0

    # for win in windows:
    #     #win.setFocus()
    #     join = click_map[count]['join']
    #     pydirectinput.click(x=join['x'], y=join['y'], clicks=5, interval=0.2)

    #     count += 1



