import cv2

def cam():
    webcam = cv2.VideoCapture(0)

    if webcam.isOpened():
        ver,frame = webcam.read()
        while ver:
            ver,frame = webcam.read()
            cv2.imshow("Webcam",frame)
            tecla = cv2.waitKey(5)
            if tecla ==27:
                break
            elif tecla == 115:
                cv2.imwrite('img.jpg',frame)
                break

    webcam.release()
    cv2.destroyAllWindows()