# Raspberry Pi PowerOff Button/LED Script

This script configures an arbitrary GPIO Pin on a Raspberry Pi computer board to work as a trigger to the `/sbin/poweroff` function. 

When the power down routine is started

1. A message will be printed on `stdout`
2. A message will be printed into the system log (usually `/var/log/syslog`)
3. A LED will be turned on until the script is forcefully killed by the OS by the power down sequence.
  * This is intended as an Indicator of "Do Not Disconnect the Board". Though the instant the LED turns Off, the SO will still be on working on the shut down sequence.

## Requirements

### Software

**Installed by default on RaspberryPi OS**

* `python3`
* `systemd`

**Installed by default on current versions of RaspberryPi OS**

* python3-gpiozero package

If not installed, install with: `sudo apt install python3-gpiozero`

### Hardware

* LED is optional.
* A cable assembly with a Button that can be connected to a GPIO GND Pin and a common GPIO Pin
* Knowledge of the GPIO label number of the selected Pin (board PIN number is different to the GPIO labeled number)

## Installation

1. Place `poweroffbutton.py` on your preferred location.
2. Edit `poweroffbutton.py` BUTTON_PIN and LED_PIN variables and change them to the selected GPIO Pin number.
3. Write down the full paths relevant to your environment
  * Full path of the directory where `poweroffbuton.py` it's located.
  * Full path of the python3 binary. Can be discovered with the command `which python3`.
4. Edit `poweroffbutton.service`
  * Change _WorkingDirectory_ parameter to the full path of the directory of the `poweroffbutton.py` script.
  * Change _ExecStart_ parameter to the correct full path of the python3 binary and the full path of the `poweroffbutton.py` script.
5. Install `poweroffbutton.service` into _systemd_ service management service
  * Copy `poweroffbutton.service` into `/etc/systemd/system/` 
    * `sudo cp path/of/poweoffbutton.service /etc/systemd/system/`
  * Enable _poweroffbutton_ service so it automatically starts on system boot.
    * `sudo systemctl enable poweroffbutton`
  * Start _poweroffbutton_ service
    * `sudo systemctl start poweroffbutton`
  * You can check enable/disable and start/stop status and the service output with `systemctl status poweroffbutton`
 6. Test!

