"""poweroffbutton.py will start poweroff routine on pull-down event on a GPIO Pin

Configure BUTTON_PIN and LED_PIN variables to valid GPIO labeled number pins.
LED pin configuration is Optional

Requires: gpiozero

Regarding sudo on poweoff() function

  sudo command on poweroff() is optional
  It is not required if run through a systemd service script controlled by root
  or if this script is already run with sudo.

  `sudo poweroff` is used so this script could be run without superuser permissions
  by an user account which has /sbin/poweroff allowed to use without password on a
  sudoers.d configuration file.
"""
from signal import pause
from os import system
import atexit

from gpiozero import Button, LED

BUTTON_PIN = 19 # GPIO19, BOARD PIN 35
LED_PIN = 26    # GPIO26, BOARD PIN 37

led = LED(LED_PIN)

button = Button(
    BUTTON_PIN,
    pull_up=True,
    bounce_time=0.5)

def poweroff():
    print("Poweroff pressed")
    led.on()
    system('logger "Poweroff button pressed"')
    system('sudo poweroff')
    pause()

def powerdown_led():
    led.off()

powerdown_led()
atexit.register(powerdown_led)
button.when_pressed = poweroff

pause()

