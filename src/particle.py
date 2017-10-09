import numpy as np
import random as rand


class Particle(object):
    best_pos = None

    """docstring for Particle"""
    def __init__(self, initial_position, initial_velocity, initial_fitness):
        super(Particle).__init__()

        self.position = initial_position
        self.velocity = initial_velocity
        self.fitness = initial_fitness
        self.best_pos = initial_position

    def update_velocity(self, g_best_position, personal_weight, global_weight, inertia_factor):
        r1 = rand.random()
        r2 = rand.random()

        personal = r1 * personal_weight * (self.best_pos - self.position)
        social = r2 * global_weight * (g_best_position - self.position )
        result = inertia_factor * self.velocity + personal + social

        self.velocity = np.around(result, decimals=4)

    def update_position(self, ub, lb):
        result = self.position * self.velocity

        for i, res in enumerate(result):
            if res > ub[i]:
                result[i] = ub[i]
                self.velocity *= -1.0
            elif res < lb[i]:
                self.velocity *= -1.0
                result[i] = lb[i]

        self.position = np.around(result, decimals=4)

    def __repr__(self):
        return f'<Particle p: {self.position} v: {self.velocity} f: {self.fitness}>'
