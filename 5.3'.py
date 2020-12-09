import sys
import math
from tankage import R_lst, t_lst, L_lst

m_fuel = 180  #kg

#print("RtL",R_lst[0],t_lst[0],L_lst[0])    #checkif list imported correctly
V = 0.179 #m^3      #volume of tank

#material property needed to added
E_mat = 78*(10**9) #pa
rho = 2700 #kg/m^3
v = 0.3

p = 2.4 * (10**6) * 1.25    #Pa inside pressure


R_list = R_lst #test
t_1_list = t_lst
L_list = L_lst
#for c in range(1,10): #test
    #R_list.append(c/10)
    #t_1_list.append(c/1000)
    #L_list.append(c)

L_viable = []
R_viable = []
t_viable = []
m_viable = []

for i in range(0, len(R_list)):
    r = R_list[i]
    L = L_list[i]
    t = t_1_list[i]
    A = math.pi * (r**2)
    m = (2*math.pi*r*t*L + 4*math.pi*t*(r**2))* rho + m_fuel
    I = math.pi*r**3*t  #area moment of inertia

    #column buckling
    sigma_cr_1 = (E_mat* I*((math.pi)**2))/(A* (L**2))
    #sigma_cr_m_1 = sigma_cr_1/1000000      #in MPa


    #shell buckling
    Q = (p/E_mat)*(r/t)**2
    sigma_cr_2 = (1.983-0.983*(math.exp(-23.14*Q)))*((E_mat*t)/(r*math.sqrt(1-v**2)*math.sqrt(3)))
    #sigma_cr_m_2 = sigma_cr_2/1000000      #in MPa

    f = 9.81 * 7.5 * 3.2175 * m         #WP4 2.2.2
    sigma_applied = f/(2*math.pi*r*t)       #normal stress for thin wall

    #(sigma_cr_1/sigma_applied, sigma_cr_2/sigma_applied)
    #if both lower then added to viable
    if sigma_cr_1 > sigma_applied and sigma_cr_2 > sigma_applied:
            L_viable.append(L)
            R_viable.append(r)
            t_viable.append(t)
            m_viable.append(m)
#print(L_viable)
#print(R_viable)
#print(t_viable)
#print(m_viable)

#optimum mass solution
m_opt = min(m_viable)
m_opt_index = m_viable.index(m_opt)
L_opt = L_viable[m_opt_index]
R_opt = R_viable[m_opt_index]
t_opt = t_viable[m_opt_index]

#print(m_opt,L_opt,R_opt,t_opt)

#check number of original and filtered
#print(len(L_lst))
#print(len(L_viable))