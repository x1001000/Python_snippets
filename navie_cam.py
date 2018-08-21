import cv2
CAMERA_ID = 0
videoStream = cv2.VideoCapture (CAMERA_ID)

try:
    videoStream.set (cv2.cv.CV_CAP_PROP_FPS, 10)
except:
    videoStream.set (cv2.CAP_PROP_FPS, 10)

while True:
    camOn, rawframe = videoStream.read ()
    if camOn:
        rawframe = cv2.flip(rawframe, 0) #Flip Vertical 
        rawframe = cv2.flip(rawframe, 0) #Flip Horizontal 
        
        cv2.imshow ("Camera %s" % CAMERA_ID, rawframe)
            
        if cv2.waitKey(1) & 0xFF == ord ("q"): 
            break
    else:
        print ("It appears that your camera is not on")
        break
videoStream.release()
cv2.destroyAllWindows()