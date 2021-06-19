import cv2
def take_snap_shot():
    vid=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = vid.read()
        cv2.imwrite('frame1.jpg', frame)
        result=False
    vid.release()
    cv2.destroyAllWindows()
take_snap_shot()