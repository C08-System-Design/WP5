from math import pi, sqrt


class Tank:
    def __init__(self, radius, length, t1, t2, volume):
        self.radius = radius
        self.length = length
        self.t1 = t1
        self.t2 = t2
        self.volume = volume

    def get_radius(self):
        r = sqrt(self.volume / self.length / pi)
        return r

    def get_volume(self):
        volume = pi*self.radius**2*self.length+4/3*pi*self.radius**3
        return volume


R = 1
t_1 = 1e-3
t_2 = 2e-3
V = 0.18
L = 2
tank = Tank(R, L, t_1, t_2, V)
print(tank.radius)
print(tank.get_radius())
print(tank.get_volume())
