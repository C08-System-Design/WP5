import sys
import math
from math import *
from numpy import *
import matplotlib.pyplot as plt
from D52 import R_lst, t_lst, L_lst
from mat import A2195_T84 as mat
from D53 import buckling_opt
from D54 import getConfigs

m_viable = buckling_opt(1590,R_lst, t_lst, L_lst, mat)[0][3]       #get the tank mass list from D53
beam_viable = getConfigs(1)                                        #get the beam mass list from D54

def tankandbeam_opt(m_viable, beam_viable):
    viable_list = buckling_opt(1590, R_lst, t_lst, L_lst, mat)[0]  #get list of all dimensions
    m_final = []
    m_beam_config = []
    m_viable_int = []
    for k in range(len(m_viable)):
        m_total = 8 * beam_viable[k] + 1590                        #Adjust total mass
        m_tank = buckling_opt(m_total,R_lst,t_lst,L_lst,mat)[0][3] #Take specifc mass of tank
        if k >= len(m_tank):                                       #Ignore numbers that don't exist in filtered list
            break
        m_viable_int.append(m_tank[k])
        m_beam_config.append(8*beam_viable[k])
    for i in range(len(m_viable_int)):
        tank_int = m_viable_int[i]                                 #Tank mass
        beam_int = m_beam_config[i]                                #Total Beam mass
        m_int = tank_int + beam_int                                #add masses together
        m_final.append(m_int)
    m_min = min(m_final)
    m_min_index = m_final.index(m_min)
    L_min = viable_list[2][m_min_index]
    R_min = viable_list[0][m_min_index]
    t_min = viable_list[1][m_min_index]

    return(m_min, L_min, R_min, t_min, m_min_index)



print(tankandbeam_opt(m_viable, beam_viable))
