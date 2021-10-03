import cv2
import numpy as np
import glob
import subprocess
import os
import shutil

face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml')

files =glob.glob("./tmp\\*")

for fname in files:    #あとはForで1ファイルずつ実行されていく
    bgr = cv2.imread(fname, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(gray, 1.1, 3)
    if len(face_rects) > 0:
        for (x,y,w,h) in face_rects:
            face= bgr[y:y+h, x:x+w]
            reduc = cv2.resize(face, (8,8))
            mosaic = cv2.resize(reduc,(w,h))
            bgr[y:y+h, x:x+w]=mosaic
            #cv2.rectangle(bgr, (x,y), (x+w,y+h), (255,0,0), 3)  
                    #(255,0,0)→枠の色は青
                        #最後の引数は太さ(-1にすると塗りつぶし)
        cv2.imwrite(fname, bgr) 

cv2.destroyAllWindows()

subprocess.run(["make_vid.bat", f""])
subprocess.run(["make_audio.bat", f""])

path = 'tmp'
shutil.rmtree(path)

aac = 'Audio.aac'
os.remove(aac)

noaudi = 'output/out.mp4'
os.remove(noaudi)

print("done")