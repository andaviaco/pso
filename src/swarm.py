import numpy as np
import random as rand
import pprint as pp
from operator import attrgetter

from particle import Particle

class Swarm(object):
    g_best = None
    particles = []

    """docstring for Swarm"""
    def __init__(self,
        nparticles,
        niterations,
        fn_eval,
        *,
        personal_weight=1,
        global_weight=3,
        inertia_factor=0.6,
        initial_fitness=9999,
        fn_ub=[5, 5],
        fn_lb=[-5, -5],
    ):
        super(Swarm, self).__init__()
        self.nparticles = nparticles
        self.niterations = niterations
        self.fn_eval = fn_eval

        self.personal_weight = personal_weight
        self.global_weight = global_weight
        self.inertia_factor = inertia_factor
        self.initial_fitness = initial_fitness
        self.fn_ub = np.array(fn_ub)
        self.fn_lb = np.array(fn_lb)

    def optimize(self):
        self.initialize_particles()

        for n in range(1, self.niterations):
            for p in self.particles:
                p.update_velocity(self.g_best, self.personal_weight, self.global_weight, self.inertia_factor)
                p.update_position(self.fn_ub, self.fn_lb)

            self.update_fitness()

        return self.g_best

    def initialize_particles(self):
        self.particles = [self.random_particle() for i in range(self.nparticles)]
        self.g_best = self.get_gobal_best()

        return self.particles

    def fitness(self, position):
        result = self.fn_eval(position)

        return result

    def update_fitness(self):
        for p in self.particles:
            p.fitness = self.fitness(p.position)

            if p.fitness < self.fitness(p.best_pos):
                p.best_pos = p.position

            if p.fitness < self.fitness(self.g_best):
                self.g_best = p.position

    def get_gobal_best(self):
        best_particle = min(self.particles, key=attrgetter('fitness'))

        return best_particle.position

    def random_particle(self):
        r_position = self.random_vector(self.fn_ub, self.fn_lb)
        r_velocity = self.random_vector(np.array([1, 1]), np.array([-1, -1]))

        return Particle(r_position, r_velocity, self.fitness(r_position))

    def random_vector(self, ub, lb):
        r = rand.random()

        return lb + (ub - lb) * r
