import sys
import math
from D52 import R_lst, t_lst, L_lst
from mat import A2195_T84 as mat
from D53 import buckling_opt


def tankandbeam_opt(m_viable, beam_viable):
    viable_list = buckling_opt(180, R_lst, t_lst, L_lst, mat)[0] #get list of all dimensions 
    m_final = []
    for i in range(len(m_viable)):
        tank_int = m_viable[i]
        beam_int = beam_viable[i]
        m_int = tank_int + beam_int                              #add masses together
        m_final.append(m_int)
    m_min = min(m_final)
    m_min_index = m_final.index(m_min)
    L_min = viable_list[2][m_min_index]
    R_min = viable_list[0][m_min_index]
    t_min = viable_list[1][m_min_index]

    return(m_min, L_min, R_min, t_min, m_min_index)


m_viable = buckling_opt(180,R_lst, t_lst, L_lst, mat)[0][3]  #get the tank mass list from D53_final
beam_viable = []                                             #get the beam mass list from D54
for i in range(len(m_viable)):
    beam_viable.append(i)

print(tankandbeam_opt(m_viable, beam_viable))

