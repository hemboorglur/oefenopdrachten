## NOAH ZEEMAN - 15494365
## NSP2 - ECPC - classes "Class 'PointMass'"
## 6 Nov 26


class PointMass:
    def __init__(self, mass, position, velocity):
        self.mass= mass
        self.position= position
        self.velocity= velocity

    def update_position_after(self, time):
        # t_1 = position t_0 + velocity * delta_t
        self.position = tuple(self.position[i] + self.velocity[i] * time for i in range(2))
        return self.position

    def update_velocity(self, velocity):
        self.velocity= velocity
    
    def get_momentum(self):
        # p = m * v 
        return tuple(self.mass * self.velocity[i] for i in range(2))

    def get_kinetic_energy(self):
        # E_kin = 1/2 m * v^2
        return tuple(0.5 * self.mass * self.velocity[i] for i in range(2))


m = PointMass(mass=5.0, position=(1.0, 0.0), velocity=(3.0, 0.0))
print(f"{m.update_position_after(0)=}")
print(f"{m.update_position_after(0.5)=}")
print(f"{m.update_position_after(0.5)=}")

m.update_velocity((0.0, 3.0))
print(f"{m.update_position_after(0.5)=}")
print(f"{m.update_position_after(0.5)=}")

print(f"{m.velocity=}")
print(f"{m.get_momentum()=}")
print(f"{m.get_kinetic_energy()=}")