A7075_T6 = \
    {"rho": 2810,  # Density in kg/m^3
     "E": 71.7,  # Young's modulus in GPa
     "sigma_ult": 590,  # Ultimate tensile strength in MPa
     "sigma_y": 510,  # Yield strength in MPa
     "alpha": 22.0*10**(-6),  # strain per kelvin (@RT)
     "ratio": 0.55  # _pySYS = approx k * sigma_y
     }

A6061_T6 = \
    {"rho": 2700,  # Density in kg/m^3
     "E": 69,  # Young's modulus in GPa
     "sigma_ult": 310,  # Ultimate tensile strength in MPa
     "sigma_y": 270,  # Yield strength in MPa
     "alpha": 23.6*10**(-6),  # strain per kelvin (RT - 100C)
     "ratio": 0.55  # SYS = approx k * sigma_y
     }

Ti_6Al_4V = \
    {"rho": 4500,  # Density in kg/m^3
     "E": 104,  # Young's modulus in GPa
     "sigma_ult": 900,  # Ultimate tensile strength in MPa
     "sigma_y": 880,  # Yield strength in MPa
     "alpha": 9.0*10**(-6),  # strain per kelvin (RT - 100C)
     "ratio": 0.55  # SYS = approx k * sigma_y
     }

A2195_T84 = \
    {"rho": 2700,  # Density in kg/m^3
     "E": 78,  # Young's modulus in GPa
     "sigma_ult": 525,  # Ultimate tensile strength in MPa
     "sigma_y": 490,  # Yield strength in MPa
     "alpha": 22.7*10**(-6),  # Strain per kelvin (guess for now)
     "ratio": 0.55  # SYS = approx k * sigma_y
     }
# NAISI Grade 18Ni (350) Maraging Steel
Steel = \
    {"rho": 7800,  # Density in kg/m^3
     "E": 207,  # Young's modulus in GPa
     "sigma_ult": 1140,  # Ultimate tensile strength in MPa
     "sigma_y": 827,  # Yield strength in MPa
     "alpha": 11.3*10**(-6),  # thermal exp coef in 1/K
     "ratio": 0.55  # SYS = approx k * sigma_y
     }

A8090_T8151 = \
 {"rho": 2540,  # Density in kg/m^3
  "E": 77,  # Young's modulus in GPa
  "sigma_ult": 450,  # Ultimate tensile strength in MPa
  "sigma_y": 370,  # Yield strength in MPa
  "alpha": 21.4*10**(-6),  # thermal exp coef in 1/K
  "ratio": 0.6  # SYS = approx k * sigma_y
  }

mats = [A7075_T6, A6061_T6, Ti_6Al_4V, A2195_T84, Steel, A8090_T8151]

"""
This code stores all defined materials (mats) in a list called mats.
Items in this list are dictionaries containing properties of a single material.
To get these properties, use the .get method with argument being your property.
For example:
A7075_T6.get("rho")
To iterate over the list of all materials, you do the following:
for mat in mats:
    mat.get("rho")
For now, my suggestion would be to import a single material into your code using
    from mat import Al6061_T6 as mat
and use mat.get("yourwantedproperty")
"""