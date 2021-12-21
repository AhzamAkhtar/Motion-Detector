import cv2 as cv
import time
import datetime
from win32api import GetSystemMetrics
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
capture=cv.VideoCapture(0)
face_cascade=cv.CascadeClassifier("face.xml")
fullbody_cascade=cv.CascadeClassifier("fullbody.xml")
detection=False
detection_stopped_time=None
timer_started=False
SECOND_TO_RECORD_AFTER_DETECTION=5
framesize=(int(capture.get(3)),int(capture.get(4)))
fourcc=cv.VideoWriter_fourcc("m","p","4","v")
while True:
    ret,frame=capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    #body=fullbody_cascade.detectMultiScale(gray,1.3,5)
    if(len(faces)):
        if detection:
            timer_started=False
        else:
            timer_started=True
            current_time=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file_name=f"{current_time}.mp4"
            out = cv.VideoWriter(file_name, fourcc, 20.0, (width,height))
            print("Started Recording ")
    elif detection:
        if timer_started:
            if time.time()-detection_stopped_time>=SECOND_TO_RECORD_AFTER_DETECTION:
                detection=False
                timer_started=False
                out.release()
                print("Stop Recording")
        else:
            timer_started=True
            detection_stopped_time=time.time()
    if detection:
        out.write(frame)
    #for (x,y,w,h) in faces:
        #cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow("Frame",frame)
    if cv.waitKey(10)==ord("q"):
        break
cv.release()
cv.destroyAllWindows()