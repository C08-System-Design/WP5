from math import pi, sqrt


class Tank:
    def __init__(self, R, L, t1, t2, V):
        self.R = R
        self.L = L
        self.t1 = t1
        self.t2 = t2
        self.V = V

    def get_radius(self, V, L):
        r = sqrt(V/L/pi)
        return r

R = 1
t1 = 1e-3
t2 = 2e-3
V = 0.18
tank = Tank(R, t1, t2, V)
print(tank.R)
