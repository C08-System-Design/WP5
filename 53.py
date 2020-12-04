'''
from math import *
'''
V = 0.179 #m^3
E_mat = 78*(10**9) #pa
sigma_y = 490 #Mpa
p = 2.4 * (10**6) * 1.25#pa
rho = 2700 #kg/m^3
v = 0.5

R_list =[0.18] #test
t_1_list = [0.005]
L_list = [1.5]

for c in range(1,10): #test
    R_list.append(c/10)
    t_1_list.append(c/1000)
    L_list.append(c)

L_viable = []
R_viable = []
t_viable = []
m_viable = []

for i in range(0,len(R_list)):
    r = R_list[i]
    L = L_list[i]
    t = t_1_list[i]
    A = pi  * (r**2)
    I = pi * (r**3) * (t) #Only cylinder since its

    sigma_cr_1 = (E_mat* I*((pi)**2))/(A* (L**2))
    sigma_cr_m_1 = sigma_cr_1/1000000

    Q = (p/E_mat)*(r/t)**2
    sigma_cr_2 = (1.983-0.983*(exp(-23.14*Q)))*((E_mat*t)/(r*sqrt(1-v**2)*sqrt(3)))
    sigma_cr_m_2 = sigma_cr_2/1000000

    m = (2*pi*r*t*L + 4*pi*t*(r**2))* rho
    f = 236.6 * m
    sigma_applied = f/(2*pi*r*t)

    if sigma_cr_m_1 > sigma_applied and sigma_cr_m_2 > sigma_applied:
            L_viable.append(L)
            R_viable.append(r)
            t_viable.append(t)
            m_viable.append(m)


print(L_viable)
print(R_viable)
print(t_viable)
print(m_viable)

m_opt = min(m_viable)
m_opt_index = m_viable.index(m_opt)
L_opt = L_viable[m_opt_index]
R_opt = R_viable[m_opt_index]
t_opt = t_viable[m_opt_index]

print(m_opt,L_opt,R_opt,t_opt)