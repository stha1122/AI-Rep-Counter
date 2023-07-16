import time

import cvzone


def puspUpConuter():
    import cv2
    import numpy as np
    from cvzone.PoseModule import  PoseDetector
    cap=cv2.VideoCapture(0)
    detector = PoseDetector(detectionCon=0.5)
    ptime=0 #previous time
    ctime=0 #corrct time
    colorr=(0,0,255)
    dir=0#direction
    count=0
    while True:
        _,img = cap.read()
        img=detector.findPose(img)
        lmlst,bbox=detector.findPosition(img,draw=False)
        if lmlst:
            #print(lmlst)
            a1=detector.findAngle(img,12,14,16)
            a2=detector.findAngle(img,15,13,11)
            per_val1=int(np.interp(a1,(80,175),(100,0)))
            per_val2 = int(np.interp(a2, (80, 175), (100, 0)))
            bar_val1=int(np.interp(per_val1, (0, 100), (40+350, 40)))
            bar_val2 = int(np.interp(per_val2, (0, 100), (40 + 350, 40)))
            #1st bar
            cv2.rectangle(img, (570, bar_val1), (570 + 35, 40 + 350),colorr, cv2.FILLED)
            cv2.rectangle(img,(570,40),(570+35,40+350),(),3)
            #bar1 %
            cvzone.putTextRect(img, f'{per_val1} %', (570, 25), 1.1, 2, colorT=(255, 255, 255), colorR=colorr, border=3,
                               colorB=())

            #2nd bar
            cv2.rectangle(img, (35, bar_val2), (35 + 35, 40 + 350),colorr, cv2.FILLED)
            cv2.rectangle(img, (35, 40), (35 + 35, 40 + 350), (), 3)
            # bar2 %
            cvzone.putTextRect(img,f'{per_val2} %',(30,25),1.1,2,colorT=(255,255,255),colorR=colorr,border=3,colorB=())
            if per_val1==100 and per_val2==100:
                if dir==0:
                    count+=0.5
                    dir=1
                    colorr=(0,255,0)
            elif per_val1==0 and per_val2==0:
                if dir==1:
                    count += 0.5
                    dir = 0
                    colorr=(0,255,0)
            else:
                color=(0,0,255)
                #print(count)
            cvzone.putTextRect(img,f'Push Ups:{int(count)}',(218,35),2,2,colorT=(255,255,255),colorR=(255,0,0),border=3,colorB=())
            cvzone.putTextRect(img, 'Left Hand', (15, 350+80), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0),
                               border=3, colorB=())
            cvzone.putTextRect(img, 'Right Hand', (495, 350+80), 2, 2, colorT=(255, 255, 255), colorR=(255, 0, 0),
                               border=3, colorB=())
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cvzone.putTextRect(img,f'FPS:{int(fps)}',(285,440),1.6,2,colorT=(255,255,255),colorR=(0,135,0),border=2,colorB=())
        cv2.imshow('Push-Ups Counter',img)
        cv2.waitKey(1)
        if cv2.waitKey(1)==ord('q'):
            break


