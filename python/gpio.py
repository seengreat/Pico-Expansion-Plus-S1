import time
import board
import digitalio



gp0 = digitalio.DigitalInOut(board.GP0)
gp0.direction = digitalio.Direction.OUTPUT

gp1 = digitalio.DigitalInOut(board.GP1)
gp1.direction = digitalio.Direction.OUTPUT

gp2 = digitalio.DigitalInOut(board.GP2)
gp2.direction = digitalio.Direction.OUTPUT

gp3 = digitalio.DigitalInOut(board.GP3)
gp3.direction = digitalio.Direction.OUTPUT

gp4 = digitalio.DigitalInOut(board.GP4)
gp4.direction = digitalio.Direction.OUTPUT

gp5 = digitalio.DigitalInOut(board.GP5)
gp5.direction = digitalio.Direction.OUTPUT

gp6 = digitalio.DigitalInOut(board.GP6)
gp6.direction = digitalio.Direction.OUTPUT

gp7 = digitalio.DigitalInOut(board.GP7)
gp7.direction = digitalio.Direction.OUTPUT

gp8 = digitalio.DigitalInOut(board.GP8)
gp8.direction = digitalio.Direction.OUTPUT

gp9 = digitalio.DigitalInOut(board.GP9)
gp9.direction = digitalio.Direction.OUTPUT

gp10 = digitalio.DigitalInOut(board.GP10)
gp10.direction = digitalio.Direction.OUTPUT

gp11 = digitalio.DigitalInOut(board.GP11)
gp11.direction = digitalio.Direction.OUTPUT

gp12 = digitalio.DigitalInOut(board.GP12)
gp12.direction = digitalio.Direction.OUTPUT

gp13 = digitalio.DigitalInOut(board.GP13)
gp13.direction = digitalio.Direction.OUTPUT

gp14 = digitalio.DigitalInOut(board.GP14)
gp14.direction = digitalio.Direction.OUTPUT

gp15 = digitalio.DigitalInOut(board.GP15)
gp15.direction = digitalio.Direction.OUTPUT

gp16 = digitalio.DigitalInOut(board.GP16)
gp16.direction = digitalio.Direction.OUTPUT

gp17 = digitalio.DigitalInOut(board.GP17)
gp17.direction = digitalio.Direction.OUTPUT

gp18 = digitalio.DigitalInOut(board.GP18)
gp18.direction = digitalio.Direction.OUTPUT

gp19 = digitalio.DigitalInOut(board.GP19)
gp19.direction = digitalio.Direction.OUTPUT

gp20 = digitalio.DigitalInOut(board.GP20)
gp20.direction = digitalio.Direction.OUTPUT

gp21 = digitalio.DigitalInOut(board.GP21)
gp21.direction = digitalio.Direction.OUTPUT

gp22 = digitalio.DigitalInOut(board.GP22)
gp22.direction = digitalio.Direction.OUTPUT

gp26 = digitalio.DigitalInOut(board.GP26)
gp26.direction = digitalio.Direction.OUTPUT

gp27 = digitalio.DigitalInOut(board.GP27)
gp27.direction = digitalio.Direction.OUTPUT

gp28 = digitalio.DigitalInOut(board.GP28)
gp28.direction = digitalio.Direction.OUTPUT

gpio = [gp0, gp1, gp2, gp3, gp4, gp5, gp6, gp7, gp8, gp9, gp10, gp11, gp12, gp13, gp14, gp15, gp16,
        gp17, gp18, gp19, gp20, gp21, gp22, gp26, gp27, gp28]
while True:
    for i,pio in enumerate(gpio):    
        pio.value = 1
#         print(i,pio.value)
        time.sleep(0.3)
        pio.value = 0
#         print(i,pio.value)
#         time.sleep(0.5)      

