
# Emily BWM

# ---- Wheel
wheel = {'mass': 1.0, 'radius': 0.3}
# ---- Speed Reducer
speed_reducer = {'type': 'reverted', 'diam_pinion': 0.04,
                  'diam_gear': 0.07, 'mass': 1.5}
# ---- Motor
motor = {'torque_stall': 170.0, 'torque_noload': 0.0,
         'speed_noload': 3.80, 'mass': 5.0, 'effcy_tau': [0, 10, 20, 40, 70, 165], 'effcy': [0, .55, .75, .71, .50, .05]}
# ---- Chassis
chassis = {'mass': 659.0}
# ---- SP
science_payload = {'mass': 75.0}
# ---- Power Subsystem
power_subsys = {'mass': 90.0}
# ---- Wheel Assembly
wheel_assembly = {'wheel': wheel, 'speed_reducer': speed_reducer, 'motor': motor}
# ---- New Addition
telemetry = {'Time': None, 'completion_time': 0, 'velocity': None, 'position': None, 'distance_traveled': 0,
             'max_velocity': 0, 'average_velocity': 0, 'power': None, 'battery_energy': 0, 'energy_per_distance': 0}
# ---- ROV!!
rover = {'wheel_assembly': wheel_assembly, 'chassis': chassis,
         'science_payload': science_payload, 'power_subsys': power_subsys, 'telemetry': telemetry}
# ---- Planet
planet = {'g': 3.72}

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as scp


effcy = rover['wheel_assembly']['motor']['effcy']
effcy_tau = rover['wheel_assembly']['motor']['effcy_tau']
effcy_fun = scp.interp1d(effcy_tau, effcy, kind = 'cubic')

maxi = np.max(effcy_tau)
mini = np.min(effcy_tau)
torque = np.linspace(mini, maxi, num= 100)
eff = effcy_fun(torque)

plt.ylabel('Efficiency (unitless)')
plt.xlabel('Torque (N*m)')
plt.plot(torque, eff)
plt.plot(effcy_tau, effcy, marker= '*', linestyle = 'none')
plt.title("Efficiency (unitless) vs. Torque (N*m)")
plt.show()