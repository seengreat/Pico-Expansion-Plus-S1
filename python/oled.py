from drv_096_oled import drv_oled,font
import time

class OLED_GUI():
    def __init__(self):
        self.oled = drv_oled.OLED_0IN96()
        self.oled.init()
        self.oled.display_on()
        self.oled.display_mode(drv_oled.NORMAL)
        self.oled.display_rotate(drv_oled.ROTATE_0)
    def set_pixel(self, x, y):
        i = int(y/8)
        m = int(y%8)
        n = 1<<m;
        drv_oled.img[x][i] |= n
        
    def draw_point(self, x, y, width):
        if x>self.oled.w or y>self.oled.h:
            print("ERR:point out of screen area!")
            return
        for xd in range(width):
            for yd in range(width):
                if x+xd > self.oled.w or y+yd > self.oled.h:
                    continue
                self.set_pixel(x+xd-1, y+yd-1)
    # Bresenham circle algorithm draw line    
    def draw_line(self, x1, y1, x2, y2, width, line_type):
        x = x1
        y = y1
        dx = x2-x1 if x2-x1 > 0 else x1-x2
        dy = y2-y1 if y2-y1 > 0 else y1-y2
        p = dx-dy;
        xdir = -1 if x1>x2 else 1
        ydir = -1 if y1>y2 else 1
        dot_cnt = 0
        while True:
            dot_cnt += 1
            if line_type == drv_oled.DOTTED and dot_cnt%3 == 0:
                self.draw_point(x, y, width)
            elif line_type == drv_oled.SOLID:
                self.draw_point(x, y, width)
            if x == x2 and y==y2:
                break
            e2 = int(2*p)
            if e2 >= -dy:
                p -= dy
                x += xdir
            if e2 <= dx:
                p += dx
                y += ydir
    def draw_rectangle(self, x1, y1, x2, y2, width, fill):
        if x1> self.oled.w or y1 > self.oled.h or x2 > self.oled.w or y2 > self.oled.h:
            print("ERR:line point out of screen area!")
            return 
        if fill == drv_oled.FULL:
            for i in range(y1, y2):
                self.draw_line(x1, i, x2, i, width, drv_oled.SOLID)
        elif fill==drv_oled.EMPTY:
            self.draw_line(x1, y1, x2, y1, width, drv_oled.SOLID)
            self.draw_line(x1, y1, x1, y2, width, drv_oled.SOLID)
            self.draw_line(x1, y2, x2, y2, width, drv_oled.SOLID)
            self.draw_line(x2, y1, x2, y2, width, drv_oled.SOLID)
    # Bresenham circle algorithm draw circle
    def draw_circle(self, x, y, r, width, fill):
        dx=0
        dy=r
        d = int(1-r)
        if x>self.oled.w or y > self.oled.h:
            print("ERR:circle center point out of screen area!")
            return 
        while dy>dx:
            if fill==drv_oled.EMPTY:
                self.draw_point(x+dx, y+dy, width)
                self.draw_point(x+dy, y+dx, width)
                self.draw_point(x-dx, y+dy, width)
                self.draw_point(x-dy, y+dx, width)
                self.draw_point(x-dx, y-dy, width)
                self.draw_point(x-dy, y-dx, width)
                self.draw_point(x+dx, y-dy, width)
                self.draw_point(x+dy, y-dx, width)
            elif fill==drv_oled.FULL:
                for i in range(dx, dy+1):
                    self.draw_point(x+dx, y+i, width)
                    self.draw_point(x+i, y+dx, width)
                    self.draw_point(x-dx, y+i, width)
                    self.draw_point(x-i, y+dx, width)
                    self.draw_point(x-dx, y-i, width)
                    self.draw_point(x-i, y-dx, width)
                    self.draw_point(x+dx, y-i, width)
                    self.draw_point(x+i, y-dx, width)                
            if d<0:
                d += 2*dx+3    
            else:
                d += 2*(dx-dy)+5
                dy -= 1
            dx += 1
            
    def draw_char(self, x, y, text_char, size):
        x0=x
        y0=y
        if size==8:
            char_nbytes = 6
        else :
            temp = 1 if int(size%8) else 0
            char_nbytes=int((int(size/8)+temp)*(size/2)) #得到字体一个字符对应点阵集所占的字节数
        offset = int(ord(text_char) - ord(' ')) # 计算偏移后的值
        for i in range(char_nbytes):
            if size==8:
                temp=font.asc2_0806[offset][i] #call 0806 font
            elif size==12:
                temp=font.asc2_1206[offset][i] #call 1206 font
            elif size==16:
                temp=font.asc2_1608[offset][i] #call 1608 font
            elif size==24:
                temp=font.asc2_2412[offset][i] #call 2412 font
            else :
                return
            for m in range(8):
                if temp&0x01:
                    self.set_pixel(x,y)
                temp>>=1
                y += 1
            x += 1
            if size!=8 and (x-x0)==size/2:
                x=x0
                y0=y0+8
            y=y0

    def draw_str(self, x, y, text_str, size):
        i = 0
        while True:
            if text_str[i]>=' ' and text_str[i]<='~' :  #判断是不是非法字符!
                self.draw_char(x, y, text_str[i], size)
                if size == 8:
                    x += 6
                else :
                    x += int(size/2)
                i += 1
                if i == len(text_str):
                    break

if __name__=='__main__':
    gui = OLED_GUI()
    while True:
        gui.oled.clear()
        gui.draw_point(5,5,4)
        gui.draw_line(1, 30, 128, 64, 2, drv_oled.SOLID)
        gui.draw_rectangle(30, 2, 40, 12, 1, drv_oled.EMPTY)
        gui.draw_rectangle(50, 2, 60, 12, 1, drv_oled.FULL)
        gui.draw_circle(80,8,7,1,drv_oled.EMPTY)
        gui.draw_circle(110,8,7,2,drv_oled.FULL)
        gui.oled.refresh()
        time.sleep(2)
        gui.oled.clear()
        gui.draw_str(2, 1, "0.96inch oled", 16)
        gui.draw_str(2, 16, "0123456789", 16)
        gui.draw_str(2, 35, "SEENGREAT", 24)
        gui.oled.refresh()
        time.sleep(2)
