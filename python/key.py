import time
import board
import digitalio



k1 = digitalio.DigitalInOut(board.GP26)
k1.direction = digitalio.Direction.INPUT
k1.pull = digitalio.Pull.UP

k2 = digitalio.DigitalInOut(board.GP21)
k2.direction = digitalio.Direction.INPUT
k2.pull = digitalio.Pull.UP

k3 = digitalio.DigitalInOut(board.GP20)
k3.direction = digitalio.Direction.INPUT
k3.pull = digitalio.Pull.UP

k1_flag = 0
k2_flag = 0
k3_flag = 0
while True:
    if (k1.value == 0 and k1_flag == 0):
        time.sleep(0.01)
        if k1.value == 0:
            print("k1 is press")
            k1_flag = 1
    elif (k1.value==1 and k1_flag == 1):
        k1_flag = 0
        
    if (k2.value == 0 and k2_flag == 0):
        time.sleep(0.01)
        if k2.value == 0:
            print("k2 is press")
            k2_flag = 1
    elif (k2.value==1 and k2_flag == 1):
        k2_flag = 0
        
    if (k3.value == 0 and k3_flag == 0):
        time.sleep(0.01)
        if k3.value == 0:
            print("k3 is press")
            k3_flag = 1
    elif (k3.value==1 and k3_flag == 1):
        k3_flag = 0
        
