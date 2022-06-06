# Raspberry Pi with DHT22

This readme covers the necessary installation of the DHT22 hardware and prerequisite libraries to read temperature and humidity data.

This library makes use of the [ADAFruit CircuitPython DHT Library](https://docs.circuitpython.org/projects/dht/en/latest/) library to speed up initial development.

## Hardware installation

### Raspberry Pi Zero Pinout

[This](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZerov2.pdf) Sparkfun pdf provides an overview of the pinout of the Raspberry Pi Zero.

## Software installation

This instruction is from a fresh install of Raspberry Pi OS Buster Lite.

Ensure that the latest package versions and upgrades are installed.

### Install dependencies

Install pip3:
```
sudo apt install python3-pip
```

Install ADAFruit CircuitPython DHT Library:
```
sudo pip3 install adafruit-circuitpython-dht
```

[Install libgpiod](https://github.com/adafruit/Adafruit_CircuitPython_DHT/issues/33#issuecomment-1105263946):
```
sudo apt-get install libgpiod2
```

[Install sysv-ipc to enable pulseio](https://github.com/adafruit/Adafruit_CircuitPython_DHT/issues/33#issuecomment-774405577) for improved readings:
```
pip3 install sysv-ipc
```

Install python dependencies.
```
pip install -r requirements.txt
```

## Data Log

The program is intended to be run as a service. In a unix environment this can be achieved by using the systemd interface to register services.
It is good practice to use `absolute paths` when executing services from the systemd interface.

By default this logger will log data in `/home/pi/data` with a pattern of `<sensor>/<year>/<month>/<day>/<sensor>_<year>-<month>-<day> <hour>:00:00.00.db`.