from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from E1 import positive


# -------------------------------------------------------
# Prey class
# -------------------------------------------------------
class Prey:
    def __init__(self, x, alpha, beta):
        self.x = x                   # public
        self.__alpha = alpha         # private
        self.__beta = beta           # private

    # ---- getters ----
    @property
    def alpha(self):
        return self.__alpha

    @property
    def beta(self):
        return self.__beta

    # ---- setters ----
    @alpha.setter
    def alpha(self, value):
        if value <= 0:
            raise ValueError("alpha must be > 0")
        self.__alpha = value

    @beta.setter
    def beta(self, value):
        if value <= 0:
            raise ValueError("beta must be > 0")
        self.__beta = value


# -------------------------------------------------------
# Predator class
# -------------------------------------------------------
class Predator:
    def __init__(self, y, delta, gamma):
        self.y = y                   # public
        self.__delta = delta         # private
        self.__gamma = gamma         # private

    # ---- getters ----
    @property
    def delta(self):
        return self.__delta

    @property
    def gamma(self):
        return self.__gamma

    # ---- setters ----
    @delta.setter
    def delta(self, value):
        if value <= 0:
            raise ValueError("delta must be > 0")
        self.__delta = value

    @gamma.setter
    def gamma(self, value):
        if value <= 0:
            raise ValueError("gamma must be > 0")
        self.__gamma = value


# -------------------------------------------------------
# Propagator class (Forward Euler)
# -------------------------------------------------------
class Propagate:

    def __init__(self, prey, predator):
        self.prey = prey
        self.predator = predator

    def __str__(self):
        return (
            f"Prey: alpha: {self.prey.alpha}, beta: {self.prey.beta}\n"
            f"Predator: gamma: {self.predator.gamma}, delta: {self.predator.delta}"
        )

    # private method for the derivatives
    def __derivatives(self, x, y):
        x_dot = self.prey.alpha * x - self.prey.beta * x * y
        y_dot = self.predator.delta * x * y - self.predator.gamma * y
        return x_dot, y_dot

    # propagate by one Euler time step
    @positive(3)  #  dt > 0
    def step(self, x, y, dt):
        dxdt, dydt = self.__derivatives(x, y)
        x_new = x + dt * dxdt
        y_new = y + dt * dydt
        return x_new, y_new

    # public: simulate from t=0 to t=t1
    @positive  # all args > 0
    def run(self, t1, dt):
        steps = int(t1 / dt)
        xs = np.zeros(steps + 1)
        ys = np.zeros(steps + 1)
        ts = np.linspace(0, t1, steps + 1)

        xs[0] = self.prey.x
        ys[0] = self.predator.y

        for i in range(steps):
            xs[i + 1], ys[i + 1] = self.step(xs[i], ys[i], dt)

        return ts, xs, ys


# -------------------------------------------------------
# Test the model using given parameters
# -------------------------------------------------------
if __name__ == "__main__":

    # Given parameters
    alpha = 1
    beta = 0.1
    gamma = 0.5
    delta = 0.02

    x0 = 100
    y0 = 20

    prey = Prey(x0, alpha, beta)
    predator = Predator(y0, delta, gamma)

    sim = Propagate(prey, predator)
    print(sim)

    # simulate
    #dt zu -0.001 gänder!!!
    # -> fehler
    t, x, y = sim.run(t1=50, dt=-0.001)


    # plot
    plt.figure(figsize=(10, 5))
    plt.plot(t, x, label="Prey (x)")
    plt.plot(t, y, label="Predator (y)")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Lotka–Volterra Predator-Prey Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

