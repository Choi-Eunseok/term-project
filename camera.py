import numpy as np
import cv2
import serial
from time import sleep

cut = 300

def merge_image(left_original, right_original):
    global cut
    
    wL, hL, cL = left_original.shape
    wR, hR, cR = right_original.shape

    crop_start = hL-cut-1
    
    left_gray = cv2.cvtColor(left_original, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_original, cv2.COLOR_BGR2GRAY)

    left_crop = left_gray[0:wL, crop_start:crop_start+cut].copy()

    left_min = 255
    for i in range(wL):
        for j in range(cut):
            if left_min > int(left_crop[i][j]):
                left_min = int(left_crop[i][j])

    able = {}
    
    for t in range(0,200):
        correct = 0
        right_crop = right_gray[0:wR,t:t+cut].copy()
        right_min = 255
        for i in range(wL):
            for j in range(cut):
                if right_min > int(right_crop[i][j]):
                    right_min = int(right_crop[i][j])
        for i in range(wL):
            for j in range(cut):
                if abs((int(left_crop[i][j]) - left_min) - (int(right_crop[i][j]) - right_min)) < 5:
                    correct += 1
        #print((correct/(wL*cut))*100)
        able[t] = (correct/(wL*cut))*100

    able_sort = sorted(able.items(), key = lambda item : item[1], reverse = True)

    result = cv2.hconcat([left_original[0:wL,0:crop_start+cut], right_original[0:wR,able_sort[0][0]+cut:hR]])
    result = cv2.line(result, (crop_start+cut, 0), (crop_start+cut, wL), (0, 0, 255), 1, cv2.LINE_AA)

    print(able_sort[0][0], able_sort[0][1], '-'*30)
    
    return result


arduino = serial.Serial('COM13', 9600)

cap = cv2.VideoCapture(1)

PICTURE_CNT = 17

sleep(5)

images = []

for i in range(PICTURE_CNT):
    c = str(int(360 / (PICTURE_CNT-1) * i)).encode('utf-8')
    arduino.write(c)
    while True:
        if arduino.readable():
            res = arduino.readline()
            print(res.decode()[:len(res)-1])
            break
    sleep(0.5)
    
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)

    cv2.imwrite('imageList/test' + str(i) + '.jpg', frame)
    print('imageList/test' + str(i) + '.jpg Saved Finished')
    w, h, c = frame.shape
    images.append(frame)


c = str(0).encode('utf-8')
arduino.write(c)

result = merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(merge_image(
    images[0], images[1]), images[2]), images[3]), images[4]), images[5]), images[6]), images[7]), images[8]), images[9]), images[10]), images[11]), images[12]), images[13]), images[14]), images[15]), images[16])
cv2.imwrite('imageList/result.jpg', result)
    
cap.release()
cv2.destroyAllWindows()


