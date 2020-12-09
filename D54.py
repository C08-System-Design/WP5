import math
# from ... import ...

Fx = 1.5 * 3.125 * 9.81 * 180   # lateral Force (in N) in x direction
Fy = 1.5 * 3.125 * 9.81 * 180   # lateral Force (in N) in y direction
Fz = 7.5 * 3.125 * 9.81 * 180   # longitudinal Force (in N) in z direction

def xyResF(Fx, Fy):                                     # xy plane resultant force
    Fxy =  math.sqrt(Fx**2 + Fy**2)
    return Fxy

def xyzResF(Fx, Fy, Fz):                                # xyz resultant force
    Fxyz = math.sqrt(Fx**2 + Fy**2 + Fz**2)
    return Fxyz

def angleLong(Fxy, Fz):                                 # angle at which the xyz force acts (reference point xy-plane)
    angleRad = (0.5*math.pi) - math.atan(Fxy/Fz)
    angleDeg =  angleRad * (180/(math.pi))              # convert to degrees
    return angleDeg

Fxy = xyResF(Fx, Fy)
print(xyzResF(Fx, Fy, Fz))
print(angleLong(Fxy, Fz))
