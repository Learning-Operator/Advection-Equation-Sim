
import numpy as np


class Advec_wave():
    def __init__(self, 
                 central_pos, 
                 magnitude, 
                 std,  
                 ds,
                 grid_length,
                 wave_speed):

        self.ds = ds
        self.grid_length = grid_length
        self.wave_speed = wave_speed
        self.x = np.arange(grid_length) * ds
        self.density_array = magnitude * np.exp(-(self.x - central_pos)**2 / (2 * std**2))