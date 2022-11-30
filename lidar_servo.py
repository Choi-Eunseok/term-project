import serial
from time import sleep
import math
import numpy as np
from stl import mesh

def recieve():
    while True:
        if arduino.readable():
            res = arduino.readline()
            print(res.decode()[:len(res)-1])
            return int(res.decode()[:len(res)-1])
            break

distance_list = []

arduino = serial.Serial('COM13', 9600)

sleep(6)

arduino.write(str(1000).encode('utf-8'))
num = recieve()+1

for i in range(num):
    temp = recieve()
    if temp > 1200:
        temp = distance_list[-1]
    distance_list.append(temp)

arduino.close()

location_list = []
face_list = []

for i in range(num):
    location_list.append([(distance_list[i] * 10*math.sin((i+1)*math.pi*2/150)), (distance_list[i] * 10*math.cos((i+1)*math.pi*2/150)), 0])
    location_list.append([(distance_list[i] * 10*math.sin((i+1)*math.pi*2/150)), (distance_list[i] * 10*math.cos((i+1)*math.pi*2/150)), 100])

    if i > 0:
        face_list.append([2*i, 2*i-1, 2*i-2])
        face_list.append([2*i+1, 2*i-1, 2*i])

vertices = np.array(location_list)
faces = np.array(face_list)

cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        print(vertices[f[j],:])
        cube.vectors[i][j] = vertices[f[j]]

cube.save('test.stl')
