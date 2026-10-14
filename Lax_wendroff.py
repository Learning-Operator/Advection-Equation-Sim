
import numpy as np
from Wave import Advec_wave

## Wave params
#wave_speed = 1 # m/s
#std = 5 #m
#magnitude = 1 #kg/m^3
#central_pos = 2 #m
#
## Resolution params
#grid_length = 100 #m
#cell_amt = 1000
#dt = 0.5 #s


#Wave_list = {
#            "wave_speed": wave_speed,
#            "std": std,
#            "magnitude": magnitude,
#            "central_pos": central_pos,
#            "grid_length": grid_length,
#            "dt": dt,
#            "cell_amt": cell_amt,
#            "wave_speed": wave_speed
#            }


#class Advec_wave():
#    def __init__(self, 
#                 central_pos, 
#                 magnitude, 
#                 std,  
#                 ds,
#                 grid_length,
#                 wave_speed):

def Lax_method(Wave_list,
         dt, 
         total_time, 
         wave_speed, 
         t_i = 0,
         steps = 10):

    #the density function, with a 1/2 timestep forward and 1/2 spatial step backward would be:
    # the average of the density values at the present step in time and one step backward minus the 1/2 * the courant number times the same exact difference.

    ds = Wave_list['grid_length'] / Wave_list['cell_amt']

    courant_number = Wave_list['wave_speed'] * dt/ds

    wave = Advec_wave(central_pos=Wave_list['central_pos'], 
                  magnitude=Wave_list['magnitude'], 
                  std=Wave_list['std'], 
                  wave_speed=Wave_list['wave_speed'], 
                  ds=ds, 
                  grid_length=Wave_list['grid_length'])

    u = wave.density_array.copy()
    u_present = u.copy()

    u_history = [u.copy()]
    times = [t_i]

    for j in range(steps):
        u_next = u_present
        u_phalfnhalf = 0.5 * (u_next[1:] + u_next[:-1]) - 0.5 * courant_number * (u_next[1:] - u_next[:-1])
        u_phalfhalf = 0.5 * (u_next[1:-1] + u_next[2:]) - 0.5 * courant_number * (u_next[2:] - u_next[1:])
        u_next[1:-1] = u_next[1:-1] - courant_number * (u_phalfhalf - u_phalfnhalf)
        u_history.append(u_next.copy())
        times.append(t_i + (j + 1) * dt)
    
    wave.density_array = u
    return wave.x, np.array(times), np.array(u_history)