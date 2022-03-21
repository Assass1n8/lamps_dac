import RPi.GPIO as GP
GP.setmode(GP.BCM)
GP.setup(22, GP.OUT)

p = GP.PWM(22, 1000)
p.start(0)

try:
    while True:
        i = int(input())
        p.ChangeDutyCycle(i)
        print(3.26*i/100)

finally:
    GP.output(22, 0)
    GP.cleanup()

