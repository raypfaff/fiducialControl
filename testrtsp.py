import cv2
import apriltag
import json
import zmq
'''
git clone https://github.com/guozhenglong/AprilTags
This is my camera calibration:
Performing calibration...
RMS: 0.32145282166889577
camera matrix:
 [[276.51675557   0.         210.79076866]
 [  0.         298.57771571 131.35965042]
 [  0.           0.           1.        ]]
distortion coefficients:  [ 0.02845336 -0.04922906 -0.00383786 -0.00396503 -0.36600082]
'''
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.bind("tcp://*:5555")
index =0
output={}
got_image = True
#vcap = cv2.VideoCapture("rtsp://{USR:PASWD@IP}/webcam")
while(1):
    vcap = cv2.VideoCapture("rtsp://{USR:PASSWD@IP}/webcam")
    ret, frame = vcap.read()
    #print ('got frame')
    if got_image:
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       detector = apriltag.Detector()
       result = detector.detect(gray)
       # Init the json - adding roll, pitch, yaw later
       output['x']=-1
       output['y']=-1
       output['z']=-1
       output['id']=-1
       if len(result) >0 :
          # There can be more than one fiducial.  At the moment, look
          # at the first one.
          result2 = detector.detection_pose(result[0],(276.51675557, 298.57771571, 210.79076866, 131.35965042))
          # This also comes back as an array,  I'm not sure why
          # there would be more than one position matrix
          coords=result2[0]
          output['x']=coords[0][3]
          output['y']=coords[1][3]
          output['z']=coords[2][3]
          output['id']=result[0].tag_id
       #cv2.imshow('VIDEO', frame)
       #cv2.waitKey(1)
       sendit=json.dumps(output)
       #print (sendit)
       socket.send_string(sendit)
    try:
       foo = socket.recv(flags=zmq.NOBLOCK)
       got_image=True
    except zmq.Again as e:
       got_image=False
    cv2.VideoCapture.release(vcap)
