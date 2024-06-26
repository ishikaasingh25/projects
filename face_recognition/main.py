import face_recognition
import cv2
import numpy
import numpy as np
import csv
import os
from datetime import datetime

video_capture=cv2.VideoCapture(0)
tata_image=face_recognition.load_image_file("photos/tata.jpg")
tata_encoding=face_recognition.face_encodings(tata_image)[0]

kohli_image=face_recognition.load_image_file("photos/kohli.jpg")
kohli_encoding=face_recognition.face_encodings(kohli_image)[0]

musk_image=face_recognition.load_image_file("photos/musk.jpg")
musk_encoding=face_recognition.face_encodings(musk_image)[0]

known_faces_encoding=[
    tata_encoding,
    kohli_encoding,
    musk_encoding
]
known_faces_names=[
    "tata",
    "kohli",
    "musk"
]

students=known_faces_names.copy()
face_locations=[]
face_encodings=[]
face_names=[]
s=True

now=datetime.now()
current_date=now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+',newline='')
lnwriter = csv.writer(f)

while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=numpy.ascontiguousarray(small_frame[:,:,::-1])
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_faces_encoding,face_encoding)
            name=""
            face_distance=face_recognition.face_distance(known_faces_encoding,face_encoding)
            best_match_index=np.argmin(face_distance)
            if matches[best_match_index]:
                name=known_faces_names[best_match_index]
            face_names.append(name)
            if name in known_faces_names:
                #students.remove(name)
                print("Present",name)
                current_time=now.strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time])

    cv2.imshow("attendance system",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
