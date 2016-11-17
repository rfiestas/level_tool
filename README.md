level_tool
=============

Description
-------
The [Sense Hat](https://www.raspberrypi.org/documentation/hardware/sense-hat/) is an add-on board for [Raspberry Pi](https://www.raspberrypi.org/), made especially for the Astro Pi mission.
The Sense HAT has an 8×8 RGB LED matrix, a five-button joystick and includes the following sensors:
- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Barometric pressure
- Humidity
The IMU (inertial measurement unit) sensor is a combination of three sensors, each with an x, y and z axis.

On this script i use IMU sensor as a level tool, it can be used to indicate how parallel (level) a surface is relative to the earth.
Led matrix show a point.
- Green point, it's full parallel.
- Yellow point, it's near parallel.
- Red point, it's not parallel.

Instalation
-------
```
git clone https://github.com/rfiestas/level_tool.git
```
also sense hat python libraries, follow this link [sense-hat](https://www.raspberrypi.org/documentation/hardware/sense-hat/) for more details.

Usage
-------
Launch this script with any root rights user.
```
level_tool.py
```
Press sense hat middle button joystick to stop script.
