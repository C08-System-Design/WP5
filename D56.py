''' Plotting displacement '''


import numpy as np
import matplotlib.pyplot as plt

#constants
c_2 = 0
m = 1600                            #mass, implement from other code
omega_n = 2449                      #natural angular frequency
f = 100                             #forcing frequency, given
omega_f = 2*f*np.pi                 #angular forcing frequency
g = 9.81                            #grav acceleration

print(omega_n)
print(omega_f)

#calc coefficient
c_1 = (-0.8*g * (omega_f / omega_n)) / ((omega_n)**2 - (omega_f)**2)


#X axis values
t = np.arange(0,0.05,0.00005) #get time steps for x axis


#Homogeneous solution
hom = c_1 * np.sin(omega_n * t) + c_2 * np.cos(omega_n * t)

#Particular solution
f0 = 0.8*g
Enumerator = (omega_n)*(omega_n) - (omega_f)*(omega_f)

part = (f0/Enumerator) * np.sin(t * omega_f)


#Total displacement
y = part + hom


#Plotting
'''Total displacement'''
plt.figure()
plt.plot(t,y)
#Naming
plt.xlabel('time [s]') 
plt.ylabel('displacement [m]')
plt.title("Total displacement graph")
plt.show()

'''Homog displacement'''
plt.figure()
plt.plot(t,hom)
#Naming
plt.xlabel('time [s]') 
plt.ylabel('displacement [m]')
plt.title("Homogeneous solution")
plt.show()

'''Particular displacement'''
plt.figure()
plt.plot(t,part)
#Naming
plt.xlabel('time [s]') 
plt.ylabel('displacement [m]')
plt.title("Particular solution")
plt.show()
