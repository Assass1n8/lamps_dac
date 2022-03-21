import RPi.GPIO as GP
def two_binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GP.setup(dac, GP.OUT)


try:
    num = input()
    if '.' in num:
        print('Число не целое')  
    elif int(num) < 0:
        print('Число отрицательное')
    elif int(num) > 255:
        print('Число превышает возможности ЦАП')

    
    while num != 'q':
        for i in range(8):
            GP.output(dac[i], two_binary(int(num))[i])
        num = int(input('Введи число: '))


finally:
    GP.output(dac, 0)
    GP.cleanup()