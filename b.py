import cv2
import dropbox
import time
import random


start_time = time.time()


def take_snapshot():
    # initializing cv2
    num = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        # print(frame)
        img_name = "img"+str(num)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot complete")
    # releases the camera
    videoCaptureObject.release()
    # closes all the window that might be opened while this process
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.AnO4SLTnOtjaAhhyrpBGgjKq6ttLdv1qwmNMJpIw82yoGKbfZZZwzBQTUcp7B5129ZjiyBYdVax7GO_S9eKNZp6XVHiq1ZOlX2WZ0BHvv_acz4_BmLqSWCcVE7som9zmS6_FLIM"
    file_from = 'D:/Coding Class/Python/c102/'+img_name
    file_to = '/Dropbox/'+img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("Files uploaded")



def main():
    while(True):
        if((time.time()-start_time) >= 10):
            name = take_snapshot()
            upload_file(name)

main()
