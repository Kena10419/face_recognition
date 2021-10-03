import os
import cv2  
import subprocess
from pathlib import Path

new_dir_path = 'tmp'
os.mkdir(new_dir_path)

videoPath = "./input.mp4"
cap = cv2.VideoCapture(videoPath)

f = open("make_im.bat", 'w', encoding='ANSI')
fvid = open("make_vid.bat", 'w', encoding='ANSI')
faudi = open("make_audio.bat", 'w', encoding='ANSI')

batpath = os.path.abspath("ffmpeg.exe")

print(batpath)

tmppath = os.getcwd()
print(tmppath)

playtim = (f"{cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)}") 

f.write('cd ' + batpath + ('\n\nffmpeg -ss 00:00 -to 00:' + (playtim) + ' -i input.mp4 tmp/%%05d.png'))
fvid.write('cd ' + batpath + ('\n\nffmpeg -r 30 -i C:/Users/segok/Desktop/face_recognition/tmp/%%05d.png -vcodec libx264 -pix_fmt yuv420p -r 30 output/out.mp4'))
faudi.write('cd ' + batpath + ('\n\nffmpeg -i input.mp4 -c copy Audio.aac\n\nffmpeg -i output/out.mp4 -i Audio.aac -c copy output/output.mp4'))

f.close()
fvid.close()
faudi.close()

subprocess.run(["make_im.bat", f""])

import face_recognition