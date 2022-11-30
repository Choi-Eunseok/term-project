import numpy as np
import cv2

cut = 10

def merge_image(left_original, right_original):
    global cut
    
    w, h, c = left_original.shape

    crop_start = h-cut-10
    
    left_gray = cv2.cvtColor(left_original, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_original, cv2.COLOR_BGR2GRAY)

    left_crop = left_gray[0:w, crop_start:crop_start+cut].copy()

    able = {}
    
    for t in range(h-cut-1, -1, -1):
        correct = 0
        right_crop = right_gray[0:w,t:t+cut].copy()
        for i in range(w):
            for j in range(cut):
                if abs(int(left_crop[i][j]) - int(right_crop[i][j])) < 5:
                    correct += 1
        print((correct/(w*cut))*100)
        able[t] = (correct/(w*cut))*100

    able_sort = sorted(able.items(), key = lambda item : item[1], reverse = True)

    result = cv2.hconcat([left_original[0:w,0:crop_start+cut], right_original[0:w,able_sort[0][0]+cut:h]])
    result = cv2.line(result, (able_sort[0][0]+cut, 0), (able_sort[0][0]+cut, w), (0, 0, 255), 1, cv2.LINE_AA)

    return result
    

cap = cv2.VideoCapture(1)

cap.set(3, 620)
cap.set(4, 480)

ret1, frame1 = cap.read()
cv2.imshow("1", frame1)

ret2, frame2 = cap.read()
cv2.imshow("2", frame2)

result = merge_image(frame1, frame2)

cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()
