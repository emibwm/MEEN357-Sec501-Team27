import scipy.interpolate as scp
import numpy as np
import matplotlib.pyplot as plt

alpha_dist = experiment1()[0]['alpha_dist']
alpha_deg = experiment1()[0]['alpha_deg']

alpha_fun = scp.interp1d(alpha_dist, alpha_deg, kind = "cubic", \
                     fill_value = 'extrapolate')
    

dist_max = np.max(alpha_dist)
dist_min = np.min(alpha_dist)
pos = np.linspace(dist_min, dist_max, num= 100)

ang = alpha_fun(pos)
plt.xlabel('Position (m)')
plt.ylabel('Terrain Angle (deg.)')
plt.plot(pos, ang)
plt.plot(alpha_dist, alpha_deg, marker= '*', linestyle = 'none')
plt.title("Terrain Angle (deg.) vs. Position (m)")
plt.show()