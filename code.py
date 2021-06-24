import cv2

numberPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500
width = 640
height = 480
count = 0

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
cap.set(10,90)

while True:
    success,img=cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea :
            cv2.rectangle(img,(x,y),(x+w,y+h),(50,255,0),4)
            cv2.putText(img,"numberPlate",(x,y-5), cv2.FONT_HERSHEY_PLAIN,1.5,(70,255,0),2)    
            regOfInterest = img[y:y+h,x:x+w] 
            cv2.imshow("Video1", regOfInterest)
    
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("#PATH_"+str(count)+".jpg", regOfInterest)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.imshow("Video", img)
        cv2.waitKey(500)
        count+=1     
        
    
        
cap.release()
cv2.destroyAllWindows()
