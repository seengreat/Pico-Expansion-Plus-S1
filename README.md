Pico-Expansion-Plus-S1 from seengreat:www.seengreat.com
 =======================================
# Ⅰ  Instructions
## 1.1、Product Overview
Pico Expansion Plus S1 is an upgraded expansion board specially designed for the Raspberry Pi Pico. It not only has the status indicator LED lights of all GPIOs in Pico of Pico Expansion Plus version, two sets of 2 * 20PIN pin array headers, four HY-2.0-4P headers, one set of SPI1 pin array and one reset button, but also adds one Full-color RGB, onboard Micro SD card slot, buzzer with switch, and one 2.54mm 4PIN header array for DHT11/DS18B20 sensors, There is also a standard 3.5mm audio jack.<br>
Raspberry Pi Pico does not have a reset button, but this product increases the reset button, so it is convenient for users to debug or write programs without frequent plugging USB line of Pico.<br>
## 1.2、Product parameters
Size	114mm(L)*78.5mm(W)*11mm(H)
Supply voltage	5V(provided by PICO)

## 1.3、Product dimensions
Size	114mm(L)*78.5mm(W)*11mm(H)
Weight	50ｇ
# Ⅱ  Usage
## 2.1、Resource introduction
 Module pin definition is shown in the figure below:<br>
![image](https://github.com/seengreat/Pico-Expansion-Plus-S1/blob/main/Pico%20Expnsion%20PLUS%20S1.png)
& PICO external expansion pins<br>
 Raspberry Pi Pico socket<br>
 The selective switch of GPIO LED<br>
 indicators to display the GPIO status<br>
 The selective switch of voltage for 4<br>
    HY-2.0-4P connectors<br>
 SPI interface<br>
 DHT11/DS18B20 header<br>
 Expansion board power indicator<br>
 PICO reset button<br>
 User keys<br>
 3.5mm audio jack<br>
 4 HY-2.0-4P connectors<br>
 Micro SD card slot<br>
 ESP-01 solder joint<br>
 Full-color RGB (WS2812)<br>
 Buzzer switch<br>
 Passive buzzer<br>
GPIO LED Indicators: The GPIO status display function can be turned on by toggling the switch S1 to the ON state. At this time, when the GPIO is at a high level, the corresponding LED indicator light is on, otherwise the light is off. If you do not need to display the GPIO status through the LED status, you can turn the switch S1 to the OFF state.<br>
It is easy of Two sets of 2*20 pins to access to the Raspberry Pi Pico expansion board or dupont wire to peripherals. <br>Both sides of the board are marked with clear<br>
pin function silk screen, which is convenient for use and measurement.<br>
The 4 HY-2.0-4P connectors can be inserted into 2.0mm-spaced cables. It is quick and convenient to connect to other functional modules. Through the slide switch S2, select the power supply voltage of the modules which are connected to these interfaces. At that time, when the slide switch S2 was turned to 5V, the power supply voltage of the connected module was 5V, and when the slide switch S2 was turned to 3.3V, the power supply voltage of the connected module was 3.3V. Note: The VCC terminals of all externally expanded HY-2.0-4P connectors are connected together, so when the power supply voltage is selected, the power supply voltage of all externally expanded HY-2.0-4P connectors will become the same.<br>
A group of pin headers leads to the SPI1 interface, which can be connected to the SPI peripheral module through flat cables or DuPont cables. The SPI1 interface is consistent with the VCC voltage of the four HY-2.0-4P connectors. One Full-color RGB, cool LED can be seen when running the demo code. One card slot for Micro SD card. A buzzer with switch, open when using, do not open when not using.<br>
A 2.54mm 4PIN header is reserved to lead out the power supply pin, data pin, and two ground pins. It can be used with multiple expansion modules, such as DS18B20 temperature sensor, DHT11 temperature and humidity sensor and so on. It can be used in a wider range. An ESP-01 transfer module solder joint is reserved to support IIC bus and UART. There is also a standard 3.5mm audio jack, which supports dual channel and left channel switching.<br>
## 2.2、Python Demo Codes Usage
### 1.Installation Thonny
Thonny download：https://thonny.org<br>
### 2.  After installing Thonny, hold down the BOOTSEL button on Pico when the power is off, connect the computer with a USB cable and release the button, at this time pop up an RPI-RP2 disk directory, drag adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.3.uf2 in the demo codes\python directory into the RPI-RP2 disk.
### 3.  Right click the 18b20.py in the demo codes demo codes\python directory, open with Thonny, click Tools - Settings, in the interpreter bar, select CiruitPython (general), and set the Raspberry Pi Pico port (COMx: the port number x of the computer may be different), and then click OK.
### 4.Files window and upload the Lib library file to Raspberry Pi Pico.
### 5.Connect the 18B20 temperature sensor to the DHT11/DS18B20 header of the expansion board (see Figure 2-1 pin definition diagram), then click the "Run current script" button or press the F5 key to run the current script and observe the data output in the shell window of the Thonny application.
### 6.Connect the headset to the 3.5mm audio jack of the expansion board (see Figure 2-1 Pin Definition Diagram) and open the audio.py demo code, upload the prepared MP3 file to Raspberry Pi Pico, and then click the "Run current script" button or press the F5 key to check the headset playback.
### 7.Turn the slide switch of the buzzer on the expansion board to the  position ( means the buzzer is turned on, means the buzzer is turned off), open the beeper.py demo code, and then click the "Run current script" button or press F5 to run the current script and check the playback of the expansion board buzzer.
### 8.Connect the DHT11 temperature and humidity sensor module to the DHT11/DS18B20 header of the expansion board (see Figure 2-1 pin definition diagram), open the dht11.py demo code, click the "Run current script" button or press the F5 key to run the current script, and observe the data output in the shell window of the Thonny application.
### 9.Open the key.py demo code, click the "Run current script" button or press the F5 key to run the current script, press the user key K1/K2/K3, and observe the data output in the shell window of the Thonny application.
### 10.Open the rgb_led.py demo code, click the "Run current script" button or press F5 to run the current script and observe the RGB changes on the expansion board.
### 11.Open the sdcard.py demo code to detect Micro SD card slot function, the file system of SD card is FAT32 or FAT, and then click the "Run current script" button or press F5 to run the current script and observe the data output in the shell window of the Thonny application.<br>

__Thank you for choosing the products of Shengui Technology Co.,Ltd. For more details about this product, please visit:
www.seengreat.com__

