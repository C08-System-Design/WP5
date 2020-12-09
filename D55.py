import sys
import math
from D52 import R_lst, t_lst, L_lst
from mat import A2195_T84 as mat
from D53 import buckling_opt


def tankandbeam_opt(m_viable, beam_viable):
    m_final = []
    for i in range(len(m_viable)):
        print(i)
        tank_int = m_viable[i]
        beam_int = beam_viable[i]
        m_int = tank_int + beam_int
        print(m_int)
        m_final.append(m_int)
    m_min = min(m_final)
    m_min_index = m_final.index(m_min)
    L_min = viable_list[1][m_min_index]
    R_min = viable_list[2][m_min_index]
    t_min = viable_list[3][m_min_index]

    return(m_min, L_min, R_min, t_min, m_min_index)

viable_list = buckling_opt(180,R_lst, t_lst, L_lst, mat)[1]
m_viable = viable_list[0]
beam_viable = []
for i in range(len(m_viable)):
    beam_viable.append(i)

print(tankandbeam_opt(m_viable, beam_viable))