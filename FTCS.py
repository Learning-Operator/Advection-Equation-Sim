
import numpy as np
from wave import Advec_wave




Grid_resolution = 100 #m
ds = 1 #m
wave_speed = 1 # m/s
std = 5 #m
magnitude = 1 #kg/m^3
central_pos = 2 #m

Wave = Advec_wave(central_pos=central_pos, 
                  magnitude=magnitude, 
                  std=std, 
                  wave_speed=wave_speed, 
                  ds=ds, 
                  grid_length=Grid_resolution)


def FTCS(Wave, dt, total_time, wave_speed):
    