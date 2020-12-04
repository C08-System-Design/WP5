# import numpy as np


def get_t(k, mp, vp, rhop):  # function for projectile penetration depth t
    tf = k*mp**0.352*vp**0.875*rhop**0.167
    return tf


K = 0.7  # provided in the reader, true for most metals, therefore out surfaces
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
"""
