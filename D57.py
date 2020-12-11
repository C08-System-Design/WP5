# --- Class Particle created --- #
class Particle:
    K = 0.7  # from the reader, true for most metals, therefore out surfaces
    _registry = []

    def __init__(self, name, m, v, rho):
        self._registry.append(self)
        self.name = name
        self.m = m
        self.v = v
        self.rho = rho

    def get_t(self):  # function for projectile penetration depth t
        t = self.K*self.m**0.352*self.v**0.875*self.rho**0.167
        return t


# --- Particle definition, values from Overleaf --- #
mm = Particle("Micrometeorite", 1e-9, 25, 1e-9/1.96e-7)
sod = Particle("Small orbital debris", 5.2e-10*2700, 10, 2.7)
mod = Particle("Medium orbital debris", 5.2e-4*2700, 10, 2.7)
for i in Particle._registry:  # i being an instance of the Particle class
    print("The", i.name, "will need at least", round(i.get_t()*10, 3),
          "mm of penetration thickness")
