from matplotlib import pyplot as plt
import numpy as np
import math
import serial

port = serial.Serial('COM4', 9600, timeout=1)






g = 9.8
k = float(input())
m = float(input())
f_time = float(input()) # время на которое мы моделируем 

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        data = float(port.readline().decode('utf-8').strip())
        print(data)
    except:
        continue

    f_x = data * f_time

    ang = math.acos(
        (k * f_x / m) /
        math.sqrt(
            (k * f_x / m)**2 +
            (g * (f_time - m / k * (1 - math.exp(-k * f_time / m))))**2
        )
    )

    v_start = math.sqrt(
        (k * f_x / (m * (1 - math.exp(-k * f_time / m))))**2 +
        (g * (f_time / (1 - math.exp(-k * f_time / m)) - m / k))**2
    )

    t = np.linspace(0, f_time, 500)

    xt = v_start*math.cos(ang) * m/k *(1 - np.exp(-k*t/m))
    yt = (v_start*math.sin(ang)*m/k+m*m*g/k**2)*(1-np.exp(-k*t/m)) - m*g*t/k

    ax.clear()
    ax.plot(xt, yt)

    fig.canvas.draw()
    fig.canvas.flush_events()

    plt.pause(0.01)