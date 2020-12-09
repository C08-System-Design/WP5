import sys
import math
from mat import A2195_T84 as mat
# import variables from variable file statically
# import radius from relevant file iteratively

# change these static values to retrieve from variables file
# using al2195-T6
sigmay = mat.get("sigma_y") * 10**6

v = 0.179           # propellant volume
m_prop = 180        # propellant mass
a = 236.6           # launch acceleration + safety factor
t_p = 2.4 * 10**6   # tankage pressure
p = t_p *1.25       # safety margin on pressure

r_structure = 1.024 # satellite primary structure radius
force = m_prop * a  # load due to propellant

# output list initialisation
R_lst = []          # radii
t_lst = []          # thicknesses
L_lst = []          # length cylindrical part


# r = 1.024 - b_l   # radius tankage outer radius is spacecraft radius minus beam length
def get_initial_r(v):
    r_o = ((v*3)/(4*math.pi))**(1/3)      # starting value for outer radius, remove and use previous function as soon as it is available
    return r_o

def get_t_cyl(p, r_o, sigmay):
    t_cyl = (p*r_o)/(sigmay)              # cylindrical stress thickness limit
    return t_cyl

def get_t_axi(r_o, force, sigmay):
    t_axi = (force * (2*r_o))/(4*sigmay)      # propellant mass load (need to add the tank mass)
    return t_axi

def get_t_final(t_axi, t_cyl):
    t_final = t_axi + t_cyl
    return t_final

def get_L(r_o,t_axi,t_cyl,v):
    r_i = r_o - get_t_final(t_axi, t_cyl)     # inner radius
    v_i = ((4)/(3))*math.pi*r_i**3            # inner volume from cylindrical end caps
    v_rest = v - v_i                          # volume still to fill
    L = v_rest/(math.pi*r_i**2)               # add volume with cylindrical part of tank
    return L

# iterate for beam length from minimum length to maximum length
# replace arbitrary iteration for actual beam interval determination
b_l = r_structure - get_initial_r(v)
h = get_initial_r(v)*2
while b_l <= 1.024-0.1 and h <= 1.850: # limit beam to give the tank a radius of at least 10 cm | height limited to 3.54 meters (height of the spacecraft)
    r_o = r_structure - b_l
    R_lst.append(r_o)
    t_axi = get_t_axi(r_o, force, sigmay)
    t_cyl = get_t_cyl(p, r_o, sigmay)
    t_lst.append(get_t_final(t_axi, t_cyl))
    L_lst.append(get_L(r_o, get_t_axi(r_o, force, sigmay), get_t_cyl(p, r_o, sigmay),v))
    h = 2*r_o + get_L(r_o, get_t_axi(r_o, force, sigmay), get_t_cyl(p, r_o, sigmay),v)
    b_l += 0.001
