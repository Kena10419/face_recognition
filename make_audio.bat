cd C:\Users\segok\Desktop\face_recognition\ffmpeg.exe

ffmpeg -i input.mp4 -c copy Audio.aac

ffmpeg -i output/out.mp4 -i Audio.aac -c copy output/output.mp4