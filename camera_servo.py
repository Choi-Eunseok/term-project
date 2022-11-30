import numpy as np
import cv2
import RPi.GPIO as GPIO
from time import sleep

cap = cv2.VideoCapture(-1)

PICTURE_CNT = 6

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12, 50)
servo.start(0)

currentDegree = -1

def setServoPos(goalDegree):
  global currentDegree
  
  if goalDegree > 180:
    goalDegree = 180

  while currentDegree != goalDegree:
    if currentDegree > goalDegree:
      currentDegree -= 10
    else:
      currentDegree += 10
    
    if abs(currentDegree - goalDegree) < 10:
      currentDegree = goalDegree
      
    duty = 3+(currentDegree*9/180.0)
    print("Current_Degree: {} to {}(Duty)".format(currentDegree, duty))
    servo.ChangeDutyCycle(duty)
    sleep(0.075)

for i in range(PICTURE_CNT):
    setServoPos(int(170 / PICTURE_CNT * i))

    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)

    cv2.imwrite('test' + str(i) + '.jpg', frame)
    
    sleep(0.5)

setServoPos(0)

cap.release()
cv2.destroyAllWindows()

servo.stop()
GPIO.cleanup()
