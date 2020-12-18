from math import *
from numpy import *
import matplotlib.pyplot as plt
from D53 import *
from mat import A2195_T84 as mat
# from ... import ...

sigmay = mat.get("sigma_y") * 10**6
rho = mat.get("rho") 

tank_mass = buckling_opt(1590, R_lst, t_lst, L_lst, mat)[0][3]
tank_radius = buckling_opt(1590, R_lst, t_lst, L_lst, mat)[0][0]

# print(len(tank_mass))

beam_config_list = []

def getForces(i):
    # lateral Force (in N) in x direction
    Fx = 1.5 * 3.125 * 9.81 * (180 + tank_mass[i])  
    # lateral Force (in N) in y direction
    Fy = 1.5 * 3.125 * 9.81 * (180 + tank_mass[i])  
    # longitudinal Force (in N) in z direction
    Fz = 7.5 * 3.125 * 9.81 * (180 + tank_mass[i])  
    return Fx, Fy, Fz

def xyResF(Fx, Fy):                          # xy plane resultant force
    Fxy =  sqrt(Fx**2 + Fy**2)
    return Fxy

def xyzResF(Fx, Fy, Fz):                     # xyz resultant force
    Fxyz = sqrt(Fx**2 + Fy**2 + Fz**2)
    return Fxyz

# angle of xyz force (wrt xy-plane)
def angleLong(Fxy, Fz):                             
    angleRad = (0.5*pi) - atan(Fxy/Fz)
    angleDeg =  angleRad * (180/(pi))        # convert to degrees
    return angleRad

#First attempt calculation(not used)
def stress(sigma_y, alpha, A, Ixx, y_min, y_max):   
    #length beam
    global sigma_comb
    L = 0.774/cos(alpha)
    F_lat = linspace(-Fx, Fx, 5)
    y_arr = linspace(y_min, y_max, 11)
    axial_list = []
    trans_list = []
    sigma_tab = []
    for Forces in range(len(F_lat)):
        F_axial = cos(alpha)*Fz/8 - cos(pi/2-alpha)*F_lat[Forces]
        # Minus because Compressive
        axial_list.append(-F_axial)
        F_trans = sin(alpha)*Fz/8 + sin(pi/2-alpha)*F_lat[Forces]
        trans_list.append(F_trans)
    axial_list = array(axial_list)
    array(trans_list)
    M_int = multiply(trans_list, L) # array 1D
    #calc stress due to axial forces
    sigma_axial = divide(axial_list, A)
    #calc stress due to shear forces
    for i in y_arr:
        sigma_shear = divide(multiply(M_int, i), Ixx) #shear stress 1D
        sigma_comb = list(add(sigma_shear, sigma_axial)) #comb stress 1D
        #define sigmatab!!!!
        sigma_tab.append(sigma_comb)
    print('combined stress in 1 beam', 
    divide(max(sigma_comb), sigma_y)*100, 'percent of yield')
    #Plot
    print(sigma_tab[0][0], y_arr)
    plt.plot(sigma_tab[0], y_arr)
    plt.show()


# for bottom beam i = -1 for top beam i = 1
def stress_simple(sigma_y, alpha, A, Ixx, y_min, y_max, F_lat, Fz, i, c):
    #length beam
    global sigma_comb
    L = (1.024-tank_radius[c])/sin(alpha)
    # print(1.024-tank_radius[c])
    y_arr = linspace(y_min, y_max, 11)
    sigma_tab = []
    # Minus because Compressive
    F_axial = cos(alpha)*i*Fz/8 + cos(pi/2-alpha)*F_lat/8
    F_trans = sin(alpha)*Fz/8 + sin(pi/2-alpha)*-i*F_lat/8
    M_int = multiply(F_trans, L) # array 1D
    #calc stress due to axial forces
    sigma_axial = divide(F_axial, A)
    #calc stress due to shear forces
    for i in y_arr:
        sigma_shear = divide(multiply(M_int, i), Ixx)      #shear stress 1D
        sigma_comb = add(sigma_shear, sigma_axial)         #comb stress 1D
        #define sigmatab!!!!
        sigma_tab.append(sigma_comb)
    max1 = [abs(max(sigma_tab)), abs(min(sigma_tab))]
    stress_lvl = divide(max(max1), sigma_y)*100
    # print('Combined stress in 1 beam', stress_lvl, '% yield strength')

    #Plot
    # plt.plot(sigma_tab, y_arr)
    # print(sigma_axial)

    # plt.axvline(linewidth=0.5, color='r')
    # plt.axhline(linewidth=0.5, color='r')
    #plt.show()

    return stress_lvl, L
# Make it so that we can plot it


def Ixxgen(a, b, r):
    NA = ((2*b**2)/(3*pi)+b*r +r**2)/(r+b/2)
    y_cilc = r - NA
    y_ellips = 4*b/(3*pi)
    Ixx = 0.25*pi*r**4 + y_cilc**2*pi*r**2 + pi*a*b**3/8 + y_ellips**2*pi*a*b/2
    Aellipscirc = pi*r**2 + pi*a*b/2
    y_max = b+2*r-NA
    y_min = b+2*r-y_max
    return Ixx, Aellipscirc, y_min, y_max

def increment(x, d):
    x = x + d
    return x

def getConfigs(load_ori):
    # Guess for a b and r (always lower value than expected value)
    a, b, r = 0.003, 0.0075, 0.005       
    # load orientation setting [1 or -1]
    o = load_ori       
    # temp list to compare values to eliminate duplicates 
    # reducing the amount of configurations significantly                                             
    # previous = []                                               
    i=0
    while i < len(tank_mass):
        # print(i)
        Fx, Fy, Fz = getForces(i)
        Ixx, Aellipscirc, y_min, y_max = Ixxgen(a,b,r)
        Fxy = xyResF(Fx, Fy)
        alpha = 0.5*pi - angleLong(Fxy, Fz)
        # print(alpha)
        stress_lvl, L = stress_simple(sigmay,80/180*pi,Aellipscirc,Ixx,y_min,y_max,Fx,Fz,o,i)
        if stress_lvl > 100:
            a = increment(a, 0.00000325)
            b = increment(b, 0.00001)
            r = increment(r, 0.000005)
        
        if stress_lvl <= 100:
            # if [a,b,r] != previous:
            #  print(L)
            m = L * Aellipscirc * rho
            # beam_config_list.append([a, b ,r, m])
            beam_config_list.append([a,b,r,m,L,alpha])
            # previous =[a, b, r]
            a = 0.003
            b = 0.0075
            r = 0.005
            i += 1
    
    return beam_config_list

# result = getConfigs(1)
# print(result)
# print(len(result))
# print(len(getConfigs(1)))