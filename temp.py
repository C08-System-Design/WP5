from D52 import *
from D53 import *
from math import pi

opt = x[0]  # m, L, R, t
sigma_cr_1 = (mat.get("E")*10**9 * math.pi * (opt[2] ** 3) * opt[3] * (pi ** 2)) / (pi*opt[2]**2 * (opt[1] ** 2))
print(sigma_cr_1/(1e6))

Q = (p / mat.get("E")*10**9) * (opt[2] / opt[3]) ** 2
sigma_cr_2 = (1.983 - 0.983 * (math.exp(-23.14 * Q))) * (
        (mat.get("E")*10**9 * opt[3]) / (opt[2] * math.sqrt(1 - v ** 2) * math.sqrt(3)))
print(sigma_cr_2/(1e6))
