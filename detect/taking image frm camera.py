import numpy as np
import cv2
def nothing(x):
    # any operation
    pass
 
cap = cv2.VideoCapture(0)
 

 
font = cv2.FONT_HERSHEY_COMPLEX
 
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([180, 255, 176])
 
    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
 
    # Contours detection
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
 
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
 
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 5:
                cv2.putText (frame, "pentagon", (x, y), font, 1,(0,0,0))
            elif len(approx) == 5:
                cv2.putText (frame, "hexagon", (x,y),font, 1,(0,0,0))
            elif 10 < len(approx) < 20:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
 
 
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
