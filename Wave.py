
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

        # density_array = np.ones(len(self.x))
        # density_array[((self.x - central_pos) > 0.0)] += 1.0
        # self.density_array = density_array
        # for i in range(len(density_array)):
        #     if i % 5
        
        # density_array = density_array * 1 for

        #self.density_array = magnitude * (self.x - central_pos)