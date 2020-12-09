import sys
import math
from D52 import R_lst, t_lst, L_lst
from mat import A2195_T84 as mat


#cross-sectional area
def get_area(r):
    A = math.pi * (r ** 2)
    return A

#area moment of inertia
def get_I(r, t):
    I = math.pi * (r ** 3) * t
    return I

#mass of the whole shell structure, cylinder + both caps
def get_mass(r, t, L):
    m = (2 * math.pi * r * t * L + 4 * math.pi * t * (r ** 2)) * rho
    return m

#column buckling critical stress
def get_sigma_cr_column(r, t, L):
    sigma_cr_1 = (E_mat * get_I(r, t) * ((math.pi) ** 2)) / (get_area(r) * (L ** 2))
    return sigma_cr_1

#shell buckling critical stress
def get_sigma_cr_shell(r, t):
    Q = (p / E_mat) * (r / t) ** 2
    sigma_cr_2 = (1.983 - 0.983 * (math.exp(-23.14 * Q))) * ((E_mat * t) / (r * math.sqrt(1 - v ** 2) * math.sqrt(3)))
    return sigma_cr_2

#actural stress applied
def get_sigma_cr_applied(r, t, L):
    f = 9.81 * 7.5 * 3.2175 * (get_mass(r, t, L) + m_fuel)  # WP4 2.2.2
    sigma_applied = f / (2 * math.pi * r * t)
    return sigma_applied

#check if its faulty
def check_config(r, t, L):
    check = True
    if get_sigma_cr_applied(r, t, L) > get_sigma_cr_column(r, t,L) or get_sigma_cr_applied(r, t, L) > get_sigma_cr_shell(r, t):
        check = False
    print(get_sigma_cr_applied(r, t, L) / get_sigma_cr_shell(r, t), "     ",get_sigma_cr_applied(r, t, L) / get_sigma_cr_column(r, t, L))
    return check

#find the optimum config (lightest)
def get_opt(config):
    masslist = config[3]
    opt_mass = min(masslist)
    opt = masslist.index(opt_mass)
    opt_config = [config[0][opt], config[1][opt], config[2][opt], config[3][opt]]
    return opt_config


def buckling_opt(mass_fuel, R_lst, t_lst, L_lst, mat):
    global E_mat, rho, v, p, m_fuel
    m_fuel = mass_fuel
    E_mat = mat.get("E") * 10 ** 9
    print(E_mat)

    rho = mat.get("rho")
    v = mat.get("nu")

    p = 2.4 * (10 ** 6) * 1.25  # Pa inside pressure, 1.25 margin

    R_viable = []
    t_viable = []
    L_viable = []
    m_viable = []

    for i in range(0, len(R_lst)):
        r = R_lst[i]
        t = t_lst[i]
        L = L_lst[i]
        if check_config(r, t, L):
            R_viable.append(r)
            t_viable.append(t)
            L_viable.append(L)
            m_viable.append(get_mass(r, t, L))

    config = [R_viable, t_viable, L_viable, m_viable]
    config_opt = get_opt(config)
    filtered = len(R_lst) - len(R_viable)   #number rejected
    return [config, config_opt, filtered]

a = buckling_opt(180,R_lst, t_lst, L_lst, mat)
print(a[2])

'''
the returned list
[0] is all the configurations pass the buckling check in [[m_viable], [L_viable], [R_viable], [t_viable]]
[1] is optimum config for this buckling check only in [m_opt, L_opt, R_opt, t_opt]
[2] is the number of case rejected
'''