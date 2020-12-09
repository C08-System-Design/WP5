# import numpy as np

# --- Class Particle created --- #
class Particle:
    K = 0.7  # from the reader, true for most metals, therefore out surfaces
    _registry = []

    def __init__(self, name, m, v, rho):
        self._registry.append(self)
        self.name = name
        self.m = m
        self.v = v
        self.rho = rho

    def get_t(self):  # function for projectile penetration depth t
        t = self.K*self.m**0.352*self.v**0.875*self.rho**0.167
        return t


# --- Particle definition, values from Overleaf --- #
mm = Particle("Micrometeorite", 1e-9, 25, 1e-9/1.96e-7)
sod = Particle("Small orbital debris", 8e-7*2700, 10, 2.7)
mod = Particle("Medium orbital debris", 7.9e-3*2700, 10, 2.7)
t_lst = []
for i in Particle._registry:  # i being an instance of the Particle class
    t_lst.append(i.get_t())
print(t_lst)
"""
Run the above function for possible projectile masses (m_p), impact velocities
(v_p) and projectile densities (rho_p). The coefficient K is held constant
for all the surfaces at K = 0.7

Since the debris can hit anywhere on the spacecraft, worst case (highest t)
shall be taken as the minimal thickness for all the outer surfaces of the
spacecraft.

Note that the units are:
m_p = [g]
v_p = [km/s]
rho_p = [grams/cm3]

Run this function for every projectile type, append results to a list, run
max(list) to get the sufficient penetration thickness. 
"""
