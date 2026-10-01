
import numpy as np


class Advec_wave():
    def __init__(self, 
                 central_pos, 
                 magnitude, 
                 std,  
                 ds,
                 grid_length):

        
        self.ds = ds
        self.grid_length = grid_length

        self.x = np.arange(grid_length) * ds
        
        self.density_array = magnitude * np.exp(-(self.x - central_pos)**2 / (2 * std**2))


