cd C:\Users\segok\Desktop\face_recognition\ffmpeg.exe

ffmpeg -r 30 -i C:/Users/segok/Desktop/face_recognition/tmp/%%05d.png -vcodec libx264 -pix_fmt yuv420p -r 30 output/out.mp4