import matplotlib.pyplot as plt
from define_edl_system import *
from subfunctions_EDL import *
from define_planet import *
from define_mission_events import *
from redefine_edl_system import *

#creates dictionaries
edl_system = define_edl_system_1()
mars = define_planet()
mission_events = define_mission_events()


# 0.5 step size
#parachute diameters range [14, 19]

#3x1 array of plots 
#1 sim time so time at term of sim vs parachute diam
#2 Rover speed relative to ground at sim term vs parachute diam
#3 Rover landing success where 1 = success 0 = failure vs parachute diam
#Provide recommendation for appropiate diam or range of diams for parachute
#Rov shall reach to ground safely and time can should get minimize (secondary)

sim_t = [] #sim time so time at term of sim vs parachute diam
rov_s = [] #rover speed relative to ground at sim term vs parachute diam
rov_f = [] #rover landing success where 1 = success 0 = failure vs parachute diam

#similar structure from main_edl_simulation.py

para_diam = [14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19]
tmax = 2000   # [s] maximum simulated time

for i in range(len(para_diam)):
    #Redefining system initial conditions w existing function
    new_system = redefine_edl_system(edl_system)
    new_system['speed_control']['on'] = False
    new_system['parachute']['diameter'] = para_diam[i]
    [t, Y, system] = simulate_edl(new_system, mars, mission_events, tmax, False)
    sim_t.append(t[-1])
    touchdown = Y[0,-1] + Y[5, -1]
    rov_s.append(touchdown) #sky crane vel + rov relative vel
    
    #Need to deduce whether it was a sucess or failure based on conditions
    final_altitude = Y[1, -1] #final sky crane altitude
    danger_altitude = edl_system['sky_crane']['danger_altitude']
    danger_speed = edl_system['sky_crane']['danger_speed']
    
    if not new_system['rover']['on_ground']: #if not on ground
        rov_f.append(0) #failure
    elif final_altitude >= danger_altitude and abs(touchdown) <= abs(danger_speed) :
        rov_f.append(1) #success
    else:
        rov_f.append(0) #failure 
    
fig, axs = plt.subplots(3, 1, figsize=(6, 9))

fig.suptitle("Simulation Time, Rover Speed, and Landing Success vs. Parachute Diameter")
axs[0].plot(para_diam, sim_t, marker='o')
axs[0].set_ylabel("Simulation Time [s]")
axs[0].set_title("Simulation Time vs. Parachute Diameter")
axs[0].set_xlabel("Parachute Diameter [m]")

axs[1].plot(para_diam, rov_s, marker='o')
axs[1].set_ylabel("Relative Speed to the Ground [m/s]")
axs[1].set_title("Rover Speed vs. Parachute Diameter")
axs[1].set_xlabel("Parachute Diameter [m]")

axs[2].plot(para_diam, rov_f, marker='o')
axs[2].set_ylabel("Landing Success [unitless]")
axs[2].set_title("Landing Success vs. Parachute Diameter")
axs[2].set_xlabel("Parachute Diameter [m]")


plt.tight_layout()
plt.show()
        
        
