import board 
import busio
import digitalio
import time
import bitbangio

NORMAL = 0
INVERTED   = 1
ROTATE_0   = 0
ROTATE_180 = 1
DOTTED = 0
SOLID  = 1
EMPTY  = 0
FULL   = 1

USE_IIC = 1

img  = [[0 for i in range(8)] for j in range(144)] # 144*18 bytes buffer

class OLED_0IN96():
    def __init__(self):
        print("gpio init")
        if USE_IIC == 0:
            self.spi = busio.SPI(clock=board.GP6, MOSI=board.GP7)
            while not self.spi.try_lock():
                pass
            self.spi.configure(baudrate=5000000, phase=0, polarity=0)
            self.cs = digitalio.DigitalInOut(board.GP5)
            self.cs.direction = digitalio.Direction.OUTPUT
            self.cs.value = True
            self.dc = digitalio.DigitalInOut(board.GP9)
            self.dc.direction = digitalio.Direction.OUTPUT
            self.dc.value = True
        if USE_IIC == 1:
            self.i2c = bitbangio.I2C(scl=board.GP6, sda=board.GP7, frequency=400000)
            while not self.i2c.try_lock():
                pass
            self.addr_list = self.i2c.scan()
            self.addr = self.addr_list[0] # when only one i2c slave device wiring in board
            print(hex(self.addr))

        self.rst = digitalio.DigitalInOut(board.GP8)
        self.rst.direction = digitalio.Direction.OUTPUT
        self.rst.value = True
        self.w = 128
        self.h = 64
        print("init finish")
        
    def write_cmd(self,cmd):
        if USE_IIC == 0:
            self.dc.value = False
            self.cs.value = False
            self.spi.write(bytes([cmd]))
            self.cs.value = True
            self.dc.value = True           
        elif USE_IIC == 1:
            temp = [0x00, 0x00]
            temp[1] = cmd
            self.i2c.writeto(self.addr,bytes(temp)) 

    def write_data(self,data):
        if USE_IIC == 0:
            self.dc.value = True
            self.cs.value = False
            self.spi.write(bytes([data]))
            self.cs.value = True
            self.dc.value = True          
        elif USE_IIC == 1:
            temp = [0x40, 0x00]
            temp[1] = data
            self.i2c.writeto(self.addr,bytes(temp))  
        
    def display_mode(self, mode):
        if mode == NORMAL:
            self.write_cmd(0xA6)
        elif mode == INVERTED:
            self.write_cmd(0xA7)
    
    def display_rotate(self, rotate):
        if rotate == ROTATE_0:
            self.write_cmd(0xC8)
            self.write_cmd(0xA1)
        if rotate == ROTATE_180:
            self.write_cmd(0xC0)
            self.write_cmd(0xA0)
            
    def display_on(self):
        self.write_cmd(0x8D)
        self.write_cmd(0x14)
        self.write_cmd(0xAF)

    def display_off(self):
        self.write_cmd(0x8D)
        self.write_cmd(0x10)
        self.write_cmd(0xAE)
        
    def refresh(self):
        for i in range(8):
            self.write_cmd(0xB0+i)
            self.write_cmd(0x00)
            self.write_cmd(0x10)
            if USE_IIC == 0:
                for j in range(128):
                    self.write_data(img[j][i])
            elif USE_IIC == 1:
                data = [0x40]
                for j in range(128):
                    data.append(img[j][i])
                self.i2c.writeto(self.addr,bytes(data)) 
                
    def clear(self):
        for i in range(8):
            for j in range(128):
                img[j][i] = 0
        self.refresh()
        
    def init(self):
        self.rst.value = False
        time.sleep(0.2)
        self.rst.value = True
        
        self.write_cmd(0xAE)
        self.write_cmd(0x00)
        self.write_cmd(0x10)
        self.write_cmd(0x40)
        self.write_cmd(0x81)
        self.write_cmd(0xCF)
        self.write_cmd(0xA1)
        self.write_cmd(0xC8)
        self.write_cmd(0xA6)
        self.write_cmd(0xA8)
        self.write_cmd(0x3F)
        self.write_cmd(0xD3)
        self.write_cmd(0x00)
        self.write_cmd(0xD5)
        self.write_cmd(0x80)
        self.write_cmd(0xD9)
        self.write_cmd(0xF1)
        self.write_cmd(0xDA)
        self.write_cmd(0x12)
        self.write_cmd(0xDB)
        self.write_cmd(0x40)
        self.write_cmd(0x20)
        self.write_cmd(0x02)
        self.write_cmd(0x8D)
        self.write_cmd(0x14)
        self.write_cmd(0xA4)
        self.write_cmd(0xA6)
        self.clear()
        self.write_cmd(0xAF)





    
    
    

