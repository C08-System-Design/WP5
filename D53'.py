import sys
import math
from D52 import R_lst, t_lst, L_lst
from mat import A2195_T84 as mat

def buckling_opt(m_fuel, R_lst, t_lst, L_lst, mat):
    # material property needed to added
    E_mat = mat.get("E")*10**9
    rho = mat.get("rho")
    v = mat.get("nu")

    p = 2.4 * (10 ** 6) * 1.25  # Pa inside pressure, 1.25 margin

    R_list = R_lst
    t_1_list = t_lst
    L_list = L_lst
    L_viable = []
    R_viable = []
    t_viable = []
    m_viable = []

    for i in range(0, len(R_list)):
        r = R_list[i]
        L = L_list[i]
        t = t_1_list[i]
        A = math.pi * (r ** 2)
        m = (2 * math.pi * r * t * L + 4 * math.pi * t * (r ** 2)) * rho + m_fuel
        I = math.pi * (r ** 3) * t  # area moment of inertia
        # column buckling
        sigma_cr_1 = (E_mat * I * ((math.pi) ** 2)) / (A * (L ** 2))

        # shell buckling
        Q = (p / E_mat) * (r / t) ** 2
        sigma_cr_2 = (1.983 - 0.983 * (math.exp(-23.14 * Q))) * (
                    (E_mat * t) / (r * math.sqrt(1 - v ** 2) * math.sqrt(3)))

        f = 9.81 * 7.5 * 3.2175 * m  # WP4 2.2.2
        sigma_applied = f / (2 * math.pi * r * t)  # normal stress for thin wall
        # if both lower then added to viable
        if sigma_cr_1 > sigma_applied and sigma_cr_2 > sigma_applied:
            L_viable.append(L)
            R_viable.append(r)
            t_viable.append(t)
            m_viable.append(m)
    # optimum mass solution
    m_opt = min(m_viable)
    m_opt_index = m_viable.index(m_opt)
    L_opt = L_viable[m_opt_index]
    R_opt = R_viable[m_opt_index]
    t_opt = t_viable[m_opt_index]
    config_opt = (m_opt, L_opt, R_opt, t_opt)
    config = (m_viable, L_viable, R_viable, t_viable)
    return [config_opt, config, (len(L_lst)-len(L_viable))]

a = buckling_opt(180, R_lst, t_lst, L_lst,mat)

print(a[2])