import serial

arduino = serial.Serial('COM7', 9600)

while(1):
    c = input()
    if c=='q':
        arduino.close()
        break
    else:
        c= c.encode('utf-8')
        arduino.write(c)
        while True:
            if arduino.readable():
                res = arduino.readline()
                print(res.decode()[:len(res)-1])
                break
