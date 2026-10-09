




from Wave import Advec_wave
import numpy as np
from typing import Optional

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






from Wave import Advec_wave
import numpy as np


def upwind(Wave_list,
           dt,
           t_i=0,
           steps=10,
           courant_number: Optional[float] = None):

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

    if courant_number is None:
        courant_number = Wave_list['wave_speed'] * dt / ds
    else:
     courant_number = courant_number

    if Wave_list['wave_speed'] > 0:
        for j in range(steps):
            u_next = u.copy()
            u_next[1:] = u[1:] - courant_number * (u[1:] - u[:-1])
            u = u_next
            u_history.append(u.copy())
            times.append(t_i + (j + 1) * dt)

    elif Wave_list['wave_speed'] < 0:
        for j in range(steps):
            u_next = u.copy()
            u_next[:-1] = u[:-1] - courant_number * (u[1:] - u[:-1])
            u = u_next
            u_history.append(u.copy())
            times.append(t_i + (j + 1) * dt)

    Wave.density_array = u

    return Wave.x, np.array(times), np.array(u_history)
