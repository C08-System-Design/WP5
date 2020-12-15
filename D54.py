from math import *
from numpy import *
import matplotlib.pyplot as plt
from D53 import *
from mat import A2195_T84 as mat
# from ... import ...

sigmay = mat.get("sigma_y") * 10**6

tank_mass = buckling_opt(1590, R_lst, t_lst, L_lst, mat)[0][3]

beam_config_list = []

def getForces(i):
    Fx = 1.5 * 3.125 * 9.81 * (180 + tank_mass[i])  # lateral Force (in N) in x direction
    Fy = 1.5 * 3.125 * 9.81 * (180 + tank_mass[i])  # lateral Force (in N) in y direction
    Fz = 7.5 * 3.125 * 9.81 * (180 + tank_mass[i])  # longitudinal Force (in N) in z direction
    return Fx, Fy, Fz

def xyResF(Fx, Fy):                                     # xy plane resultant force
    Fxy =  sqrt(Fx**2 + Fy**2)
    return Fxy

def xyzResF(Fx, Fy, Fz):                                # xyz resultant force
    Fxyz = sqrt(Fx**2 + Fy**2 + Fz**2)
    return Fxyz

def angleLong(Fxy, Fz):                                 # angle at which the xyz force acts (reference point xy-plane)
    angleRad = (0.5*pi) - atan(Fxy/Fz)
    angleDeg =  angleRad * (180/(pi))              # convert to degrees
    return angleDeg

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
    print('The combined stress in one beam is', divide(max(sigma_comb), sigma_y)*100, 'percent the yield strength')
    #Plot
    print(sigma_tab[0][0], y_arr)
    plt.plot(sigma_tab[0], y_arr)
    plt.show()


# for bottom beam i = -1 for top beam i = 1
def stress_simple(sigma_y, alpha, A, Ixx, y_min, y_max, F_lat, i):
    #length beam
    global sigma_comb
    L = 0.774/cos(alpha)
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
        sigma_shear = divide(multiply(M_int, i), Ixx) #shear stress 1D
        sigma_comb = add(sigma_shear, sigma_axial) #comb stress 1D
        #define sigmatab!!!!
        sigma_tab.append(sigma_comb)
    max1 = [abs(max(sigma_tab)), abs(min(sigma_tab))]
    stress_lvl = divide(max(max1), sigma_y)*100
    # print('The combined stress in one beam is', stress_lvl, 'percent the yield strength')

    #Plot
    # plt.plot(sigma_tab, y_arr)
    # print(sigma_axial)

    # plt.axvline(linewidth=0.5, color='r')
    # plt.axhline(linewidth=0.5, color='r')
    #plt.show()

    return stress_lvl
# Make it so that we can plot it


# TO DO: iterate the Ixxgen for increasing values of a b and r -> use the output and plug it into stress_simple -> check if value exceeds 100% if yes increase a/b/r if not save as possible configuration. Loop this for every tank configuration.

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

# Ixx, Aellipscirc, y_min, y_max = Ixxgen(0.02, 0.03, 0.02)

# stress_simple(276*10**6, 50/180*pi, Aellipscirc, Ixx, y_min, y_max, Fx)

# Guess for a b and r (always lower value than expected value)
a, b, r = 0.003, 0.0075, 0.005

# setting for load orientation
o = 1

previous = []
i=0
while i < len(tank_mass):
    Fx, Fy, Fz = getForces(i)
    Ixx, Aellipscirc, y_min, y_max = Ixxgen(a,b,r)
    stress_lvl = stress_simple(sigmay, 50/180*pi, Aellipscirc, Ixx, y_min, y_max, Fx, o)
    if stress_lvl > 100:
        a = increment(a, 0.000000325)
        b = increment(b, 0.000001)
        r = increment(r, 0.0000005)
    
    if stress_lvl <= 100:
        print(stress_lvl)
        if [a,b,r] != previous:
            beam_config_list.append([a, b ,r])
        previous =[a, b, r]
        a = 0.003
        b = 0.0075
        r = 0.005
        i += 1

print(beam_config_list)

