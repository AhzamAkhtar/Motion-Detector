import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1=cam.read() #compairing two frames to detect any motion in new frame with the help of new frame
    ret,frame2=cam.read()
    diff=cv2.absdiff(frame1,frame2)
    # diif showing colourful oytput,which may leads to error,so converted it to gray in nest step
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    # TO GET RID OF NOISE IN AN IMAGE USE THRESHOLD
    threshold,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    # USING DILATED T ENHANCE THE IMAGE
    dilated=cv2.dilate(thresh,None,iterations=3)
    #YOU CAN SAY THAT TO DETECT EDGES
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    for c in contours:
        if cv2.contourArea(c)<4000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.Beep(500,200)
        print("go")
        #winsound.PlaySound("alert.wav",winsound.SND_ASYNC)
    if cv2.waitKey(10)==ord("q"):
        break
    cv2.imshow("be sure",frame1)