#!/usr/bin/env python
''' level_tool.py V1.
Use IMU Sensor as level.Launch with root user.
Press joystick middle button to exit.'''

from __future__ import division
import sys
from sense_hat import SenseHat

def thresholds(value, v_max=7, v_min=0):
    ''' Define max and min thresholds '''
    return int(max(v_min, min(v_max, value)))

def draw(x, y, color):
    ''' Draw pixels '''
    sense.set_pixel(thresholds(x-0.5), thresholds(y-0.5), color)
    sense.set_pixel(thresholds(x+0.5), thresholds(y-0.5), color)
    sense.set_pixel(thresholds(x-0.5), thresholds(y+0.5), color)
    sense.set_pixel(thresholds(x+0.5), thresholds(y+0.5), color)

sense = SenseHat()

color = black = [0, 0, 0]
green = [0, 255, 0]
yellow = [255, 255, 0]
red = [255, 0, 0]

# pixels
pixels = 4

# Relation grades over pixels.
relation = pixels / 90

# Precision
precision = 0.1
prec_max = pixels + precision
prec_min = pixels - precision

# Aproximation
aproximation = 0.6
apro_max = pixels + aproximation
apro_min = pixels - aproximation

# Tmp vars to refresh
pos_x_tmp = 0
pos_y_tmp = 0
color_tmp = 0

# Clear display
sense.clear()

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'middle':
            sense.clear()
            sys.exit(0)
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]

    # Explain why, only have 180 grades.
    # https://richardstechnotes.wordpress.com/imu-stuff/
    if 0 < pitch < 90:
        pos_x = 4 - pitch * relation
    elif 270 < pitch < 360:
        pos_x = 8 - (pitch-270) * relation

    if 0 < roll < 90:
        pos_y = 4 + roll * relation
    elif 270 < roll < 360:
        pos_y = (roll-270) * relation
    elif 90 < roll < 180:
        pos_y = 8 - (roll-90) * relation
    elif 180 < roll < 360:
        pos_y = 4 - (roll-180) * relation

    if (prec_min < round(pos_x, 1) < prec_max) and \
    (prec_min < round(pos_y, 1) < prec_max):
        color = green
    elif (apro_min < round(pos_x, 1) < apro_max) and \
    (apro_min < round(pos_y, 1) < apro_max):
        color = yellow
    else:
        color = red

    if round(pos_x, 0) != pos_x_tmp or \
    round(pos_y, 0) != pos_y_tmp or color != color_tmp:
        draw(pos_x_tmp, pos_y_tmp, black)
        draw(pos_x, pos_y, color)
        pos_x_tmp = round(pos_x, 0)
        pos_y_tmp = round(pos_y, 0)
        color_tmp = color
