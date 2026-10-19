##Hailey Reyes
##check after rover_dynamics is done
import numpy as np
from subfunctions import simulate_rover, mechpower, rover, planet, battenergy
import matplotlib.pyplot as plt
from define_experiment import experiment1
import end_of_mission_event


##telemetry = {'Time': None, 'completion_time': 0, 'velocity': None, 'position': None, 'distance_traveled': 0,
#             'max_velocity': 0, 'average_velocity': 0, 'power': None, 'battery_energy': 0, 'energy_per_distance': 0}

##get dictionaries
experiment, end_event = experiment1()
##set end 
end_event['max_distance'] = 1000
end_event['max_time'] = 10000
end_event['min_velocity'] = 0.01
##run rover dynamics simulation
rover = simulate_rover(rover,planet,experiment,end_event)
##get outputs from telemetry 
t = rover['telemetry']['time']
v = rover['telemetry']['velocity']
p = rover['telemetry']['position']


##calling values for table
# completion_time = t[-1]
# distance_travel = p[-1]
# max_velocity = max(v)
# average_velocity = sum(v) / len(v)
# battery_energy = battenergy(t, v, rover)
# batt_energy_per_distance = battery_energy/distance_travel
# print(completion_time)
# print(distance_travel)
# print(max_velocity)
# print(average_velocity)
# print(battery_energy)
# print(batt_energy_per_distance)

##calculate power
power = mechpoer(v,rover)

##make plots
plt.figure(figsize=[8,14])
##plot position
plt.subplot(3,1,1)
plt.plot(t,p)
plt.title('Position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
#velocity
plt.subplot(3,1,2)
plt.plot(t,v)
plt.title('Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
##plot power
plt.subplot(3,1,3)
plt.plot(t,power)
plt.title('Power vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
##adjust spacing of plots and show plots
plt.tight_layout(h_pad=3)
plt.show()
