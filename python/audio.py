"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
from board import *
import audiomp3
import audiopwmio

audio = audiopwmio.PWMAudioOut(left_channel=GP18, right_channel=GP19) # GP18 or GP19
decoder = audiomp3.MP3Decoder(open("lyxz.mp3", "rb"))

audio.play(decoder)
while audio.playing:
     pass
 
print("Done playing!")