import sys
import math
from D52 import R_lst, t_lst, L_lst
from mat import A2195_T84 as mat

#cross-sectional enclosed area
def get_area(r):
    A = math.pi * (r ** 2)
    return A

#area moment of inertia
def get_I(r, t):
    I = math.pi * (r ** 3) * t
    return I

#mass of the structure, cylinder + spherical end caps
def get_mass(r, t, L):
    m = (2 * math.pi * r * t * L + 4 * math.pi * t * (r ** 2)) * rho
    return m

#column buckling critical stress
def get_sigma_cr_column(r, t, L):
    sigma_cr_1 = (E_mat * get_I(r, t) * ((math.pi) ** 2)) / (get_area(r) * (L ** 2))
    return sigma_cr_1

#shell buckling critical stress
def get_sigma_cr_shell(r, t):
    Q = (p / E_mat) * (r / t) ** 2 #dimensionless variable for intermediate step
    sigma_cr_2 = (1.983 - 0.983 * (math.exp(-23.14 * Q))) * ((E_mat * t) / (r * math.sqrt(1 - v ** 2) * math.sqrt(3)))
    return sigma_cr_2

#stress imposed by launch loads (compressive load at two ends)
def get_sigma_cr_applied(r, t, L):
    f = 9.81 * 7.5 * 3.2175 * (get_mass(r, t, L) + m_extra)  # WP4 2.2.2
    sigma_applied = f / (2 * math.pi * r * t)               #normal stress
    return sigma_applied

#check if configuration fails
def check_config(r, t, L):
    check = True
    if get_sigma_cr_applied(r, t, L) > get_sigma_cr_column(r, t,L) or get_sigma_cr_applied(r, t, L) > get_sigma_cr_shell(r, t):
        check = False
    return check

#find the optimum config (lowest mass)
def get_opt(config):
    masslist = config[3]                #masses
    opt_mass = min(masslist)            #lowest mass
    opt = masslist.index(opt_mass)      #index with lowest mass
    opt_config = [config[0][opt], config[1][opt], config[2][opt], config[3][opt]] #radius thickness length and mass
    return opt_config

#filter list of configurations
def buckling_opt(mass_extra, R_lst, t_lst, L_lst, mat):
    global E_mat, rho, v, p, m_extra
    m_extra = mass_extra                #total mass of the propellant
    E_mat = mat.get("E") * 10 ** 9      #materials young's modulus


    rho = mat.get("rho")    #kg/m^3
    v = mat.get("nu")       #poission ratio

    p = 2.4 * (10 ** 6) * 1.25  # Pa inside pressure, 1.25 margin

    #new lists for viable configs
    R_viable = []   #radii
    t_viable = []   #thicknesses
    L_viable = []   #lengths
    m_viable = []   #masses

    for i in range(0, len(R_lst)):
        r = R_lst[i]
        t = t_lst[i]
        L = L_lst[i]
        if check_config(r, t, L):
            R_viable.append(r)
            t_viable.append(t)
            L_viable.append(L)
            m_viable.append(get_mass(r, t, L))

    config = [R_viable, t_viable, L_viable, m_viable]   #all viable configurations
    config_opt = get_opt(config)                        #optimal configuration
    filtered = len(R_lst) - len(R_viable)               #number of failing configs
    return [config, config_opt, filtered]

'''
the returned list
[0] is all the configurations pass the buckling check in [[m_viable], [L_viable], [R_viable], [t_viable]]
[1] is optimum config for this buckling check only in [m_opt, L_opt, R_opt, t_opt]
[2] is the number of case rejected

a = buckling_opt(180,R_lst, t_lst, L_lst, mat)
print(a[1]) #optimal config
print(a[2]) #number of failing configs
'''

a = buckling_opt(1600,R_lst, t_lst, L_lst, mat)
print(a[1]) #optimal config
print(a[2]) #number of failing configs