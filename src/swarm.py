import numpy as np
import random as rand
import pprint as pp

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
        fn_ub=np.array([5, 5]),
        fn_lb=np.array([-5, -5]),
    ):
        super(Swarm, self).__init__()
        self.nparticles = nparticles
        self.niterations = niterations
        self.fn_eval = fn_eval
        self.fn_ub = fn_ub
        self.fn_lb = fn_lb

        self.personal_weight = personal_weight
        self.global_weight = global_weight
        self.inertia_factor = inertia_factor

    def optimize(self):
        self.initialize_particles()

        return (0, 0)

    def initialize_particles(self):
        self.particles = [self.random_particle() for i in range(self.nparticles)]
        pp.pprint(self.particles)

    def fitness(self):
        pass

    def update_velocity(self):
        pass

    def update_position(self):
        pass

    def random_particle(self):
        r_position = self.random_vector(self.fn_ub, self.fn_lb)
        r_velocity = self.random_vector(self.fn_ub, self.fn_lb)

        return Particle(r_position, r_velocity)

    def random_vector(self, ub, lb):
        r = rand.random()

        return lb + (ub - lb) * r
