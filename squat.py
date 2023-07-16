def sitUpCounter():
    import cv2
    from cvzone.PoseModule import PoseDetector
    import numpy as np
    import cvzone
    cap=cv2.VideoCapture(0)
    detector=PoseDetector(detectionCon=0.5)
    per=0
    angle=0
    color=(0,0,255)
    count=0
    dir=0
    while True:
        _,img=cap.read()
        img=detector.findPose(img)
        lmlst,bbox=detector.findPosition(img,False)
        if lmlst:
            angle=detector.findAngle(img,24,26,28)
            per=np.interp(angle,(100,170),(100,0))
            bar_value=np.interp(angle,(100,170),(15,15+300))
            cv2.rectangle(img, (580, int(bar_value)), (580 + 30, 15 + 300),color, cv2.FILLED)
            cv2.rectangle(img,(580,15),(580+30,15+300),(),2)
            cvzone.putTextRect(img, f"{int(per)}%", (575, 350), 1.0, 2, (255, 255, 255), color, border=2, colorB=())
            if per==100:
                if dir==0:
                    dir=1
                    count+=0.5
                    color=(0,255,0)
            elif per==0:
                if dir==1:
                    dir=0
                    count+=0.5
                    color = (0, 255, 0)
            else:
                color = (0, 0, 255)
        cvzone.putTextRect(img, f"Count:{int(count)}", (30, 40), 2, 2, (255, 255, 255), (0, 100, 0), border=0,
                           colorB=())
        cv2.imshow('Squat Counter',img)
        if cv2.waitKey(1) == ord('q'):
            break

