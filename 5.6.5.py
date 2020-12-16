''' Plotting displacement '''


import numpy as np
import matplotlib.pyplot as plt

#constants
c_1 = 0.002
c_2 = 0.054
k = 5                               #equivalent stiffness
m = 1500                            #mass, implement from other code
omega_n = np.sqrt(m/k)              #natural angular frequency
f = 100                             #forcing frequency, given
omega_f = 2*f*np.pi                 #angular forcing frequency
g = 9.81                            #grav acceleration

print(omega_n)
print(omega_f)

#X axis values
t = np.arange(0,2,0.01) #get time steps for x axis


#Homogeneous solution
hom = c_1 * omega_n * np.sin(omega_n * t) + c_2 * omega_n * np.cos(omega_n * t)

#Particular solution
f0 = 0.8*g*m
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
