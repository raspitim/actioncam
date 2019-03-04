from picamera import PiCamera
from gpiozero import Button
from time import sleep

cam = PiCamera()
button = Button(14)
cam.resolution = (1024, 768)
name = 0

while True:
    if button.is_pressed:
        cam.start_recording('/home/pi/capture'+str(name)+".h264")
        print("start")
        sleep(1)
        button.wait_for_press()
        cam.stop_recording()
        print("stop")
        sleep(2)
    name = name + 1
