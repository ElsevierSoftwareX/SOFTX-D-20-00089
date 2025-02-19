#!/usr/bin/python3
# (C) Kim Miikki 2020

from time import sleep
from rpi.camerainfo import *

if camera_detected==0:
    print("Raspberry Pi camera module not found!")
    exit(0)

enable_gains=False
preview_mode="off"
iso=100
w=camera_maxx
h=camera_maxy

info="Auto exposure shutter speed "
if enable_gains:
    info+="and AWB gains "
info+="for Raspberry Pi camera module "
info+=camera_revision
print(info)
print("")

camera=PiCamera(resolution=(w,h))
if preview_mode=="on":
    camera.start_preview(resolution=(w,h))
camera.iso=int(iso)
# You can query the exposure_speed attribute to determine the actual
# shutter speed being used when this attribute is set to 0
camera.exposure_mode='auto'
camera.shutter_speed=0
# Wait for the automatic gain control to settle
sleep(2)
camera.awb_mode = "auto"
ss=camera.exposure_speed
if preview_mode=="on":
    sleep(5)
    camera.stop_preview()
l=len(str(ss))
print("Shutter speed: "+str(round(ss/1000)).rjust(l)+" ms")
print("Shutter speed: "+str(ss)+" µs")

if enable_gains:
    g=camera.awb_gains
    print("")
    print("Red gain: ",round(float(g[0]),2),g[0])
    print("Blue gain:",round(float(g[1]),2),g[1])

camera.close()
