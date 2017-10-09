
class Swarm(object):
    g_best = None

    """docstring for Swarm"""
    def __init__(self,
        nparticles,
        niterations,
        fn_eval,
        *,
        personal_weight=1,
        global_weight=3,
        inertia_factor=0.6
    ):
        super(Swarm, self).__init__()
        self.nparticles = nparticles
        self.niterations = niterations
        self.fn_eval = fn_eval

        self.personal_weight = personal_weight
        self.global_weight = global_weight
        self.inertia_factor = inertia_factor

    def optimize(self):
        self.initialize_particles()

        return (0, 0)

    def initialize_particles(self):
        pass

    def fitness(self):
        pass

    def update_velocity(self):
        pass

    def update_position(self):
        pass

    def random_position(self):
        pass
