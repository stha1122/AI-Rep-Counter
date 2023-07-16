def bicepCurlCounter():
#to capture image from "WEBCAM"
    import cv2
    import cvzone
#to detect pose
    from cvzone.PoseModule import PoseDetector
#since there is one webcam 0 is passed to the function
    cap=cv2.VideoCapture(0)
    import numpy as np
    color=(0,0,255)
#direction
    dir=0
    curl_count=0
#detectionConfidence
    dectector=PoseDetector(detectionCon=0.69)

    while True:
    #read function returns two values that why two variables are used
        _,img=cap.read()

    #returns detected pose "POSE DETECTION"
        img=dectector.findPose(img)

    #dectect "LANDMARKS"
    #lmlst landmark list,bbox boundry box
        lmlst,bbox=dectector.findPosition(img,draw=False)

    # imshow()is used to display captured image and 'Bicep Curl Counter'is a window name


    #selecting landmarks
        if lmlst:

            angle=dectector.findAngle(img,16,14,12)
            bar_val=np.interp(angle,(22,170),(60,300+60))
            #bar_val2=np.interp(angle,(180,330),(60,300+60))
        #percentageValue
            per_val=np.interp(angle,(22,170),(100,0))
           # per_val2=np.interp(angle,(180,330),(100,0))
        #to show percentage of exercise
            cv2.rectangle(img,(540,int(bar_val)),(40+540,300+60),color,cv2.FILLED)
            #cv2.rectangle(img, (540, int(bar_val2)), (40 + 540, 300 + 60), (255,0,0), cv2.FILLED)
                         #  (x,y),(x+w,y+h)
            cv2.rectangle(img,(540,60),(40+540,300+60),(0,0,0),2)
        #cv2.rectangle(img, (1248, 64), (1311, 191), (0, 255, 0), 2)
        #(480, 640, 3)print(img.shape)

        #displaying percentage
            cvzone.putTextRect(img,f"{int(per_val)}%",(540,50),1.8,2,(255,255,255),color,border=2,colorB=())


        #print(angle)
            if per_val==100:
                if dir==0:
                    curl_count+=0.5
                    dir=1
                    color=(0,255,0)
            elif per_val==0:
                if dir ==1:
                    curl_count+=0.5
                    dir=0
                    color = (0, 255, 0)
            else:
                color = (0, 0, 255)


        #cvzone.putTextRect(img,"BICEP CURL COUNTER !!",(100,50),2,3,(255,255,255),(225,0,0),border=4,colorB=())
        cvzone.putTextRect(img,f"Count:{int(curl_count)}",(50,90),2,3,(255,255,255),(0,100,0),border=4,colorB=())


        cv2.imshow('Bicep Curl Counter', img)
    # we are checking for each millisecond if at all we have clicked 'q' to terminate the program
        if cv2.waitKey(1)==ord('q'):
            break
