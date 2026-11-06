## NOAH ZEEMAN - 15494365
## NSP2 - ECPC - classes "Class 'ProjectileMotion'"
## 6 Nov 26

# class ProjectileMotion
#    ...
#    __init__
#       ...
#    add_launch_parameters
#       ...
#    get_initial_velocities
#       ...
#    get_launch_angles
#       ...
#    get_time_of_flights
#       ...
#    get_flight_ranges
#       ...

# import necessary packages
import math as m


class ProjectileMotion:
    launch_angl, launch_velo= [], []
    g = 9.81

    def __init__(self):
        pass
        
    def add_launch_parameters(self, v, angle):
        self.launch_velo.append(v)
        self.launch_angl.append(angle)

    def get_initial_velocities(self):
        return self.launch_velo

    def get_launch_angles(self):
        return self.launch_angl

    def get_time_of_flights(self):
        return [(2 * self.launch_velo[i] * m.sin(m.radians(self.launch_angl[i]))) / self.g for i in range(len(self.launch_angl))]

    def get_flight_ranges(self):
        ToF= self.get_time_of_flights()
        return [self.launch_velo[i] * m.cos(m.radians(self.launch_angl[i])) * ToF[i] for i in range(len(self.launch_angl))]
        

speedy = ProjectileMotion()
speedy.add_launch_parameters(v=28, angle=68)
speedy.add_launch_parameters(v=11, angle=15)

v = speedy.get_initial_velocities()
angles = speedy.get_launch_angles()
x = speedy.get_flight_ranges()
t = speedy.get_time_of_flights()

print(f"{v=}")
print(f"{angles=}")
print(f"{x=}")
print(f"{t=}")