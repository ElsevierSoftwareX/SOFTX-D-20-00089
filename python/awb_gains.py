#!/usr/bin/python3
# (C) Kim Miikki 2020

from time import sleep
from rpi.camerainfo import *

if camera_detected==0:
    print("Raspberry Pi camera module not found!")
    exit(0)

exposure=20000   
exp_mode_manual="off"
preview_mode="off"
iso=100
w=camera_maxx
h=camera_maxy

info="Auto white balance gains for Raspberry Pi camera module "
info+=camera_revision
print(info)
print("")

camera=PiCamera(resolution=(w,h))
if preview_mode=="on":
    camera.start_preview(resolution=(w,h))
# Now fix the values
if exp_mode_manual=="on":
    camera.exposure_mode = "off"
    camera.shutter_speed = int(exposure)
camera.iso=int(iso)
# Wait for the automatic gain control to settle
sleep(2)
if preview_mode=="on":
    sleep(5)
    camera.stop_preview()
camera.awb_mode = "auto"
g = camera.awb_gains
print("Red gain: ",round(float(g[0]),2),g[0])
print("Blue gain:",round(float(g[1]),2),g[1])
#print(g): This gives fractions i.e. (Fraction(395, 256), Fraction(245, 128))
# Manfrotto Lumie LEDs:
# Red gain:  1.85 237/128
# Blue gain: 1.51 387/256

camera.close()
