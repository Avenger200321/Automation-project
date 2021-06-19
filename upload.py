import cv2
import dropbox
import time 
import random

start_time = time.time()
def take_snapshot():
    number=random.randint(0,100)
    vid=cv2.VideoCapture(0)
    result = True 
    while(result):
        ret,frame =vid.read()
        img_name= 'img' + str(number)+ '.png'
        cv2.imwrite(img_name, frame)
        start_time=time.time
        result= False
    print('Snapshot Taken')
    vid.release()
    cv2.destroyAllWindows()
    return img_name
def upload_file(img_name):
    access_token='sl.AyhyhjPKU3pW0oDlH1at4ydYgsCUyOp_Se4R2Fhd4oyivudsr7TATkeuI2nVbt1odlxO2s_Jn3RG8wwL8Qz4c9GE9Wid8KFaG0fTu1eooXmhD5nLqQMjUXCfvsjFxxHQGQzxPRVJ1wo'
    file=img_name
    filefrom=img_name
    fileto='/security camera/'+img_name
    dbx=dropbox.Dropbox(access_token)
    with open(filefrom,'rb')as F:
        dbx.files_upload(F.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('File uploaded')
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()