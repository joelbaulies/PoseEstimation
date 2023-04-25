import cv2
import time
import PoseModule as pm


cap = cv2.VideoCapture('Videos/101.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.getPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 10, (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime- pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 70), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)