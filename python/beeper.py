import pwmio
import board
import time

# pwm = pwmio.PWMOut(board.D18, duty_cycle=2 ** 15, frequency=440, variable_frequency=True)
# time.sleep(0.2)
# pwm.frequency = 880
# time.sleep(0.1)

# 定义音调频率
tones = {'L1': 175, 'L2': 196, 'L3': 221, 'L4': 234, 'L5': 262, 'L6': 294, 'L7': 330,
         '1': 350, '2': 393, '3': 441, '4': 495, '5': 556, '6': 624, '7': 661,
         'H1': 700, 'H2': 786, 'H3': 882, 'H4': 935, 'H5': 965, 'H6': 996, 'H7': 1023, '0': 0}
# 定义小星星旋律
little_star = "1155665-4433221-5544332-5544332-1155665-4433221"
jingle_bells = ["5","H3","H2","H1","5","0","5","5",  "5","H3","H2","H1","6","0","6","6",  "6","H4","H3","H2","7","0",  "H5","H5","H4","H2","H3","0","5","5",
                "5","H3","H2","H1","5","0","5","5",  "5","H3","H2","H1","6","0","6","6",  "6","H4","H3","H2","H5","H5","H5",  "H6","H5","H4","H2","H1","0",
                "H3","H3","H3","H3","H3","H3",   "H3","H5","H1","H2","H3","0",   "H4","H4","H4","H4","H3","H3",  "H3","H2","H2","H1","H2","H5",
                "H3","H3","H3","H3","H3","H3",   "H3","H5","H1","H2","H3","0",   "H4","H4","H4","H4","H3","H3",  "H5","H5","H4","H2","H1","0",
                "5","H3","H2","H1","5","0","5","5",  "5","H3","H2","H1","6","0","6","6",  "6","H4","H3","H2","7","0",  "H5","H5","H4","H2","H3","0","5","5",
                "5","H3","H2","H1","5","0","5","5",  "5","H3","H2","H1","6","0","6","6",  "6","H4","H3","H2","H5","H5","H5",   "H6","H5","H4","H2","H1","0",
                "H3","H3","H3","H3","H3","H3",   "H3","H5","H1","H2","H3","0",   "H4","H4","H4","H4","H3","H3",  "H3","H2","H2","H1","H2","H5",
                "H3","H3","H3","H3","H3","H3",   "H3","H5","H1","H2","H3","0",   "H4","H4","H4","H4","H3","H3",  "H5","H5","H4","H2","H1","0",
                "H1","H5","H1"]
jingle_bells_delay = [2,2,2,2,4,2,1,1, 2,2,2,2,4,2,1,1, 2,2,2,2,4,4, 2,2,2,2,4,2,1,1,
                       2,2,2,2,4,2,1,1, 2,2,2,2,4,2,1,1, 2,2,2,2,2,2,4, 2,2,2,2,4,4,
                       2,2,4,2,2,4, 2,2,2,1,4,4, 2,2,4,2,2,4, 2,2,2,2,4,4,
                       2,2,4,2,2,4, 2,2,2,1,4,4, 2,2,4,2,2,4, 2,2,2,2,4,4,
                       2,2,2,2,4,2,1,1, 2,2,2,2,4,2,1,1, 2,2,2,2,4,4, 2,2,2,2,4,2,1,1,
                       2,2,2,2,4,2,1,1, 2,2,2,2,4,2,1,1, 2,2,2,2,2,2,4, 2,2,2,2,4,4,
                       2,2,4,2,2,4, 2,2,2,1,4,4, 2,2,4,2,2,4, 2,2,2,2,4,4,
                       2,2,4,2,2,4, 2,2,2,1,4,4, 2,2,4,2,2,4, 2,2,2,2,4,4,
                       4,4,4]
# 设置D7（GPIO 13）口为IO输出，然后通过PWM控制无缘蜂鸣器发声
beeper = pwmio.PWMOut(board.GP18, duty_cycle=0x7fff, frequency=330, variable_frequency=True)

i = 0
for tone in jingle_bells:
    freq = tones[tone]
    if freq:
        beeper.duty_cycle = 0x7fff
        beeper.frequency = freq
#          beeper.init(duty_cycle=1000, freq=freq)  # 调整PWM的频率，使其发出指定的音调       
    else:
        beeper.duty_cycle = 0  # 空拍时一样不上电
    # 停顿一下 （四四拍每秒两个音，每个音节中间稍微停顿一下）
    time.sleep(jingle_bells_delay[i]*0.1)
    beeper.duty_cycle = 0  # 设备占空比为0，即不上电
    time.sleep(0.1)
    i += 1
# 
beeper.deinit()  # 释放PWM