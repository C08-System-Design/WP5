import numpy as np
from mat import A2195_T84


def get_sphere_mass(r, p, material):
    # for a given pressure and target stress allowable, this function gets
    # mass of a material
    A = 4*np.pi*r**2
    t = get_hoop_t(r, p, material)
    m = A*t*material.get("rho")
    return m


def get_hoop_t(r, p, material):
    t = r*p/material.get("sigma_y")/1e6
    return t


def get_sphere_volume(r):
    V = 4/3*np.pi*r**3
    return V


def elongate(r):
    v1 = get_sphere_volume(r)
    r_new = r - 0.1
    v2 = get_sphere_volume(r_new)
    v3 = v1 - v2
    L = v3 / (np.pi*r_new**2)
    return [r_new, L]


def get_cylinder_mass(r, l, t):
    m = 2*np.pi*r*t*l
    return m


R = 0.4  # radius [m]
P = 2.4e6  # pressure [Pa]
mat = A2195_T84
print(get_sphere_mass(R, P, mat))
R_new = elongate(R)[0]
L = elongate(R)[1]
print(get_sphere_mass(R_new, P, mat)+get_cylinder_mass(R_new, L, get_hoop_t(R, P, mat)))

print(get_sphere_mass(0.34961345684772915, P, mat))


