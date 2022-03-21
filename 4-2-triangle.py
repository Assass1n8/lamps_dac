import RPi.GPIO as GP
import time
def two_binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GP.setup(dac, GP.OUT)
k = 0
T = float(input('Период T: '))

try:
    while True:
        for i in range(8):
            GP.output(dac[i], two_binary(k)[i])

        k += 1
        time.sleep(T)

finally:
    GP.output(dac, 0)
    GP.cleanup()
