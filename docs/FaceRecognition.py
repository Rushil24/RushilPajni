import cv2
#TrDict = {'csrt': cv2.TrackerCSRT_create,
#          'kcf': cv2.TrackerKCF_create,
#          'boosting': cv2.TrackerBoosting_create,
#          'mil': cv2.TrackerMIL_create,
#          'tld': cv2.TrackerTLD_create,
#          'medianflow': cv2.TrackerMedianFlow_create,
#          'mosse': cv2.TrackerMOSSE_create}

#tracker = TrDict['csrt']()
#or
tracker = cv2.TrackerCSRT_create()
v = cv2.VideoCapture('C:\\Users\\NITRO 5\\OneDrive\\Pictures\\Camera Roll\\mot.mp4')
ret , frame = v.read()
cv2.imshow('Frame', frame)
bb = cv2.selectROI('Frame',frame) #ROI = Region Of Interest
tracker.init(frame,bb)
while True:
    ret , frame = v.read()
    if not ret:
        break
    (success,box) = tracker.update(frame)
    if success:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2) #(255,0,0),2 = code for box in red color
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF #use this if you want to exit the video
    if key == ord('q'):
        break
v.release()
cv2.destoyAllWindows()

    