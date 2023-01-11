import ctypes
import ctypes.util
import numpy
import time
import math
#import camera.hamamatsu_camera as hc
import rs232.RS232 as RS232
import filter_wheel.fw102c_LB as fw102c
# import laser.skyra as skyra
# import xyz_stage.ms2000 as ms2000
#import thorlabs_apt as apt #don't think i need this? for thorlabs motor in lsfmx.py
#import generator.ni as generator
# import utils.findbounds as findbounds
# import utils.chromatic as chromatic
# import utils.utils as utils
# import rclone.rclone as rclone
import lsmfx_LB as lsmfx_LB
import h5py
# import warnings
import os
import os.path
# import errno
# import sys
# import scipy.ndimage
# import warnings
# import gc
# import nidaqmx
# import os
# import os.path
# from os import path
# import shutil

############# SCAN PARAMETERS #############
drive = 'C'
fname = 'lindsey_python_test' # specimen names

xcenter = 12.87
ycenter = 3.16
zcenter = -1.19
xMin = xcenter - .25 #2MM BY 2MM BY 200UM
xMax = xcenter + .25
yMin = ycenter - .8
yMax = ycenter + 0.00
zMin = zcenter - 0.07
zMax = zcenter + 0.00

xWidth = 0.48 # 
yWidth = 0.8 # mm
zWidth = 0.07 # mm
camY = 256 # pixels
camX = 2048 # pixels
expTime = 4.99 # ms
camOffset = 0.0 # counts
wavelengths = numpy.array([660]) # lambda in nm
motor_positions = numpy.array([5.75, 1.60])
initial_powers = numpy.array([20.0, 50.0])
attenuations = numpy.array([1.5,1.5]) # mm^-1
binning = '1x1'
flatField = 0
#motor_positions = numpy.array([7.55, 5.75, 1.60])

# xMin = xMin - 0.5
# xMax = xMax + 0.5
# yMin = yMin - 0.5
# yMax = yMax + 0.5

######### INITIALIZE PARAMETERS ###########
xLength = xMax - xMin # mm
yLength = math.ceil((yMax - yMin)/yWidth)*yWidth # mm
zLength = math.ceil((zMax - zMin)/zWidth)*zWidth # mm
xOff = xMax - (xLength)/2
yOff = yMax - yLength/2
zOff = zMin



############ BEGIN SCANNING ##############
lsmfx_LB.scan3D(drive, fname, xOff, yOff, zOff, xLength, yLength, zLength, xWidth, yWidth, zWidth, camY, camX, expTime, binning, wavelengths, initial_powers, motor_positions, attenuations, camOffset, flatField)