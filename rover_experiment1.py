##Hailey Reyes
##check after rover_dynamics is done
import numpy as np
from subfunctions import simulate_rover, mechpower, rover, planet
import matplotlib.pyplot as plt
from define_experiment import experiment1
##get dictionaries
experiment, end_event = experiment1()

end_event['max_distance'] = 1000
end_event['max_time'] = 1000
end_event['min_velocity'] = 0.01

rover = simulate_rover(rover,planet,experiment,end_event)

time = rover['telemetry']['time']
velocity = rover['telemetry']['velocity']
position = rover['telemetry']['position']

power = mechpower(velocity,rover)

#
plt.figure(figsize=[8,14])
##x
plt.subplot(3,1,1)
plt.plot(time,position)
plt.title('Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
#v
plt.subplot(3,1,2)
plt.plot(time,velocity)
plt.title('Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
##p
plt.subplot(3,1,3)
plt.plot(time,power)
plt.title('Power')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')

plt.tight_layout(h_pad=3)
plt.show()





