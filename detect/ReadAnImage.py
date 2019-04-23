import cv2
choice = input('Enter 1 to use Webcam, anything else to read an image from a file')
if choice == '1':
    print('Press Q to quit the image window')
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('image', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    path = input('Enter the path for the image from this folder')
    img = cv2.imread(path,0)
    cv2.imshow('images', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()