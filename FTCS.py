
import numpy as np
from Wave import Advec_wave


# Wave params
wave_speed = 1 # m/s
std = 5 #m
magnitude = 1 #kg/m^3
central_pos = 2 #m

# Resolution params
grid_length = 100 #m
cell_amt = 1000
dt = 0.5 #s


Wave_list = {
            "wave_speed": wave_speed,
            "std": std,
            "magnitude": magnitude,
            "central_pos": central_pos,
            "grid_length": grid_length,
            "dt": dt,
            "cell_amt": cell_amt,
            "wave_speed": wave_speed
            }


def FTCS(Wave_list,
         dt, 
         total_time, 
         wave_speed, 
         t_i = 0,
         steps = 10):

    ds = Wave_list['grid_length'] / Wave_list['cell_amt']

    Wave = Advec_wave(central_pos=Wave_list['central_pos'], 
                  magnitude=Wave_list['magnitude'], 
                  std=Wave_list['std'], 
                  wave_speed=Wave_list['wave_speed'], 
                  ds=ds, 
                  grid_length=Wave_list['cell_amt'])

    u = Wave.density_array.copy()
    u_history = [u.copy()]
    times = [t_i]

    courant_number = Wave_list['wave_speed'] * Wave_list['dt'] / ds

    position_array_initial = Wave.x.copy()
    density_initial = Wave.density_array.copy()

    for j in range(steps):
        u_next = u.copy()
        u_next[1:-1] = u[1:-1] - 0.5 *(courant_number) * (u[2:] - u[:-2])
        u = u_next
        u_history.append(u.copy())
        times.append(t_i + (j + 1) * dt)                 

    Wave.density_array = u
    return Wave.x, np.array(times), np.array(u_history)