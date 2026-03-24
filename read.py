from matplotlib import pyplot as plt
import numpy as np
import math
import serial

port = serial.Serial('COM5', 9600, timeout=1)






g = 9.8
k = float(input())
m = float(input())
f_time = float(input()) # время на которое мы моделируем 

while True:

    isfloat = False
    while isfloat != True:
            try:
                data = float(port.readline().decode('utf-8').strip())
                isfloat = True
            except ValueError:
                 pass


    f_x = data * f_time

    ang = math.acos(  
    (k * f_x / m) /
    math.sqrt(
        (k * f_x / m)**2 +
        (g * (f_time - m / k * (1 - math.exp(-k * f_time / m))))**2
        )
    ) # подсчет угла в радианах

    v_start = math.sqrt(
    (k * f_x / (m * (1 - math.exp(-k * f_time / m))))**2 +
    (g * (f_time / (1 - math.exp(-k * f_time / m)) - m / k))**2
    ) # подсчет модуля начальной скорости



    t = np.linspace(0, f_time, 30000)

    xt = v_start*math.cos(ang) * m/k *(1 - np.exp(-k*t/m))
    yt = (v_start*math.sin(ang)*m/k+m*m*g/k**2)*(1-np.exp(-k*t/m)) - m*g*t/k

    plt.ion()
    
    plt.plot(xt, yt) 
    plt.show()
    plt.pause(2)

    plt.clf()